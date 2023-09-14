import requests
from bs4 import BeautifulSoup
from time import sleep
import random
import warnings
import pandas as pd
warnings.filterwarnings("ignore")
header = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

def get_links(numero:int, empresa:str):
    empresa
    response = requests.get(
        f'https://www.reclameaqui.com.br/empresa/{empresa}/lista-reclamacoes/?pagina={numero}&status=EVALUATED',
        verify=False,
        headers=header
    )
    soup = BeautifulSoup(response.text,'html.parser')

    reclamacoes = soup.select('div div a')

    filtrado = ['https://www.reclameaqui.com.br'+link['href'] for link in reclamacoes if link['href'].startswith(f'/{empresa}/')]

    return filtrado

empresas = ['picpay','nubank']
dados_completos = []
for empresa in empresas:
    lista_original =[]
    for i in range(1,11):
        dados = get_links(i,empresa)
        if dados == []:
            break
        lista_original = lista_original + dados
        tempo_dormido = random.randint(2,3)
        print(f' {i} dormindo por {tempo_dormido}')
        sleep(tempo_dormido)
        print(dados)
    dados_completos = dados_completos + lista_original

df = pd.DataFrame(dados_completos)
print(df)




