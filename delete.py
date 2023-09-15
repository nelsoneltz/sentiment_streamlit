import requests
from bs4 import BeautifulSoup
from time import sleep
import random
import warnings
import pandas as pd

header = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(
    # f'https://www.reclameaqui.com.br/picpay/comprei-e-nao-recebi-cashback_HNGppKaord3lDWad/',
    f'https://www.reclameaqui.com.br/picpay/como-pedi-o-cartao-de-debito_fgX5KIEiDCEPn00C/',
    verify=False,
    headers=header
)
soup = BeautifulSoup(response.text,'html.parser')

# reclamacao = soup.find_all('p')

# # print(reclamacao)
# # for p in reclamacao:
# #     print(p.getText())

# print(reclamacao[0].getText() + '\n')
# print(reclamacao[1].getText() + '\n')
# print(reclamacao[2].getText() + '\n')

# CERTOS

complaint_title = soup.find('h1',{'data-testid':'complaint-title'})

complaint_description = soup.find('p',{'data-testid':'complaint-description'})

company_interactions = soup.find_all('div',{'data-testid':'complaint-interaction'})
if len(company_interactions) >2:

    company_response = company_interactions[0]
    print(company_response.getText()[38:])
    consumer_consideration = company_interactions[-1]
    print(consumer_consideration.getText()[51:])
else:
    company_response = company_interactions[0]
    print(company_response.getText()[38:])
    consumer_consideration = company_interactions[1]
    print(consumer_consideration.getText()[51:])

complaint_status = soup.find('div',{'data-testid':'complaint-status'})

complaint_deal_again = soup.find('div',{'data-testid':'complaint-deal-again'})

rating = soup.find('div',{'class':'uh4o7z-3 jSJcMd'})
