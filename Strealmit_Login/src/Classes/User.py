import sqlite3
import streamlit as st

class User():
    def __init__(self, name:str, mail:str, password:str):
        self.__name = name
        self.__mail = mail
        self.__password = password
        
    def to_dict(self)->dict:
        return {
            "Username":self.__name,
            "Mail": self.__mail,
            "Password": self.__password,
        }
        
    def save(self, dbase:sqlite3.Connection, cursor:sqlite3.Cursor)->None:
        cursor.execute(f'INSERT INTO Usuarios VALUES("{self.__name}", "{self.__mail}", "{self.__password}", "Padrão")')
        dbase.commit()
    
    def locate(self, dbase:sqlite3.Connection, cursor:sqlite3.Cursor)->list:
        cursor.execute(f"SELECT * FROM Usuarios WHERE nome='{self.__name}' AND email='{self.__mail}'")
        return cursor.fetchall()
    
    def isunique(self, dbase:sqlite3.Connection, cursor:sqlite3.Cursor):
        cursor.execute(f"SELECT * FROM Usuarios WHERE nome='{self.__name}' OR email='{self.__mail}'")
        if len(cursor.fetchall()) == 0: return True
        return False
    
    def findCredentials(self, dbase:sqlite3.Connection, cursor:sqlite3.Cursor)->None:
        cursor.execute(f"SELECT * FROM Usuarios WHERE nome='{self.__name}' AND email='{self.__mail}' AND password='{self.__password}'")
        return cursor.fetchall()
    
    def delete(self, dbase:sqlite3.Connection, cursor:sqlite3.Cursor)->None:
        cursor.execute(f"DELETE FROM Usuarios WHERE nome='{self.__name}' AND email='{self.__mail}' AND password='{self.__password}'")
        dbase.commit()
    
    def getUsername(self):
        return self.__name
    
    def getMail(self):
        return self.__mail
    
    def getPassword(self):
        return self.__password

    def setUsername(self, name:str)-> None:
        self.__name = name
    
    def setMail(self, mail:str)-> None:
        self.__mail = mail
    
    def setPassword(self, password:str)-> None:
        self.__password = password