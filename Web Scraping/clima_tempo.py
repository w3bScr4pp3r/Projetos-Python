import requests
from bs4 import BeautifulSoup

# URL do site Clima Tempo
url = "https://www.climatempo.com.br/previsao-do-tempo/agora/cidade/83/vilavelha-es"

# Realizando a requisição GET
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    try:
        # Criando o objeto BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        # Buscando a temperatura atual na página
        temperature = soup.find("span", class_="-bold -gray-dark-2 -font-55 _margin-l-20 _center").text
        print("Temperatura atual: ",temperature)
    except:
        print("Erro ao obter dados do Clima Tempo")
