import streamlit as st
import sqlite3
from Classes.User import User
from Packages import Database
from Packages import ConstantValues

def main(Title):
    [dbase, cursor] = Database.CreateDatabase()

    main_container = st.container()

    main_container.title(Title)
    main_container.markdown("---")

    mail=''
    password=''

    with main_container:
        with st.form(key="auth"):
            mail = st.text_input("Email")
            password = st.text_input("Senha", type="password")
            submit_button = st.form_submit_button("Login")
        
        user = User(firstName='', secondName='', mail=mail, password=password, phone=0, recoveryMail='', type='')

        if mail == '' or password == '':
            st.warning("Por favor, preencha todos os campos.")
        elif len(user.locate(dbase=dbase, cursor=cursor)) == 0:
            st.warning("Usuário não encontrado.")
        elif len(user.findCredentials(dbase=dbase, cursor=cursor)) == 0:
            st.warning("Credenciais incorretas.") 
        else:
            st.info(f"Usuário autenticado!")
            return user