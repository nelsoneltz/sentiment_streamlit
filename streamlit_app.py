import streamlit as st
import numpy as np
import pandas as pd
from transformers import BertForSequenceClassification, AutoTokenizer
import torch
caminho_dbfs = {{modelo}}
# Carregue o modelo pré-treinado e o tokenizador
model = BertForSequenceClassification.from_pretrained(caminho_dbfs)
tokenizer = AutoTokenizer.from_pretrained(caminho_dbfs)

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







prompt = st.chat_input("Say something")
if prompt:
    resultado = analise_func(prompt)
    st.write(f"User has sent the following prompt: {resultado}")