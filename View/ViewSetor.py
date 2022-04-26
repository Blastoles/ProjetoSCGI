from os import getcwd

from PyQt5 import uic, QtWidgets

class viewSetor():
    def Show(self):
        self.tela.show()

    def Close(self):
        self.tela.close()

    def Lista(self,i,j,texto):
        self.tela.TB_Setor.setItem(i, j, QtWidgets.QTableWidgetItem(texto))

    def LinhaSelect(self):
        linha = self.tela.TB_Setor.currentRow()
        return linha

    def TextoSelectLinha(self,linhaSelect):
        TextoLinha = self.tela.TB_Setor.item(linhaSelect,1).text()
        return TextoLinha

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\CD_Setor.ui".format(Local))
        #self.tela = uic.loadUi(".\View\Telas\CD_Setor.ui")
