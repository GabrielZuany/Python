import streamlit as st
import sqlite3
from Classes.User import User
from Packages import Database
from Packages.ConstantValues import *
from page import Login, SignUp, Admin, Sobre
from streamlit_option_menu import option_menu

[dbase, cursor] = Database.CreateDatabase()

def sidebar():
    with st.sidebar:
        selected = option_menu("Menu", ["App", 'Cadastrar', 'Admin', 'Sobre'], 
            icons=['bar-chart', 'plus', 'gear', 'info'], menu_icon="cast", default_index=0)
        st.markdown("---")
        with st.expander("Admin Login (para acessar a área de adm)"):
            st.info(f" - Email: {ADMIN_MAIL}\n - Senha: {ADMIN_PASSWORD}")
    return selected

def main(selected):
    if selected=='App':
        user = Login.main("Login")

    elif selected=='Cadastrar':
        SignUp.main()

    elif selected=='Admin':
        try:
            u = Login.main("Autenticação Necessária")
            u = u.locate(dbase, cursor)
            if u[0][4] == 'Admin':
                Admin.main()
        except:pass

    elif selected=='Sobre':
        Sobre.main()

    else:pass


selected = sidebar()
main(selected)