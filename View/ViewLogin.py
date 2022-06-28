## Bibliotecas ##
from PyQt5 import uic
from os import getcwd
from PyQt5.QtWidgets import QWidget

## Classe visualização da tela ##
class viewLogin(QWidget):

    ## Chama a tela ##
    def Show(self):
        self.tela.show()

    ## Fecha a tela ##
    def Close(self):
        self.tela.close()

    ## Coleta os dados preenchidos ##
    def Dados(self):
        usuario = self.tela.CP_Login.text()
        senha = self.tela.CP_Senha.text()
        return usuario,senha

    ## Exibe mensagem de erro ##
    def MensagemErro(self):
        self.tela.Tx_Status.setText("Usuário ou Senha invalido(s)!!")

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\Login.ui".format(Local))
