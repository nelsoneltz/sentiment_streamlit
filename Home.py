import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import funcs

st.set_page_config(
    page_title="Avaliador",
    page_icon="🚧",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# Este é um web app criado por Nelson Eltz e Abner Sampaio."
    }
)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.write('# Avaliador')

# Como centralizar essa imagem?
# st.image("gif1.gif",width=600)
funcs.imagem("gif1.gif")
st.write('#### Desbloqueie a chave para avaliações de atendimento ao cliente mais precisas com o Avaliador. Saber antecipadamente como seus clientes irão avaliar seu serviço é fundamental para o sucesso do seu negócio. Nosso web app permite que você preveja se as avaliações serão positivas, negativas ou neutras com base nas mensagens dos clientes. Seja proativo na melhoria de sua experiência do cliente começando agora.')

left,right = st.columns(2,gap='large')
with left:
    st.write("('#### Por enquanto estamos realizando análises on premise. Mas no futuro a ideia é obter o feedback do Avaliador em tempo real, para uma tomada de decisão mais efetiva sobre o atendimento ao cliente.")
    st.write("('#### Nosso modelo de machine learning foi criado utilizando milhares de mensagens trocadas entre clientes e empresas, bem como suas avaliações sobre o atendimento.")
with right:
    st.image("gif2.gif",use_column_width=True)
   




# st.image("gif1.gif",width=600)

st.divider()


