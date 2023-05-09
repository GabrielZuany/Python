import sqlite3
import streamlit as st

class User():
    def __init__(self, firstName:str, secondName:str, mail:str, password:str, phone:int, recoveryMail:str, type:str):
        self.__firstName = firstName
        self.__secondName = secondName
        self.__mail = mail
        self.__password = password
        self.__phone = phone
        self.__recoveryMail = recoveryMail
        self.__type = type
        
    def save(self, dbase:sqlite3.Connection, cursor:sqlite3.Cursor)->None:
        cursor.execute(f'INSERT INTO Usuarios VALUES("{self.__firstName}", "{self.__secondName}", "{self.__mail}", "{self.__password}", "Padrão", {self.__phone}, "{self.__recoveryMail}")')
        dbase.commit()
    
    def locate(self, dbase:sqlite3.Connection, cursor:sqlite3.Cursor)->list:
        cursor.execute(f"SELECT * FROM Usuarios WHERE Email='{self.__mail}'")
        return cursor.fetchall()
    
    def isunique(self, dbase:sqlite3.Connection, cursor:sqlite3.Cursor):
        cursor.execute(f"SELECT * FROM Usuarios WHERE (Nome='{self.__firstName}' AND Sobrenome='{self.__secondName}') OR Email='{self.__mail}'")
        if len(cursor.fetchall()) == 0: return True
        return False
    
    def findCredentials(self, dbase:sqlite3.Connection, cursor:sqlite3.Cursor)->None:
        cursor.execute(f"SELECT * FROM Usuarios WHERE Email='{self.__mail}' AND Senha='{self.__password}'")
        return cursor.fetchall()
    
    def delete(self, dbase:sqlite3.Connection, cursor:sqlite3.Cursor)->None:
        cursor.execute(f"DELETE FROM Usuarios WHERE Email='{self.__mail}'")
        dbase.commit()

    def isadmin(self)->None:
        if self.__type == 'Admin': return True
        return False
    
    def getfirstName(self):
        return self.__firstName

    def getSecondtName(self):
        return self.__secondName

    def getPhone(self):
        return self.__phone

    def getType(self):
        return self.__type

    def getRecoveryMail(self):
        return self.__recoveryMail
    
    def getMail(self):
        return self.__mail
    
    def getPassword(self):
        return self.__password
