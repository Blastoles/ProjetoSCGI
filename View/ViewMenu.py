## Bibliotecas ##
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

## Classe visualização da tela ##
class viewMenu(QWidget):
    def Show(self):
        self.tela.show()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.tela = uic.loadUi("..\\View\Telas\Home.ui")
