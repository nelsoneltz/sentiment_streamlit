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
    page_title="Single Text Analysis",
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

    # print(f"Frase: {texto}")
    # print(f"Sentimento Predito: {sentimento_predito}")
    return sentimento_predito

# FRONT
st.title('Single Text Analysis')
# st.header('Sentimento')
st.divider()

# Prompt 1
prompt = st.chat_input("Say something",key='prompt1')
if prompt:
    resultado1 = analise_func(prompt)
    st.write('## Resultado')
    st.write(f"A sentença: {prompt}")
    st.write(f"Retornou o sentimento: {resultado1}")


