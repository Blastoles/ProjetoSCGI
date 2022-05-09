import sqlite3
from os import getcwd
from Controller.ControllerMensagem import SistemaMensagem


class DAOCadastrarContagem():
    def Lista(self):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT NUM_DE_SERIE, MODELO, SETOR_NOME, SETOR_SIGLA FROM IMPRESSORA")
            lista = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return lista

    def BuscarDados(self,Selec):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT "
                           "NUM_DE_SERIE, MODELO,NOME_AMIGAVEL,SETOR_NOME,MODELO_TPRETO,MODELO_TMARGENTA,MODELO_TAMARELO,MODELO_TAZUL "
                           "FROM IMPRESSORA "
                           "WHERE NUM_DE_SERIE = '{}'".format(Selec))
            selec = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return selec

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        self.Local = Local[0].replace('C:','C:\\')
        self.msg = SistemaMensagem()