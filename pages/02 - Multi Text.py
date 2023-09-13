import streamlit as st
import numpy as np
import pandas as pd
from transformers import BertForSequenceClassification, AutoTokenizer
import torch
import nltk
from nltk.tokenize import sent_tokenize
@st.cache_resource
def get_nltk():
    nltk.download('punkt')

st.set_page_config(
    page_title="Multi Text Analysis",
    page_icon="🚧",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# Este é um web app criado por Nelson Eltz e Abner Sampaio."
    }
)
@st.cache_resource
def load_model(path):
	  return BertForSequenceClassification.from_pretrained(path)
@st.cache_resource
def load_token(path):
      return AutoTokenizer.from_pretrained(path)

caminho_dbfs = st.secrets['MODELO']
# Carregue o modelo pré-treinado e o tokenizador

model = load_model(caminho_dbfs)
tokenizer = load_token(caminho_dbfs)
get_nltk()

def analise_func(texto:str):

    # Tokenize o texto de entrada
    tokens = tokenizer(texto, return_tensors="pt", padding=True)
    input_ids = tokens["input_ids"]
    attention_mask = tokens["attention_mask"]
    # Fazendo a previsão
    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)
        predicted_class = torch.argmax(outputs.logits, dim=1).item()

    # Mapeie o resultado da classe para rótulos de sentimento
    sentimentos = ["Negativo", "Neutro", "Positivo"]
    sentimento_predito = sentimentos[predicted_class]

    return sentimento_predito

def analise_sentimento_texto(texto):
    texto = texto.replace(',','.')

    frases = sent_tokenize(texto, language="portuguese")  # Divide o texto em frases
    sentimentos_frases = [analise_func(frase) for frase in frases]
    # print(frases)
    return sentimentos_frases,frases

# FRONT
st.title('Multi Text Analysis')
# st.header('Sentimento')
st.divider()

# Prompt 2
prompt2 = st.chat_input("Say something",key='prompt2')
if prompt2:
    resultado2, frases = analise_sentimento_texto(prompt2)

    valores_sentimento = []
    for sentimento in resultado2:
        if sentimento == 'Positivo':
            valores_sentimento.append(1)
        if sentimento == 'Neutro':
            valores_sentimento.append(0)
        if sentimento == 'Negativo':
            valores_sentimento.append(-1)      
    media = sum(valores_sentimento) / len(valores_sentimento)
    st.write(f'## Resultado: {media}')
    # st.write(f"O sentimento encontrado na frase foi: {resultado2}")
    for i in range(len(frases)):
         st.write(frases[i] +' '+  resultado2[i])
