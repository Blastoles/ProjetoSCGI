## Bibliotecas ##
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget

## Classe visualização da tela ##
class viewManutencao(QWidget):

    ## Chama a tela ##
    def Show(self):
        self.tela.show()

    ## Fecha a tela ##
    def Close(self):
        self.tela.close()

    ## Mostra impressora ##
    def SetImpressora(self,lista):
        self.tela.CP_Impressora.addItems(lista)

    ## Limpa tela ##
    def LimparTela(self):
        self.tela.TB_Manutencao.clearContents()
        self.tela.TB_Manutencao.setRowCount(0)
        self.tela.CP_Impressora.clear()
        self.tela.CP_Impressora.addItem("Selecione a Impressora")
        self.tela.CP_Impressora.addItem("Número de Serie -- Modelo -- Setor -- Sigla do Setor")
        self.tela.CP_Impressora.setCurrentIndex(0)

    ## Mostra lista ##
    def Lista(self,i,j,texto):
        self.tela.TB_Manutencao.setItem(i, j, QtWidgets.QTableWidgetItem(texto))

    ## Coleta impressora selecionada ##
    def ImprSelect(self):
        impr = self.tela.CP_Impressora.currentText()
        return impr

    ## Coleta dados da linha selecionada ##
    def LinhaSelect(self):
        linha = self.tela.TB_Manutencao.currentRow()
        return linha

    ## Coleta dados da tela ##
    def Dados(self):
        texto = str(self.tela.BR_Pesquisa.text())
        self.tela.BR_Pesquisa.setText("")
        return texto

    ## Coleta dados selecionados ##
    def TextoSelectLinha(self,linhaSelect):
        TextoLinha = []
        TextoLinha.append(self.tela.TB_Manutencao.item(linhaSelect, 0).text())
        TextoLinha.append(self.tela.TB_Manutencao.item(linhaSelect, 4).text())
        TextoLinha.append(self.tela.TB_Manutencao.item(linhaSelect, 6).text())
        return TextoLinha

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.tela = uic.loadUi("..\\View\Telas\CD_Manutencao.ui")