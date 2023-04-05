import sqlite3

def CreateDatabase():
    dbase = sqlite3.connect('src/Database/database.db')
    cursor = dbase.cursor()
    
    try:
        cursor.execute('CREATE TABLE Usuarios (nome text, email text, password text, type text)')
    except: pass
    
    dbase.commit()
    return [dbase, cursor]
    
