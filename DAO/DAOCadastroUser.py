## Bibliotecas ##
import sqlite3
from os import getcwd
from Controller.ControllerMensagem import SistemaMensagem

## Classe de acesso ao banco ##
class DAOCadastraruser():

    ## Inserir dados ##
    def InserirDados(self,dados,linhadb):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("INSERT INTO USUARIO "
                               "(ID_USUARIO,NOME,USUARIO,EMAIL,TELEFONE,ADMINISTRADOR,ATIVO,SENHA)"
                               " VALUES "
                               "({},'{}','{}','{}','{}',{},{},'{}')"
                               "".format(linhadb+1,dados[0],dados[3],dados[1],dados[2],int(dados[5]),int(dados[6]),dados[4]))
            banco.commit()
            self.msg.MsgRealizadoComSucesso()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    ## Verificar registro ##
    def CheckUser(self,user):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT USUARIO FROM USUARIO WHERE USUARIO = '{}'".format(user))
            checkuser = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return checkuser

    ## Contar registros no banco ##
    def ContLista(self):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT ID_USUARIO USUARIO FROM USUARIO ORDER BY ID_USUARIO DESC LIMIT 1")
            ContLista = cursor.fetchall()
            if ContLista != []:
                NumLista = ContLista[0][0]
            else:
                NumLista = 0
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return NumLista

    ## Atualizar dados ##
    def UpdateDados(self,Dados):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("UPDATE USUARIO SET "
                           "NOME = '{}', EMAIL = '{}', TELEFONE = '{}', ADMINISTRADOR = '{}', ATIVO = '{}', SENHA = '{}' "
                           "WHERE "
                           "USUARIO = '{}'".format(Dados[0],Dados[1],Dados[2],Dados[5],Dados[6],Dados[4],Dados[3]))
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