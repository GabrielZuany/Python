import streamlit as st
import sqlite3
from Classes.User import User
from Packages import Database

[dbase, cursor] = Database.CreateDatabase()

main_container = st.container()

main_container.title("Login")
main_container.markdown("---")

username=''
mail=''
password=''
logado = False

with main_container:
    with st.form(key="auth"):
        username = st.text_input("Usuário")
        mail = st.text_input("Email")
        password = st.text_input("Senha", type="password")

        submit_button = st.form_submit_button("Login")
    
    user = User(name=username, mail=mail, password=password)
    
    if username == '' or mail == '' or password == '':
        st.warning("Por favor, preencha todos os campos.")
    elif len(user.locate(dbase=dbase, cursor=cursor)) == 0:
        st.warning("Usuário não encontrado.")
    elif len(user.findCredentials(dbase=dbase, cursor=cursor)) == 0:
        st.warning("Credenciais incorretas.") 
    else: logado = True   
    
    if not logado:
        username=''
        mail=''
        password=''
    else:
        username=user.getUsername()
        mail=user.getMail()
        password=user.getPassword()
        
    st.sidebar.info(f'''
        >
        - Usuário: {username}\n
        - Email: {mail}\n
        - Senha: {password}\n
        >
        ''')
        