## Bibliotecas ##
from os import getcwd
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget

## Classe visualização da tela ##
class viewContagem(QWidget):

    ## Chama a tela ##
    def Show(self):
        self.tela.show()

    ## Fecha a tela ##
    def Close(self):
        self.tela.close()

    ## Mostra impressora ##
    def SetImpressora(self,lista):
        self.tela.CP_Impressora.addItems(lista)

    ## Limpa a tela ##
    def LimparTela(self):
        self.tela.TB_Contagem.clearContents()
        self.tela.TB_Contagem.setRowCount(0)
        self.tela.CP_Impressora.clear()
        self.tela.CP_Impressora.addItem("Selecione a Impressora")
        self.tela.CP_Impressora.addItem("Número de Serie -- Modelo -- Setor -- Sigla do Setor")
        self.tela.CP_Impressora.setCurrentIndex(0)

    ## Mostra lista na tela ##
    def Lista(self,i,j,texto):
        self.tela.TB_Contagem.setItem(i, j, QtWidgets.QTableWidgetItem(texto))

    ## Coleta impressora selecionada ##
    def ImprSelect(self):
        impr = self.tela.CP_Impressora.currentText()
        return impr

    ## Coleta linha selecionada ##
    def LinhaSelect(self):
        linha = self.tela.TB_Contagem.currentRow()
        return linha

    ## Coleta dados da tela ##
    def Dados(self):
        texto = str(self.tela.BR_Pesquisa.text())
        self.tela.BR_Pesquisa.setText("")
        return texto

    ## Coleta dados da linha selecionada ##
    def TextoSelectLinha(self,linhaSelect):
        TextoLinha = []
        TextoLinha.append(self.tela.TB_Contagem.item(linhaSelect, 0).text())
        TextoLinha.append(self.tela.TB_Contagem.item(linhaSelect, 4).text())
        TextoLinha.append(self.tela.TB_Contagem.item(linhaSelect, 5).text())
        return TextoLinha

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.tela = uic.loadUi("..\\View\Telas\CD_Contagem.ui")
