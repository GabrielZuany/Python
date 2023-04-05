import streamlit as st
import sqlite3
from Classes.User import User
from Packages import Database

[dbase, cursor] = Database.CreateDatabase()

main_container = st.container()

main_container.title("Cadastre-se")
main_container.markdown("---")

username=''
mail=''
password=''

with main_container:
    with st.form(key="auth"):
        username = st.text_input("Usuário")
        mail = st.text_input("Email")
        password = st.text_input("Senha", type="password")

        submit_button = st.form_submit_button("Cadastrar")
    
    user = User(name=username, mail=mail, password=password)
    
    if username == '' or mail == '' or password == '':
        st.warning("Por favor, preencha todos os campos.")
        st.stop()
    elif user.isunique(dbase=dbase, cursor=cursor):        
        user.save(dbase, cursor)
        st.info("Usuário criado com sucesso!")
    else:
        st.warning("Usuário já existente.")
        st.stop()