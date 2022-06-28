## Bibliotecas ##
from os import getcwd
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
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\Confirmar.ui".format(Local))
