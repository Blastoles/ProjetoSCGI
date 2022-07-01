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
            cursor.execute("")
            banco.commit()
            self.msg.MsgRealizadoComSucesso()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    def BuscarContagemImp(self):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("")
            banco.commit()
            self.msg.MsgRealizadoComSucesso()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        self.Local = Local[0].replace('C:','C:\\')
        self.msg = SistemaMensagem()