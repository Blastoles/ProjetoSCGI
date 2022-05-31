import sqlite3
from os import getcwd
from Controller.ControllerMensagem import SistemaMensagem


class DAOCadastrarContagem():
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

    def BuscarDados(self,Selec):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
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

    def UltimaContagem(self,num):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT DATA,CONTAGEM FROM CONTADOR WHERE IMPRESSORA_NUM_DE_SERIE = '{}' ORDER BY CONTAGEM DESC LIMIT '1'".format(num))
            Ultima = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return Ultima

    def InsertContagem(self,dado,linhadb):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("INSERT INTO "
                           "CONTADOR "
                           "VALUES "
                           "({},'{}','{}','{}','{}','{}','{}','{}')".format(linhadb+1,dado[0],dado[1],dado[2],dado[3],dado[4],dado[5],dado[7]))
            banco.commit()
            self.msg.MsgRealizadoComSucesso()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    def UpdateContagem(self,dados):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("UPDATE CONTADOR SET "
                           "CONTAGEM = '{}', "
                           "DATA = '{}', "
                           "CUSTO_PRETO = '{}', "
                           "CUSTO_MARGENTA = '{}', "
                           "CUSTO_AMARELO = '{}', "
                           "CUSTO_AZUL = '{}' "
                           "WHERE ID_CONTADOR = '{}'".format(dados[0],dados[1],dados[2],dados[3],dados[4],dados[5],dados[6]))
            banco.commit()
            self.msg.MsgRealizadoComSucesso()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    def ContLista(self):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT ID_CONTADOR FROM CONTADOR ORDER BY ID_CONTADOR DESC LIMIT 1")
            ContLista = cursor.fetchall()
            if ContLista != []:
                NumLista = ContLista[0][0]
            else:
                NumLista = 0
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return NumLista

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        self.Local = Local[0].replace('C:','C:\\')
        self.msg = SistemaMensagem()