import sqlite3
from Controller.ControllerMensagem import SistemaMensagem

class DAOuser():

    def TodaLista(self):
        banco = sqlite3.connect('db_contator.db')
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

    def Pesquisa(self,texto):
        banco = sqlite3.connect('db_contator.db')
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

    def __init__(self):
        self.msg = SistemaMensagem()