import sqlite3
from os import getcwd

from Controller.ControllerMensagem import SistemaMensagem


class DAOContagemimpressora():
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

    def Pesquisa(self,Impre):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT NUM_DE_SERIE, MODELO, SETOR_NOME, SETOR_SIGLA, DATA, CONTAGEM, MODELO_TPRETO, CUSTO_PRETO, MODELO_TMARGENTA, CUSTO_MARGENTA, MODELO_TAMARELO, CUSTO_AMARELO, MODELO_TAZUL, CUSTO_AZUL FROM CONTADOR C LEFT JOIN IMPRESSORA I ON C.IMPRESSORA_NUM_DE_SERIE = I.NUM_DE_SERIE WHERE NUM_DE_SERIE = '{}'".format(Impre))
            pesq = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return pesq

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        self.Local = Local[0].replace('C:','C:\\')
        self.msg = SistemaMensagem()