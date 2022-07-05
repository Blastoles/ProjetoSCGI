## Bibliotecas ##
import sqlite3
from os import getcwd
from Controller.ControllerMensagem import SistemaMensagem

## Classe de acesso ao banco ##
class DAORContagem():

    ## Pesquisa dados de impressora com filtro ##
    def BuscarDadosImp(self,imp):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT NUM_DE_SERIE, MODELO, MAC, SETOR_NOME, END_IP, ANO_AQUISICAO FROM IMPRESSORA WHERE NUM_DE_SERIE = '{}'".format(imp))
            DadoImp = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return DadoImp

    def BuscarContagemImp(self,imp):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT DATA, CONTAGEM, CUSTO_PRETO + CUSTO_MARGENTA + CUSTO_AMARELO + CUSTO_AZUL AS CUSTO FROM CONTADOR WHERE IMPRESSORA_NUM_DE_SERIE = '{}' ORDER BY CONTAGEM DESC".format(imp))
            DadoCont = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return DadoCont

    ## Regras, Constante, e Ações ##
    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        self.Local = Local[0].replace('C:','C:\\')
        self.msg = SistemaMensagem()