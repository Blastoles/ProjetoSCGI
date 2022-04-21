import sqlite3
from Controller.ControllerMensagem import SistemaMensagem


class DAOCadastrarSetor():
    def InserirDados(self,dados,linhadb):
        banco = sqlite3.connect('db_contator.db')
        cursor = banco.cursor()
        print(dados[0],linhadb)
        try:
            cursor.execute("INSERT INTO SETOR"
                           "(ID_SETOR,NOME_SETOR,SIGLA,RESPONSAVEL_LOCAL,PRIORIDADE)"
                           "VALUES"
                           "({},'{}','{}','{}',{})".format((linhadb+1),dados[0],dados[1],dados[2],dados[3]))
            #ID,Nome_Setor,Sigla,Responsavel_Local,Prioridade
            banco.commit()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    def CheckUser(self,user):
        banco = sqlite3.connect('db_contator.db')
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT SIGLA FROM SETOR WHERE SIGLA = '{}'".format(user))
            checkuser = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return checkuser

    def ContLista(self):
        banco = sqlite3.connect('db_contator.db')
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT ID_SETOR FROM SETOR")
            ContLista = cursor.fetchall()
            NumLista = len(ContLista)
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return NumLista

    def UpdateDados(self,Dados):
        banco = sqlite3.connect('db_contator.db')
        cursor = banco.cursor()
        try:
            cursor.execute("UPDATE SETOR SET NOME = '{}', SIGLA = '{}', RESPONSAVEL_LOCAL = '{}', PRIORIDADE = '{}' WHERE USUARIO = '{}'".format(Dados[0],Dados[1],Dados[2],Dados[5],Dados[3]))
            banco.commit()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    def __init__(self):
        self.msg = SistemaMensagem()