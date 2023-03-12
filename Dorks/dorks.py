import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd

# Define as dorks que serão usadas para a pesquisa
dorks = ['site:.com.br intitle:Index of /wp-content/uploads',
         'site:pastebin.com intitle:login AND password',
         'site:github.com intitle:login AND password']

# Cria uma lista para armazenar os resultados
results = []

# Loop através das dorks
for dork in dorks:
    # Realiza a pesquisa com a dork usando o mecanismo de busca do Google
    dork = dork.replace(" ","+")
    dork = dork.replace(":","%3A")  
    url = f"https://www.google.com.br/search?q={dork}"    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = rq.get(url, headers=headers)

    # Extrai as URLs e títulos das páginas encontradas
    soup = bs(response.text, 'html.parser')
    results_div = soup.find_all('div', class_='MjjYud')

    for result in results_div:
        link = result.find('a')
        title = result.find('h3').text
        url = link['href']
        
        # Adiciona as informações na lista de resultados
        results.append([dork, title, url])

# Cria um DataFrame do pandas com os resultados
df = pd.DataFrame(results, columns=['Dork', 'Título', 'URL'])

# Salva o DataFrame em um arquivo Excel
df.to_excel('dorks.xlsx', index=False)
