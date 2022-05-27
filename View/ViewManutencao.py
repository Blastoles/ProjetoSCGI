from os import getcwd

from PyQt5 import uic, QtWidgets

class viewManutencao():
    def Show(self):
        self.tela.show()

    def Close(self):
        self.tela.close()

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\CD_Manutencao.ui".format(Local))