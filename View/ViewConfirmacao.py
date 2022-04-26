from os import getcwd

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class viewConfirmacao(QMessageBox):
    def Show(self):
        self.tela.show()

    def Close(self):
        self.tela.close()

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\Confirmar.ui".format(Local))
        #self.tela = uic.loadUi(".\View\Telas\Confirmar.ui")