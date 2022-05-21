from os import getcwd

from PyQt5 import uic, QtWidgets

class viewRelatorio():
    def Show(self):
        self.tela.show()

    def Close(self):
        self.tela.close()

    def Lista(self,i,j,texto):
        self.tela.TB_Impressora.setItem(i, j, QtWidgets.QTableWidgetItem(texto))

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\CD_Relatorio.ui".format(Local))
