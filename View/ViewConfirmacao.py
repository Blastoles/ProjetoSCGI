## Bibliotecas ##
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox

## Classe visualização da tela ##
class viewConfirmacao(QMessageBox):

    ## Chama a tela ##
    def Show(self):
        self.tela.show()

    ## Fecha a tela ##
    def Close(self):
        self.tela.close()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.tela = uic.loadUi("..\\View\Telas\Confirmar.ui")
