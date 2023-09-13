import requests
from bs4 import BeautifulSoup
from time import sleep
import random
import warnings
warnings.filterwarnings("ignore")
header = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

def get_links(numero:int):
    empresa = 'picpay'
    response = requests.get(
        f'https://www.reclameaqui.com.br/empresa/{empresa}/lista-reclamacoes/?pagina={numero}&status=EVALUATED',
        verify=False,
        headers=header
    )
    soup = BeautifulSoup(response.text,'html.parser')

    reclamacoes = soup.select('div div a')

    filtrado = [link['href'] for link in reclamacoes if link['href'].startswith(f'/{empresa}/')]

    return filtrado


lista_original =[]
for i in range(50,53):
    if get_links(i) == []:
        break
    lista_original = lista_original + get_links(i)
    print(lista_original)
    tempo_dormido = random.randint(2,10)
    sleep(tempo_dormido)
    print(i)
    print(f'dormindo por {tempo_dormido}')

for index,link in enumerate(lista_original):
    print(index,link)

print(len(lista_original))