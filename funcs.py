import streamlit as st

def imagem(path):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        st.image(path,width=600)

    with col3:
        st.write(' ')