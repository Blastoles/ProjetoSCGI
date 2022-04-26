import sqlite3
from os import getcwd

from Controller.ControllerMensagem import SistemaMensagem

class DAOlogin():

    def CheckUser(self,user):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        user_db = ''
        try:
            cursor.execute("SELECT USUARIO, ATIVO FROM USUARIO WHERE USUARIO = '{}'".format(user.upper()))
            user_db = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return user_db

    def CheckSenha(self,senha):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        senha_db = ''
        try:
            cursor.execute("SELECT SENHA FROM USUARIO WHERE SENHA = '{}'".format(senha))
            senha_db = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return senha_db

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        self.Local = Local[0].replace('C:','C:\\')
        self.msg = SistemaMensagem()