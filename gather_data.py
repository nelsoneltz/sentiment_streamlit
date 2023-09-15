PAGINAS = 3
EMPRESAS = ['santander']
import funcs
import pandas as pd


dados = funcs.get_links(empresas = EMPRESAS,paginas= PAGINAS)

dados_roubados = []
for link in dados:
    try:
        complaint = funcs.complaint_data(link)
        # print(complaint['complaint_title'])
        dados_roubados.append(complaint)
        print(str(len(dados_roubados))+f'/{PAGINAS*10*len(EMPRESAS)}' +' ' + complaint['complaint_title'])
    except:
        pass
    
print("Criando dataframe...")

base_bonita = pd.DataFrame(dados_roubados)
print("Criando arquivo .csv...")
base_bonita.to_csv('teste.csv',index=False)