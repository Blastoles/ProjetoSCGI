from os import getcwd

from PyQt5 import uic, QtWidgets

class viewImpressora():
    def Show(self):
        self.tela.show()

    def Close(self):
        self.tela.close()

    def LinhaSelect(self):
        linha = self.tela.TB_Impressora.currentRow()
        return linha

    def Dados(self):
        texto = str(self.tela.BR_Pesquisa.text())
        self.tela.BR_Pesquisa.setText("")
        return texto

    def Lista(self,i,j,texto):
        self.tela.TB_Impressora.setItem(i, j, QtWidgets.QTableWidgetItem(texto))

    def TextoSelectLinha(self,linhaSelect):
        TextoLinha = self.tela.TB_Impressora.item(linhaSelect,1).text()
        return TextoLinha

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\CD_Impressora.ui".format(Local))
        #self.tela = uic.loadUi(".\View\Telas\CD_Impressora.ui")