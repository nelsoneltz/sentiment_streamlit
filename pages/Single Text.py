import streamlit as st
import numpy as np
import pandas as pd
from transformers import BertForSequenceClassification, AutoTokenizer
import torch
import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt')

st.set_page_config(
    page_title="Sentimento - Home",
    page_icon="🙂",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
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
st.title('Home')
st.header('Sentimento')
st.divider()

# Prompt 1
prompt = st.chat_input("Say something1",key='prompt1')
if prompt:
    resultado1 = analise_func(prompt)
    st.write(f"O sentimento encontrado na frase foi: {resultado1}")


