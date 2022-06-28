## Bibliotecas ##
from os import getcwd
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget

## Classe visualização da tela ##
class viewSetor(QWidget):

    ## Chama a tela ##
    def Show(self):
        self.tela.show()

    ## Fecha a tela ##
    def Close(self):
        self.tela.close()

    ## Mostra a lista ##
    def Lista(self,i,j,texto):
        self.tela.TB_Setor.setItem(i, j, QtWidgets.QTableWidgetItem(texto))

    ## Coleta seleção ##
    def LinhaSelect(self):
        linha = self.tela.TB_Setor.currentRow()
        return linha

    ## Coleta dados ##
    def Dados(self):
        texto = str(self.tela.BR_Pesquisa.text())
        self.tela.BR_Pesquisa.setText("")
        return texto

    ## Coleta dados da linha selecionadad ##
    def TextoSelectLinha(self,linhaSelect):
        TextoLinha = self.tela.TB_Setor.item(linhaSelect,1).text()
        return TextoLinha

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\CD_Setor.ui".format(Local))
