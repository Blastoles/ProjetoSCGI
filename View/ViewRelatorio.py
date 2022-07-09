## Bibliotecas ##
from os import getcwd
from collections import OrderedDict
from PyQt5 import uic, QtWidgets
import random
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

## Classe visualização da tela ##
class viewRelatorio(QWidget):

    ## Chama a tela ##
    def Show(self):
        self.tela.show()

    ## Fecha a tela ##
    def Close(self):
        self.tela.close()

    ## Coleta o status ##
    def Status(self):
        if self.tela.BT_TodosStatus.isChecked():
            return ''
        elif self.tela.BT_Funcionando.isChecked():
            return '1'
        elif self.tela.BT_Desativada.isChecked():
            return '0'

    ## Coleta condição ##
    def Condicao(self):
        if self.tela.BT_TodosCond.isChecked():
            return ''
        elif self.tela.BT_Comprada.isChecked():
            return '0'
        elif self.tela.BT_Alugada.isChecked():
            return '1'

    ## Mostra lista ##
    def Lista(self,i,j,texto):
        self.tela.TB_Impressora.setItem(i, j, QtWidgets.QTableWidgetItem(texto))

    ## Mostra lista ##
    def ListaManu(self,lista):
        self.tela.CB_Impressora.addItems(lista)

    ## Habilita opção na tela ##
    def DataCheck(self):
        if self.tela.BT_DataInicial.isChecked():
            self.tela.CP_DataInicial.setDisabled(False)
        else:
            self.tela.CP_DataInicial.setDisabled(True)
        if self.tela.BT_DataFinal.isChecked():
            self.tela.CP_DataFinal.setDisabled(False)
        else:
            self.tela.CP_DataFinal.setDisabled(True)

    ## Coleta dados da tela ##
    def ColetaDadosContagem(self):
        lst = []
        for LinhasSelecionadas in self.tela.TB_Impressora.selectedIndexes():
            lst.append(self.tela.TB_Impressora.item(LinhasSelecionadas.row(), 0).text())
        return (list(OrderedDict.fromkeys(lst)))


    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:', 'C:\\')
        self.tela = uic.loadUi("{}View\Telas\CD_Relatorio.ui".format(Local))
