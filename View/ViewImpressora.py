## Bibliotecas ##
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget

## Classe visualização da tela ##
class viewImpressora(QWidget):

    ## Chama a tela ##
    def Show(self):
        self.tela.show()

    ## Fecha a tela ##
    def Close(self):
        self.tela.close()

    ## Coleta a linha selecionada ##
    def LinhaSelect(self):
        linha = self.tela.TB_Impressora.currentRow()
        return linha

    ## Coleta o dado da tela ##
    def Dados(self):
        texto = str(self.tela.BR_Pesquisa.text())
        self.tela.BR_Pesquisa.setText("")
        return texto

    ## Mostra lista ##
    def Lista(self,i,j,texto):
        self.tela.TB_Impressora.setItem(i, j, QtWidgets.QTableWidgetItem(texto))

    ## Coleta linha selecionada ##
    def TextoSelectLinha(self,linhaSelect):
        TextoLinha = self.tela.TB_Impressora.item(linhaSelect,0).text()
        return TextoLinha

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.tela = uic.loadUi("..\\View\Telas\CD_Impressora.ui")