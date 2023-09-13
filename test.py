from string import punctuation
import nltk
from nltk.corpus import stopwords
 
nltk.download('stopwords')


text = '''
Péssimo, por que eu não faço idéia de quem seja a pessoa que recebeu e pra variar esse pessoal sempre dá um monte de desculpas pra dizer o erro foi seu problema é seu! Como eu vou entrar em contato com quem recebeu se não tem número de telefone ou CPF? Mais beleza, muito bom saber que a Nubank age dessa maneira por um único erro e a resposta é não podemos fazer nada. E devido ao sigilo né fica cada um com seus problemas. Fora que ontem a Nubank fez um estorno da UBER sem eu pedir e sem meu conhecimento. Parabéns pra vocês viu o valor muito mais alto que essa que eu errei ficou por isso mesmo! Mais é bom saber disso. Pago a fatura mês e encerro minha conta. Procuro um outro banco onde não vão ficar usando um [Editado pelo Reclame Aqui] pra ficar me enrolando. Obrigado por nada.
'''

for i in list(punctuation):
    text = text.replace(i,'').replace('\n','')


print(text) # texto sem pontuação

lista_palavras = text.split(' ')
lista_palavras = [palavra.lower() for palavra in lista_palavras]

for word in stopwords.words('portuguese'):
    try:
        for x in lista_palavras:
            lista_palavras.remove(word)
    except:
        pass
# print(stopwords.words('portuguese'))


dicio= {}
for word in lista_palavras:
    print(f'{word}: {lista_palavras.count(word)}')
    dicio[word] = lista_palavras.count(word)

sorted_ = sorted(dicio.items(), key=lambda x:x[1], reverse=True)

for key in sorted_:
    print(key[0], key[1])


print(sorted_)