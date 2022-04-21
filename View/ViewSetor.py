from PyQt5 import uic, QtWidgets

class viewSetor():
    def Show(self):
        self.tela.show()

    def Close(self):
        self.tela.close()

    def Lista(self,i,j,texto):
        self.tela.TB_Setor.setItem(i, j, QtWidgets.QTableWidgetItem(texto))

    def __init__(self):
        self.tela = uic.loadUi(".\View\Telas\CD_Setor.ui")
