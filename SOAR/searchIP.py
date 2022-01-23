import PySimpleGUIQt as sg
import requests as rq
import shodan
import csv

api_endpoint = 'https://api.abuseipdb.com/api/v2/check/'

headers = {
    'Accept': 'application/json',
    'Key': 'KEY_API_ABUSEIPDB'
}

key_shodan = 'KEY_API_SHODAN'

api = shodan.Shodan(key_shodan)

csv_rows = []    

sg.theme('Dark Blue 3')  

layout = [  [sg.Text('Origem: ')],
            [sg.Input(key='Origem'), sg.FileBrowse()],
            [sg.Text('Destino: ')],
            [sg.Input(key='Destino'), sg.FileBrowse()],                        
            [sg.Button('Pesquisar', key='Search'), sg.Button('Limpar', key='Clear'), sg.Button('Sair', key='Quit')]]

window = sg.Window('SearchIP v1.0 by Daniel M. Alves', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    elif event == 'Clear':
        window['Origem'].update('')
        window['Destino'].update('')
        
    else:
        
        origem = values['Origem']
        destino = values['Destino']     

        with open(f'{origem}', 'r') as origem:
            csvreader = csv.reader(origem, delimiter=';')
            for row in csvreader:
                csv_rows.append(row)

        with open(f'{destino}', 'w') as destino:

            destino.write('Malicious;IP;DNS;Open Ports;ISP;City;Country;Count\n')

            for item in csv_rows[1:]:

                target = item[0]
                count = item[1]

                response = rq.get(api_endpoint, headers=headers, params={'ipAddress':target})

                try:
                    host = api.host(target)

                    response_data = response.json()['data']

                    if response_data['abuseConfidenceScore'] >= 30:
                        is_malicious = 'Yes'
                    else:
                        is_malicious = 'No'

                    if len(response_data['hostnames']) >= 1:
                        hostname = response_data['hostnames'][0]
                    else:
                        hostname = response_data['domain']

                    if len(host['ports']) >= 1:
                        ports = str(host['ports'])
                    else:
                        ports = 'sem informação'

                    isp = response_data['isp']

                    if len(host['city']) >= 1:
                        city = str(host['city'])
                    else:
                        city = 'sem informação'

                    country = response_data['countryCode']

                    destino.write(is_malicious+';'+target+';'+hostname +
                                ';'+ports+';'+isp+';'+city+';'+country+';'+count+'\n')

                except:

                    destino.write('sem informação;'+target+';sem informação;sem informação;sem informação;sem informação;sem informação;'+count+'\n')

window.close()
