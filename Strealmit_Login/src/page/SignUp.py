import streamlit as st
import sqlite3
from Classes.User import User
from Packages import Database
from Packages import ConstantValues

def AnyEmpty(user:User):
    if user.getfirstName()=='' or user.getSecondtName()=='' or user.getMail()=='' or user.getPassword()=='' or user.getPhone()=='' or user.getRecoveryMail()=='' :return True
    return False

def main():
    [dbase, cursor] = Database.CreateDatabase()

    main_container = st.container()

    main_container.title("Cadastrar-se")
    main_container.markdown("---")

    with main_container:
        with st.form(key="auth"):
            left_col, right_col = st.columns(2)
            firstName = left_col.text_input("Nome")
            secondName = right_col.text_input("Sobrenome")
            mail = left_col.text_input("Email")
            recoveryMail = right_col.text_input("Email de Recuperação")
            password = left_col.text_input("Senha", type="password")
            phone = right_col.text_input("Telefone")
            type = 'Padrão'

            submit_button = st.form_submit_button("Cadastrar")
        
        user = User(firstName=firstName, secondName=secondName, mail=mail, password=password, phone=phone, recoveryMail=recoveryMail, type=type)
        
        if AnyEmpty(user):
            st.warning("Por favor, preencha todos os campos.")
        elif len(user.locate(dbase=dbase, cursor=cursor)) != 0:
            st.warning("Usuário já cadastrado.")
        else:
            user.save(dbase, cursor)
            st.info("Usuário cadastrado com sucesso!")
            