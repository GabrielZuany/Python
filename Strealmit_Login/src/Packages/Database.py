import sqlite3
from .ConstantValues import *

def CreateDatabase():
    dbase = sqlite3.connect(DATABASE_PATH)
    cursor = dbase.cursor()
    
    try:
        cursor.execute('CREATE TABLE Usuarios (Nome text, Sobrenome text, Email text, Senha text, TipoUsuario text, Telefone integer, EmailRecuperacao text)')
    except: pass
    
    dbase.commit()
    return [dbase, cursor]
    
def GetAllUsers():
    dbase = sqlite3.connect(DATABASE_PATH)
    cursor = dbase.cursor()

    cursor.execute("SELECT * FROM Usuarios")
    return cursor.fetchall()