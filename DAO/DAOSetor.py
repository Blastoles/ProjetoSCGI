import sqlite3
from Controller.ControllerMensagem import SistemaMensagem

class DAOsetor():

    def TodaLista(self):
        banco = sqlite3.connect('db_contator.db')
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT "
                           "NOME_SETOR,SIGLA,PRIORIDADE,RESPONSAVEL_LOCAL "
                           "FROM "
                           "SETOR")
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
                               "NOME_SETOR,"
                               "PRIORIDADE,"
                               "RESPONSAVEL_LOCAL,"
                               "IMPRESSORA_NUM_DE_SERIE,"
                           "FROM "
                               "SETOR "
                           "WHERE "
                               "NOME LIKE '%{}%' "
                           "OR "
                               "PRIORIDADE LIKE '%{}%' "
                           "OR "
                               "RESPONSAVEL_LOCAL LIKE '%{}%' "
                           "OR "
                               "IMPRESSORA_NUM_DE_SERIE LIKE '%{}%'"
                           "".format(texto,texto,texto,texto))
            lista = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return lista

    def LocalizarSetor(self,TextoLista):
        banco = sqlite3.connect('db_contator.db')
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT * FROM SETOR WHERE SIGLA = '{}'".format(TextoLista))
            User = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return User

    def ExcluirSetor(self,idSetor):
        banco = sqlite3.connect('db_contator.db')
        cursor = banco.cursor()
        try:
            cursor.execute("DELETE FROM SETOR WHERE ID_SETOR = '{}'".format(idSetor))
            banco.commit()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    def __init__(self):
        self.msg = SistemaMensagem()