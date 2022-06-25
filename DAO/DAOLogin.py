## Bibliotecas ##
import sqlite3
from os import getcwd
from Controller.ControllerMensagem import SistemaMensagem

## Classe de acesso ao banco ##
class DAOlogin():

    ## Busca usuário no banco de dados ##
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

    ## Busca senha no banco de dados ##
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

    ## Regras, Constante, e Ações ##
    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        self.Local = Local[0].replace('C:','C:\\')
        self.msg = SistemaMensagem()
