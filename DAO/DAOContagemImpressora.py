## Bibliotecas ##
import sqlite3
from Controller.ControllerMensagem import SistemaMensagem

## Classe de acesso ao banco ##
class DAOContagemimpressora():

    ## Pesquisa impressora ##
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

    ## Pesquisa dados de contagem ##
    def Pesquisa(self,Impre):
        banco = sqlite3.connect(self.Local)
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT NUM_DE_SERIE, MODELO, SETOR_NOME, SETOR_SIGLA, DATA, CONTAGEM, MODELO_TPRETO, CUSTO_PRETO, MODELO_TMARGENTA, CUSTO_MARGENTA, MODELO_TAMARELO, CUSTO_AMARELO, MODELO_TAZUL, CUSTO_AZUL "
                           "FROM CONTADOR C "
                           "LEFT JOIN IMPRESSORA I "
                           "ON C.IMPRESSORA_NUM_DE_SERIE = I.NUM_DE_SERIE "
                           "WHERE NUM_DE_SERIE = '{}'"
                           "ORDER BY DATA DESC,CONTAGEM DESC".format(Impre))
            pesq = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return pesq

    ## Exclui registro ##
    def ExcluirContagem(self,dado):
        banco = sqlite3.connect(self.Local)
        cursor = banco.cursor()
        try:
            cursor.execute("DELETE FROM CONTADOR WHERE ID_CONTADOR = '{}' AND IMPRESSORA_NUM_DE_SERIE = '{}' AND CONTAGEM = '{}' AND DATA = '{}'".format(dado[0][0],dado[0][1],dado[0][2],dado[0][3]))
            banco.commit()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    ## Localiza contagem, impressora no banco ##
    def Localizar(self,dado):
        banco = sqlite3.connect(self.Local)
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT "
                           "ID_CONTADOR,IMPRESSORA_NUM_DE_SERIE,CONTAGEM,DATA,CUSTO_PRETO,CUSTO_MARGENTA,CUSTO_AMARELO,CUSTO_AZUL "
                           "FROM CONTADOR C LEFT JOIN IMPRESSORA I "
                           "ON C.IMPRESSORA_NUM_DE_SERIE = I.NUM_DE_SERIE "
                           "WHERE IMPRESSORA_NUM_DE_SERIE = '{}' AND DATA = '{}' AND CONTAGEM = '{}' LIMIT 1".format(dado[0],dado[1],dado[2]))
            Dados = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return Dados

    ## Regras, Constante, e Ações ##
    def __init__(self):
        self.Local = '..\\db_contator.db'
        self.msg = SistemaMensagem()