import streamlit as st
import sqlite3
from Classes.User import User
from Packages import Database
from Packages import ConstantValues

def main(): 
    [dbase, cursor] = Database.CreateDatabase()
    cursor.execute("SELECT * FROM Usuarios")
    all_users = cursor.fetchall()

    st.markdown("---")
    st.markdown("## Usuários Cadastrados")
    st.markdown("---")

    for user in all_users:
        nome = user[0]
        sobrenome = user[1]
        mail = user[2]
        senha = user[3]
        tipo = user[4]
        telefone = user[5]
        recuperacao = user[6]

        st.info(f'''
            > - Usuário: {nome} ''' + f'{sobrenome}\n' + f'''
            > - Email: {mail}\n
            > - Senha: {senha}\n
            > - Tipo de Usuário: {tipo}\n
            > - Telefone: {telefone}\n
            > - Email de Recuperação: {recuperacao}\n
        ''')

        if mail=='Admin@mail.com': disabled=True
        else: disabled=False

        delete = st.button(f"Deletar: {nome} "+f"{sobrenome}", disabled=disabled)
        if delete:
            cursor.execute(f"DELETE FROM Usuarios WHERE Email='{mail}'")
            dbase.commit()
            st.stop()

        st.markdown("---")
