## Bibliotecas ##
from os import getcwd
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

## Classe visualização da tela ##
class GRelatorio(QWidget):

    ## Chama a tela ##
    def Show(self):
        self.tela.show()

    ## Fecha a tela ##
    def Close(self):
        self.tela.close()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:', 'C:\\')
        self.tela = uic.loadUi("{}View\Telas\TelaRelatorio.ui".format(Local))
