## Bibliotecas ##
import sqlite3
from os import getcwd
from Controller.ControllerMensagem import SistemaMensagem

## Classe de acesso ao banco ##
class DAOManutencao():

    ## Busca a lista de impressora ##
    def Lista(self):
        banco = sqlite3.connect(self.Local)
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT NUM_DE_SERIE, MODELO, SETOR_NOME, SETOR_SIGLA FROM IMPRESSORA")
            lista = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return lista

    ## Pesquisa impressora, manutenção no banco ##
    def Pesquisa(self,Impre):
        banco = sqlite3.connect(self.Local)
        cursor = banco.cursor()
        filtro = ['BETWEEN','AND']
        try:
            cursor.execute("SELECT "
                           "NUM_DE_SERIE, MODELO, SETOR_NOME, SETOR_SIGLA, DATA_PARADA, TIPO, DESCRICAO, CUSTO, VOLTOU_FUNCIONAR, DATA_VOLTA "
                           "FROM "
                           "MANUTENCAO M "
                           "LEFT JOIN IMPRESSORA I "
                           "ON M.IMPRESSORA_NUM_DE_SERIE = I.NUM_DE_SERIE "
                           "WHERE NUM_DE_SERIE = '{}' "
                           "ORDER BY "
                           "DATA_PARADA DESC".format(Impre))
            pesq = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return pesq

    ## Exclui registro no banco ##
    def ExcluirManutencao(self,dado):
        banco = sqlite3.connect(self.Local)
        cursor = banco.cursor()
        try:
            cursor.execute("DELETE FROM MANUTENCAO WHERE ID_MANUTENCAO = '{}' AND IMPRESSORA_NUM_DE_SERIE = '{}' AND DATA_PARADA = '{}' AND DESCRICAO = '{}'".format(dado[0][0],dado[0][7],dado[0][2],dado[0][3]))
            banco.commit()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    ## Busca manutenção com filtro ##
    def Localizar(self,dado):
        banco = sqlite3.connect(self.Local)
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT "
                           "ID_MANUTENCAO, TIPO, DATA_PARADA, DESCRICAO, CUSTO, VOLTOU_FUNCIONAR, DATA_VOLTA, IMPRESSORA_NUM_DE_SERIE "
                           "FROM "
                           "MANUTENCAO "
                           "WHERE "
                           "IMPRESSORA_NUM_DE_SERIE LIKE '{}' "
                           "AND "
                           "DATA_PARADA LIKE '{}' "
                           "AND "
                           "DESCRICAO LIKE '{}' "
                           "LIMIT 1".format(dado[0],dado[1],dado[2]))
            Dados = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return Dados

    ## Regras, Constante, e Ações ##
    def __init__(self):
        self.Local = '..\\db_contator.db'
        self.msg = SistemaMensagem()
