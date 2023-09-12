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
st.write('# Home')

st.write('Página de intro teste')
