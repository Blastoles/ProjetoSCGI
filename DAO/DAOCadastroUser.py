import sqlite3
from Controller.ControllerMensagem import SistemaMensagem


class DAOCadastraruser():

    def InserirDados(self,dados,linhadb):
        banco = sqlite3.connect('db_contator.db')
        cursor = banco.cursor()
        try:
            cursor.execute("INSERT INTO USUARIO "
                               "(ID_USUARIO,NOME,USUARIO,EMAIL,TELEFONE,ADMINISTRADOR,ATIVO,SENHA)"
                               " VALUES "
                               "({},'{}','{}','{}','{}',{},{},'{}')"
                               "".format(int(linhadb),dados[0],dados[3],dados[1],dados[2],int(dados[5]),int(dados[6]),dados[4]))
            #Linha,Nome,Usuario,Email,Telefone,Admin,Ativo,Senha
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

    def __init__(self):
        self.msg = SistemaMensagem()