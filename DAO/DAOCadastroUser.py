import sqlite3
from Controller.ControllerMensagem import SistemaMensagem

class DAOCadastraruser():

    def InserirDados(self):
        banco = sqlite3.connect('db_contator.db')
        cursor = banco.cursor()
        try:
            cursor.execute("INSERT INTO USUARIO "
                               "(ID_USUARIO,NOME,USUARIO,EMAIL,TELEFONE,ADMINISTRADOR,ATIVO,SENHA)"
                               " VALUES "
                               "({},'{}','{}','{}','{}',{},{},'{}')"
                               "".format(int(nLista),Nome,Usuario,Email,Telefone,int(Admin),int(Ativo),Hashen)))
            lista = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return lista

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

    def __init__(self):
        self.msg = SistemaMensagem()