## Bibliotecas ##
import sqlite3
from os import getcwd
from Controller.ControllerMensagem import SistemaMensagem

## Classe acesso ao banco de dados ##
class DAOuser():

    ## Busca todos os dados de usuários cadastrados ##
    def TodaLista(self):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT "
                               "NOME,"
                               "USUARIO,"
                               "EMAIL,"
                               "TELEFONE,"
                               "ATIVO "
                           "FROM "
                               "USUARIO")
            lista = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return lista

    ## Pesquisa na tabela dos usuários determinado texto preenchido na tela ##
    def Pesquisa(self,texto):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT "
                               "NOME,"
                               "USUARIO,"
                               "EMAIL,"
                               "TELEFONE,"
                               "ATIVO "
                           "FROM "
                               "USUARIO "
                           "WHERE "
                               "NOME LIKE '%{}%' "
                           "OR "
                               "USUARIO LIKE '%{}%' "
                           "OR "
                               "EMAIL LIKE '%{}%' "
                           "OR "
                               "TELEFONE LIKE '%{}%'"
                           "".format(texto,texto,texto,texto))
            lista = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return lista

    ## Busca o usuário ##
    def LocalizarUser(self,TextoLista):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT * FROM USUARIO WHERE USUARIO = '{}'".format(TextoLista))
            User = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return User

    ## Exclui registro no banco ##
    def ExcluirUser(self,User):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("DELETE FROM USUARIO WHERE USUARIO = '{}'".format(User))
            banco.commit()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        self.Local = Local[0].replace('C:','C:\\')
        self.msg = SistemaMensagem()
