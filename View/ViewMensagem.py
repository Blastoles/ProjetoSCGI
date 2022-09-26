## Bibliotecas ##
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

## Classe visualização da tela ##
class viewMensagem(QWidget):

    ## Chama a tela ##
    def MsgShow(self):
        self.tela.show()

    ## Fecha a tela ##
    def MsgClose(self):
        self.tela.close()

    ## Altera aviso ##
    def MsgErroLogin(self):
        self.tela.TX_Atencao.setText("Usuário ou Senha invalido(s)\nTente novamente!!")

    ## Altera aviso ##
    def MsgFaltaDados(self,falta):
        self.tela.TX_Atencao.setText("Está faltando informações no campo(s)!\n\n{}{}{}".format(falta[0],falta[1],falta[2]))

    ## Altera aviso ##
    def MsgRealizadoComSucesso(self):
        self.tela.TX_Atencao.setText("Realizado com sucesso!!")

    ## Altera aviso ##
    def MsgUserAtivo(self):
        self.tela.TX_Atencao.setText("Usuário Desativado!!")

    ## Altera aviso ##
    def MsgUserCadastrado(self):
        self.tela.TX_Atencao.setText("Já existe um usuário cadastrado com esse usuário!!")

    ## Altera aviso ##
    def MsgErroBando(self):
        self.tela.TX_Atencao.setText("Ocorreu um erro com o Banco de Dados!!")

    ## Altera aviso ##
    def MsgSelecionarImpr(self):
        self.tela.TX_Atencao.setText("Selecione uma impressora valida!!")

    ## Altera aviso ##
    def MsgSelecionarLinha(self):
        self.tela.TX_Atencao.setText("Selecione uma linha da tabela!!")

    ## Altera aviso ##
    def MsgSetorJaCadastrado(self):
        self.tela.TX_Atencao.setText("Já existe um setor com essa 'SIGLA'!!")

    ## Altera aviso ##
    def MsgImprJaCadastrado(self):
        self.tela.TX_Atencao.setText("Já existe uma Impressora com esse 'Número de Série'!!")

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.tela = uic.loadUi("..\\View\Telas\mensagem.ui")
