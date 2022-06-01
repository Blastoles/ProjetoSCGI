import sqlite3
from os import getcwd

from Controller.ControllerMensagem import SistemaMensagem


class DAOManutencao():
    def Lista(self):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT NUM_DE_SERIE, MODELO, SETOR_NOME, SETOR_SIGLA FROM IMPRESSORA")
            lista = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return lista

    def Pesquisa(self,Impre):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
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

    def ExcluirContagem(self,dado):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("DELETE FROM CONTADOR WHERE ID_CONTADOR = '{}' AND IMPRESSORA_NUM_DE_SERIE = '{}' AND CONTAGEM = '{}' AND DATA = '{}'".format(dado[0][0],dado[0][1],dado[0][2],dado[0][3]))
            banco.commit()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    def Localizar(self,dado):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
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

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        self.Local = Local[0].replace('C:','C:\\')
        self.msg = SistemaMensagem()