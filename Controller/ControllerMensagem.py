## Bibliotecas ##
from PyQt5.QtWidgets import QMainWindow
from View.ViewMensagem import viewMensagem

## Classe principal ##
class SistemaMensagem(QMainWindow):

    ## Tela erro login ##
    def MsgErroLogin(self):
        self.msg.MsgErroLogin()
        self.MsgShow()

    ## Tela falta dados ##
    def MsgFaltaDados(self,falta):
        self.msg.MsgFaltaDados(falta)
        self.MsgShow()

    ## Tela usuário desativado ##
    def MsgUserAtivo(self):
        self.msg.MsgUserAtivo()
        self.MsgShow()

    ## Tela erro na consulta no banco de dados ##
    def MsgErroBancoDados(self):
        self.msg.MsgErroBando()
        self.MsgShow()

    ## Tela erro duplicidade de dados ##
    def MsgUserJaCadastrado(self):
        self.msg.MsgUserCadastrado()
        self.MsgShow()

    ## Tela falta selecionar impressora ##
    def MsgSelecionarImpr(self):
        self.msg.MsgSelecionarImpr()
        self.MsgShow()

    ## Tela falta selecionar linha ##
    def MsgSelecionarLinha(self):
        self.msg.MsgSelecionarLinha()
        self.MsgShow()

    ## Tela processo realizado com sucesso ##
    def MsgRealizadoComSucesso(self):
        self.msg.MsgRealizadoComSucesso()
        self.MsgShow()

    ## Tela erro duplicidade de dados ##
    def MsgSetorJaCadastrado(self):
        self.msg.MsgSetorJaCadastrado()
        self.MsgShow()

    ## Tela erro duplicidade de dados ##
    def MsgImprJaCadastrado(self):
        self.msg.MsgImprJaCadastrado()
        self.MsgShow()

    ## Fecha tela ##
    def MsgClose(self):
        self.msg.MsgClose()

    ## Chama a tela ##
    def MsgShow(self):
        self.msg.MsgShow()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.msg = viewMensagem()
        #Definição dos botões
        self.msg.tela.BT_OK.clicked.connect(self.MsgClose)
