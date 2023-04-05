import streamlit as st
import sqlite3
from Classes.User import User
from Packages import Database

[dbase, cursor] = Database.CreateDatabase()

main_container = st.container()

username=''
mail=''
password=''
        
cursor.execute("SELECT * FROM Usuarios")
all_users = cursor.fetchall()

with main_container:
    st.title("Admin")
    st.markdown("---")
    left_col, right_col = st.columns(2)
    
    for user in all_users:
        u = User(name=user[0], mail=user[1], password=user[2])
        
        st.info(f'''
            >
            - Usuário: {u.getUsername()}\n
            - Email: {u.getMail()}\n
            - Senha: {u.getPassword()}\n
            >
            ''')
        
        click = st.button(f"Deletar: {u.getUsername()}")
        if click:
            u.delete(dbase, cursor)
            st.stop()
            
        st.markdown("---")
            