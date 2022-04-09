import sqlite3
from Controller.ControllerMensagem import SistemaMensagem

class DAOlogin():

    def CheckUser(self,user):
        banco = sqlite3.connect('db_contator.db')
        cursor = banco.cursor()
        user_db = ''
        try:
            cursor.execute("SELECT USUARIO FROM USUARIO WHERE USUARIO = '{}'".format(user.upper()))
            user_db = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return user_db

    def CheckSenha(self,senha):
        banco = sqlite3.connect('db_contator.db')
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
        self.msg = SistemaMensagem()