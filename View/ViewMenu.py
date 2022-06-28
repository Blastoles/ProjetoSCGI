## Bibliotecas ##
from PyQt5 import uic
from os import getcwd
from PyQt5.QtWidgets import QWidget

## Classe visualização da tela ##
class viewMenu(QWidget):
    def Show(self):
        self.tela.show()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\Home.ui".format(Local))
