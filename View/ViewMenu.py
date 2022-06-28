## Bibliotecas ##
from PyQt5 import uic, QtWidgets
from os import getcwd

## Classe visualização da tela ##
class viewMenu(QtWidgets):
    def Show(self):
        self.tela.show()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\Home.ui".format(Local))
