PAGINAS = 10
EMPRESAS = ['picpay','nubank','c6-bank']
import funcs
import pandas as pd


dados = funcs.get_links(empresas = EMPRESAS,paginas= PAGINAS)

dados_roubados = []
for link in dados:
    try:
        complaint = funcs.complaint_data(link)
        print(complaint['complaint_title'])
        dados_roubados.append(complaint)
    except:
        pass

base_bonita = pd.DataFrame(dados_roubados)

base_bonita.to_csv('teste.csv',index=False)