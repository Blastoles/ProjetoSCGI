from os import getcwd

from PyQt5 import uic, QtWidgets

class viewContagem():
    def Show(self):
        self.tela.show()

    def Close(self):
        self.tela.close()

    def SetImpressora(self,lista):
        self.tela.CP_Impressora.addItems(lista)

    def LimparTela(self):
        self.tela.TB_Contagem.clearContents()
        self.tela.TB_Contagem.setRowCount(0)
        self.tela.CP_Impressora.clear()
        self.tela.CP_Impressora.addItem("Selecione a Impressora")
        self.tela.CP_Impressora.addItem("Número de Serie -- Modelo -- Setor -- Sigla do Setor")
        self.tela.CP_Impressora.setCurrentIndex(0)

    def Lista(self,i,j,texto):
        self.tela.TB_Contagem.setItem(i, j, QtWidgets.QTableWidgetItem(texto))

    def ImprSelect(self):
        impr = self.tela.CP_Impressora.currentText()
        return impr

    def LinhaSelect(self):
        linha = self.tela.TB_Contagem.currentRow()
        return linha

    def Dados(self):
        texto = str(self.tela.BR_Pesquisa.text())
        self.tela.BR_Pesquisa.setText("")
        return texto

    def TextoSelectLinha(self,linhaSelect):
        TextoLinha = []
        TextoLinha.append(self.tela.TB_Contagem.item(linhaSelect, 0).text())
        TextoLinha.append(self.tela.TB_Contagem.item(linhaSelect, 4).text())
        TextoLinha.append(self.tela.TB_Contagem.item(linhaSelect, 5).text())
        return TextoLinha

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\CD_Contagem.ui".format(Local))
