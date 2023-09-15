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

def get_links_from_company(numero:int, empresa:str):
    response = requests.get(
        f'https://www.reclameaqui.com.br/empresa/{empresa}/lista-reclamacoes/?pagina={numero}&status=EVALUATED',
        verify=False,
        headers=header
    )
    soup = BeautifulSoup(response.text,'html.parser')

    reclamacoes = soup.select('div div a')

    filtrado = ['https://www.reclameaqui.com.br'+link['href'] for link in reclamacoes if link['href'].startswith(f'/{empresa}/')]

    return filtrado

def get_links(empresas:list,paginas:int):
    dados_completos = []
    for empresa in empresas:
        lista_original =[]
        for i in range(1,paginas+1):
            dados = get_links_from_company(i,empresa)
            if dados == []:
                break
            lista_original = lista_original + dados
            tempo_dormido = random.randint(2,10)
            print(f'Empresa {empresa}. Página {i}. Aguardando {tempo_dormido} segundos antes de continuar.')
            sleep(tempo_dormido)
            # print(dados)
        dados_completos = dados_completos + lista_original

    # df = pd.DataFrame(dados_completos)
    # print(df)
    return dados_completos

def complaint_data(link:str):
    response = requests.get(
    link,
    verify=False,
    headers=header
    )
    soup = BeautifulSoup(response.text,'html.parser')

    complaint_title = soup.find('h1',{'data-testid':'complaint-title'})

    complaint_description = soup.find('p',{'data-testid':'complaint-description'})

    company_interactions = soup.find_all('div',{'data-testid':'complaint-interaction'})
    if len(company_interactions) >2:
        company_response = company_interactions[0].getText()[38:]
        company_response_time = company_interactions[0].getText()[19:29] +' '+ company_interactions[0].getText()[33:38]+':00'
        # print(company_response.getText()[38:])
        consumer_consideration = company_interactions[-1].getText()[51:]
        consumer_consideration_time = company_interactions[-1].getText()[32:42]+ ' ' +company_interactions[-1].getText()[46:51] +':00'
        # print(consumer_consideration.getText()[51:])
    else:
        company_response = company_interactions[0].getText()[38:]
        company_response_time = company_interactions[0].getText()[19:29] +' '+ company_interactions[0].getText()[33:38]+':00'
        # print(company_response.getText()[38:])
        consumer_consideration = company_interactions[1].getText()[51:]
        consumer_consideration_time = company_interactions[-1].getText()[32:42]+ ' ' +company_interactions[-1].getText()[46:51] +':00'
        # print(consumer_consideration.getText()[51:])
        
    complaint_status = soup.find('div',{'data-testid':'complaint-status'})

    complaint_deal_again = soup.find('div',{'data-testid':'complaint-deal-again'})

    rating = soup.find('div',{'class':'uh4o7z-3 jSJcMd'})

    data_dict = {
        "complaint_title":complaint_title.getText(),
        "complaint_description":complaint_description.getText(),
        "company_response":company_response,
        "company_response_time":company_response_time,
        "consumer_consideration":consumer_consideration,
        "consumer_consideration_time":consumer_consideration_time,
        "complaint_status":complaint_status.getText(),
        "complaint_deal_again":complaint_deal_again.getText(),
        "rating":rating.getText(),
    }
    # print(data_dict['company_response'])
    # print(data_dict['company_response_time'])
    # print(data_dict['consumer_consideration'])
    # print(data_dict['consumer_consideration_time'])
    return data_dict

# print(complaint_data('https://www.reclameaqui.com.br/picpay/comprei-e-nao-recebi-cashback_HNGppKaord3lDWad/'))
# print(complaint_data('https://www.reclameaqui.com.br/picpay/como-pedi-o-cartao-de-debito_fgX5KIEiDCEPn00C/'))






