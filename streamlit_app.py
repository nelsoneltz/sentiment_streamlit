import streamlit as st
import numpy as np
import pandas as pd
st.title('Home')
st.header('Sentimento')
st.divider()


prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")