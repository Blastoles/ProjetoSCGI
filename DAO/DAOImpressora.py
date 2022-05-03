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
                 "NUM_DE_SERIE,MODELO,NOME_AMIGAVEL,SETOR_NOME,END_IP,MODELO_TPRETO,MODELO_TMARGENTA,MODELO_TAMARELO,MODELO_TAZUL "
                 "FROM "
                 "IMPRESSORA "
                 "WHERE "
                 "NUM_DE_SERIE LIKE '%{}%' OR "
                 "MODELO LIKE '%{}%' OR "
                 "NOME_AMIGAVEL LIKE '%{}%' OR "
                 "SETOR_NOME LIKE '%{}%' OR "
                 "END_IP LIKE '%{}%' OR "
                 "MODELO_TPRETO LIKE '%{}%' OR "
                 "MODELO_TMARGENTA LIKE '%{}%' OR "
                 "MODELO_TAMARELO LIKE '%{}%' OR "
                 "MODELO_TAZUL LIKE '%{}%'".format(texto,texto,texto,texto,texto,texto,texto,texto,texto))
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

    def ExcluirImpr(self, Setor):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("DELETE FROM IMPRESSORA WHERE NUM_DE_SERIE = '{}'".format(Setor))
            banco.commit()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        self.Local = Local[0].replace('C:', 'C:\\')
        self.msg = SistemaMensagem()