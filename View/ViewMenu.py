## Bibliotecas ##
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

## Classe visualização da tela ##
class viewMenu(QWidget):
    def Show(self, permi):
        if permi == 1:
            self.tela.BT_Usuario.setDisabled(False)
            self.tela.BT_Setor.setDisabled(False)
            self.tela.BT_Impressora.setDisabled(False)
        elif permi == 0:
            self.tela.BT_Usuario.setDisabled(True)
            self.tela.BT_Setor.setDisabled(True)
            self.tela.BT_Impressora.setDisabled(True)
        self.tela.show()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.tela = uic.loadUi("..\\View\Telas\Home.ui")
