import sqlite3
from os import getcwd

from Controller.ControllerMensagem import SistemaMensagem


class DAOCadastrarimpressora():
    def InserirDados(self,dados,linhadb):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("INSERT INTO IMPRESSORA VALUES ({},'{}','{}','{}','{}','{}','{}','{}','{}',{},{},{},{},{},'{}',{},'{}',{},'{}','{}','{}'"
                           ")".format((linhadb+1),dados[0],dados[1],dados[2],dados[3],dados[4],dados[5],dados[6],dados[7],dados[8],dados[9],dados[10],dados[11],dados[12],dados[13],dados[14],dados[15],dados[16],dados[17],dados[18],dados[19]))
            #ID_IMPRESSORA,NUM_DE_SERIE,MAC,MODELO,FABRICANTE,NOME_AMIGAVEL,ANO_AQUISICAO,SETOR_NOME,SETOR_SIGLA,ATIVO,ALUGADA,USB,REDE,WIFI,END.IP,MONOCROMATIVO,MODELO_TPRETO,CROMATICO,MODELO_TMARGENTA,MODELO_TAMARELO,MODELO_TAZUL
            banco.commit()
            self.msg.MsgRealizadoComSucesso()
        except:
            self.msg.MsgErroBancoDados()
            banco.close()

    def ConsultaSetor(self):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT NOME_SETOR,SIGLA FROM SETOR")
            setor = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return setor

    def CheckUser(self,user):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT SIGLA FROM SETOR WHERE SIGLA = '{}'".format(user))
            checkuser = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return checkuser

    def ContLista(self):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT ID_IMPRESSORA FROM IMPRESSORA")
            ContLista = cursor.fetchall()
            NumLista = len(ContLista)
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return NumLista

    def UpdateDados(self,Dados):
        banco = sqlite3.connect('{}db_contator.db'.format(self.Local))
        cursor = banco.cursor()
        try:
            cursor.execute("UPDATE "
                           "SETOR SET "
                           "NOME_SETOR = '{}', RESPONSAVEL_LOCAL = '{}', PRIORIDADE = '{}' "
                           "WHERE "
                           "SIGLA = '{}'".format(Dados[0],Dados[2],Dados[3],Dados[1]))
            banco.commit()
            self.msg.MsgRealizadoComSucesso()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        self.Local = Local[0].replace('C:','C:\\')
        self.msg = SistemaMensagem()