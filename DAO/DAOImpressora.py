import sqlite3
from os import getcwd

from Controller.ControllerMensagem import SistemaMensagem

class DAOimpressora():
    def TodaLista(self):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT "
                           "NUM_DE_SERIE,MODELO,NOME_AMIGAVEL,SETOR_NOME,END_IP,MODELO_TPRETO,MODELO_TMARGENTA,MODELO_TAMARELO,MODELO_TAZUL "
                           "FROM "
                           "IMPRESSORA")
            lista = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return lista

    def Pesquisa(self, texto):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT "
                           "NOME_SETOR,SIGLA,PRIORIDADE,RESPONSAVEL_LOCAL "
                           "FROM "
                           "SETOR "
                           "WHERE "
                           "NOME_SETOR LIKE '%{}%' OR PRIORIDADE LIKE '%{}%' OR RESPONSAVEL_LOCAL LIKE '%{}%' OR SIGLA LIKE '%{}%'".format(
                texto, texto, texto, texto))
            lista = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return lista

    def LocalizarImp(self, TextoLista):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT * FROM IMPRESSORA WHERE NUM_DE_SERIE = '{}'".format(TextoLista))
            User = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return User

    def ExcluirSetor(self, Setor):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("DELETE FROM SETOR WHERE SIGLA = '{}'".format(Setor))
            banco.commit()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        self.Local = Local[0].replace('C:', 'C:\\')
        self.msg = SistemaMensagem()