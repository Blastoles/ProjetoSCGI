import sqlite3
from os import getcwd

from Controller.ControllerMensagem import SistemaMensagem

class DAORelatorio():

    def BuscarDadosBD(self,filtro,cond):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT NUM_DE_SERIE, MODELO, SETOR_NOME, SETOR_SIGLA "
                           "FROM IMPRESSORA "
                           "WHERE ATIVO {} {} AND ALUGADA {} {}".format(cond[0],filtro[0],cond[1],filtro[1]))
            lista = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return lista


    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        self.Local = Local[0].replace('C:','C:\\')
        self.msg = SistemaMensagem()