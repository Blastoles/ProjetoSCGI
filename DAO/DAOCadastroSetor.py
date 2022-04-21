import sqlite3
from Controller.ControllerMensagem import SistemaMensagem


class DAOCadastrarSetor():
    def InserirDados(self,dados,linhadb):
        banco = sqlite3.connect('db_contator.db')
        cursor = banco.cursor()
        try:
            cursor.execute("INSERT INTO SETOR "
                               "(NOME,RESPONSAVEL,PRIORIDADE)"
                               " VALUES "
                               "({},'{}','{}','{}')"
                               "".format(int(linhadb),dados[0],dados[3],dados[1]))
            #Linha,Nome,
            banco.commit()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    def CheckUser(self,user):
        banco = sqlite3.connect('db_contator.db')
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT USUARIO FROM USUARIO WHERE USUARIO = '{}'".format(user))
            checkuser = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return checkuser

    def ContLista(self):
        banco = sqlite3.connect('db_contator.db')
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT ID_USUARIO USUARIO FROM USUARIO")
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
            cursor.execute("UPDATE USUARIO SET NOME = '{}', EMAIL = '{}', TELEFONE = '{}', ADMINISTRADOR = '{}', ATIVO = '{}', SENHA = '{}' WHERE USUARIO = '{}'".format(Dados[0],Dados[1],Dados[2],Dados[5],Dados[6],Dados[4],Dados[3]))
            banco.commit()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    def __init__(self):
        self.msg = SistemaMensagem()