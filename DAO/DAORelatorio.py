## Bibliotecas ##
import sqlite3
from os import getcwd
from Controller.ControllerMensagem import SistemaMensagem

## Classe de acesso ao banco ##
class DAORelatorio():

    ## Busca dados de impressoras com filtro ##
    def BuscarDadosBD(self,filtro,cond):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT NUM_DE_SERIE, MODELO, SETOR_NOME, SETOR_SIGLA, ATIVO, ALUGADA "
                           "FROM IMPRESSORA "
                           "WHERE ATIVO {} {} AND ALUGADA {} {}".format(cond[0],filtro[0],cond[1],filtro[1]))
            lista = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return lista

    ## Busca manutenção de impressoras com filtro ##
    def BuscarManutencao(self,manu):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT TIPO, DATA_PARADA, CUSTO FROM MANUTENCAO WHERE IMPRESSORA_NUM_DE_SERIE = '{}'".format(manu))
            lista = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return lista

    ## Busca DADOS de MANUTENCAO com filtro ##
    def BuscarDadoManu(self,manu):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT DATA_PARADA, CUSTO, TIPO, DATA_VOLTA FROM MANUTENCAO WHERE IMPRESSORA_NUM_DE_SERIE = '{}' AND DATA_PARADA = '{}' AND CUSTO = '{}'")
            lista = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return lista

    ## Regras, Constante, e Ações ##
    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        self.Local = Local[0].replace('C:','C:\\')
        self.msg = SistemaMensagem()