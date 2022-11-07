## Bibliotecas ##
import sqlite3
from Controller.ControllerMensagem import SistemaMensagem

## Classe de acesso ao banco ##
class DAOimpressora():

    ## Busca lista de impressora ##
    def TodaLista(self):
        banco = sqlite3.connect(self.Local)
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT "
                           "NUM_DE_SERIE,MODELO,NOME_AMIGAVEL,SETOR_NOME,END_IP,MODELO_TPRETO,MODELO_TMARGENTA,MODELO_TAMARELO,MODELO_TAZUL "
                           "FROM "
                           "IMPRESSORA")
            lista = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return lista

    ## Pesquisa impressora com filtro ##
    def Pesquisa(self, texto):
        banco = sqlite3.connect(self.Local)
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT "
                 "NUM_DE_SERIE,MODELO,NOME_AMIGAVEL,SETOR_NOME,END_IP,MODELO_TPRETO,MODELO_TMARGENTA,MODELO_TAMARELO,MODELO_TAZUL "
                 "FROM "
                 "IMPRESSORA "
                 "WHERE "
                 "NUM_DE_SERIE LIKE '%{}%' OR "
                 "MODELO LIKE '%{}%' OR "
                 "NOME_AMIGAVEL LIKE '%{}%' OR "
                 "SETOR_NOME LIKE '%{}%' OR "
                 "END_IP LIKE '%{}%' OR "
                 "MODELO_TPRETO LIKE '%{}%' OR "
                 "MODELO_TMARGENTA LIKE '%{}%' OR "
                 "MODELO_TAMARELO LIKE '%{}%' OR "
                 "MODELO_TAZUL LIKE '%{}%'".format(texto,texto,texto,texto,texto,texto,texto,texto,texto))
            lista = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return lista

    ## Busca impressora ##
    def LocalizarImp(self, TextoLista):
        banco = sqlite3.connect(self.Local)
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT * FROM IMPRESSORA WHERE NUM_DE_SERIE = '{}'".format(TextoLista))
            User = cursor.fetchall()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()
        return User

    ## Exclui registro ##
    def ExcluirImpr(self, Setor):
        banco = sqlite3.connect(self.Local)
        cursor = banco.cursor()
        try:
            cursor.execute("DELETE FROM IMPRESSORA WHERE NUM_DE_SERIE = '{}'".format(Setor))
            banco.commit()
        except:
            self.msg.MsgErroBancoDados()
        banco.close()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        self.Local = '..\\db_contator.db'
        self.msg = SistemaMensagem()