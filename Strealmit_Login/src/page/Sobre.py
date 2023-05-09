import streamlit as st
import sqlite3
from Classes.User import User

def main():
    with st.container():
        st.title("Sobre:")
        st.markdown("---")

        st.info(f'''
        > - Código Fonte: https://github.com/GabrielZuany/Streamlit-Login\n
        > - Autor: Gabriel Zuany\n
        > - Data: 07/04/2023
        ''')
        