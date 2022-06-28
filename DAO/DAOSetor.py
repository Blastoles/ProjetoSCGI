## Bibliotecas ##
import sqlite3
from os import getcwd
from Controller.ControllerMensagem import SistemaMensagem

## Classe de acesso ao banco ##
class DAOsetor():

    ## Busca setor ##
    def TodaLista(self):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT "
                           "NOME_SETOR,SIGLA,PRIORIDADE,RESPONSAVEL_LOCAL "
                           "FROM "
                           "SETOR")
            lista = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return lista

    ## Pesquisa dados com filtro ##
    def Pesquisa(self,texto):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT "
                           "NOME_SETOR,SIGLA,PRIORIDADE,RESPONSAVEL_LOCAL "
                           "FROM "
                           "SETOR "
                           "WHERE "
                           "NOME_SETOR LIKE '%{}%' OR PRIORIDADE LIKE '%{}%' OR RESPONSAVEL_LOCAL LIKE '%{}%' OR SIGLA LIKE '%{}%'".format(texto,texto,texto,texto))
            lista = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return lista

    ## Busca setor ##
    def LocalizarSetor(self,TextoLista):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT * FROM SETOR WHERE SIGLA = '{}'".format(TextoLista))
            User = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return User

    ## Exclui registro ##
    def ExcluirSetor(self,Setor):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("DELETE FROM SETOR WHERE SIGLA = '{}'".format(Setor))
            banco.commit()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        self.Local = Local[0].replace('C:','C:\\')
        self.msg = SistemaMensagem()