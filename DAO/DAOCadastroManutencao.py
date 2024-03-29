## Bibliotecas ##
import sqlite3
from Controller.ControllerMensagem import SistemaMensagem

## Classe de acesso ao banco ##
class DAOCadastrarManutencao():

    ## Busca lista de registro ##
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

    ## Pesquisa dados ##
    def BuscarDados(self,Selec):
        banco = sqlite3.connect(self.Local)
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT "
                           "NUM_DE_SERIE, MODELO,NOME_AMIGAVEL,SETOR_NOME,MODELO_TPRETO,MODELO_TMARGENTA,MODELO_TAMARELO,MODELO_TAZUL "
                           "FROM IMPRESSORA "
                           "WHERE NUM_DE_SERIE = '{}'".format(Selec))
            selec = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return selec

    ## Inserir dados ##
    def InsertManutencao(self,dado,linhadb):
        banco = sqlite3.connect(self.Local)
        cursor = banco.cursor()
        try:
            cursor.execute("INSERT INTO "
                           "MANUTENCAO "
                           "VALUES "
                           "({},'{}','{}','{}','{}','{}','{}','{}')".format(linhadb+1,dado[0],dado[1],dado[2],dado[3],dado[4],dado[5],dado[6]))
            banco.commit()
            self.msg.MsgRealizadoComSucesso()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    ## Atualizar dados ##
    def UpdateManutencao(self,dados):
        banco = sqlite3.connect(self.Local)
        cursor = banco.cursor()
        try:
            cursor.execute("UPDATE MANUTENCAO SET "
                           "TIPO = '{}', "
                           "DATA_PARADA = '{}', "
                           "DESCRICAO = '{}', "
                           "CUSTO = '{}', "
                           "VOLTOU_FUNCIONAR = '{}', "
                           "DATA_VOLTA = '{}' "
                           "WHERE ID_MANUTENCAO = '{}'".format(dados[0],dados[1],dados[2],dados[3],dados[4],dados[5],dados[6][0]))
            banco.commit()
            self.msg.MsgRealizadoComSucesso()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    ## Contar quantidade de registro ##
    def ContLista(self):
        banco = sqlite3.connect(self.Local)
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT ID_MANUTENCAO FROM MANUTENCAO ORDER BY ID_MANUTENCAO DESC LIMIT 1")
            ContLista = cursor.fetchall()
            if ContLista != []:
                NumLista = ContLista[0][0]
            else:
                NumLista = 0
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return NumLista

    ## Regras, Constante, e Ações ##
    def __init__(self):
        self.Local = '..\\db_contator.db'
        self.msg = SistemaMensagem()