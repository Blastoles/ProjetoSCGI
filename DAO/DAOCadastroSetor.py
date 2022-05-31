import sqlite3
from os import getcwd

from Controller.ControllerMensagem import SistemaMensagem


class DAOCadastrarSetor():
    def InserirDados(self,dados,linhadb):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("INSERT INTO SETOR"
                           "(ID_SETOR,NOME_SETOR,SIGLA,RESPONSAVEL_LOCAL,PRIORIDADE)"
                           "VALUES"
                           "({},'{}','{}','{}',{})".format((linhadb+1),dados[0],dados[1],dados[2],dados[3]))
            #ID,Nome_Setor,Sigla,Responsavel_Local,Prioridade
            banco.commit()
            self.msg.MsgRealizadoComSucesso()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    def CheckUser(self,user):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT SIGLA FROM SETOR WHERE SIGLA = '{}'".format(user))
            checkuser = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return checkuser

    def ContLista(self):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT ID_SETOR FROM SETOR ORDER BY ID_SETOR DESC LIMIT 1")
            ContLista = cursor.fetchall()
            if ContLista != []:
                NumLista = ContLista[0][0]
            else:
                NumLista = 0
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return NumLista

    def UpdateDados(self,Dados):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("UPDATE "
                           "SETOR SET "
                           "NOME_SETOR = '{}', RESPONSAVEL_LOCAL = '{}', PRIORIDADE = '{}' "
                           "WHERE "
                           "SIGLA = '{}'".format(Dados[0],Dados[2],Dados[3],Dados[1]))
            banco.commit()
            self.msg.MsgRealizadoComSucesso()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        self.Local = Local[0].replace('C:','C:\\')
        self.msg = SistemaMensagem()