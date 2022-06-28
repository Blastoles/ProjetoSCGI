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

    ## Grafico da tela ##
    def Grafico(self):
        x = ['01/01/2022','02/01/2022','03/01/2022','04/01/2022','05/01/2022']
        y = ['1','1.3', '2.7', '3', '4.5']
        y1 = ['6','7','8','9','10']
        y2 = ['8', '9', '6', '5', '1']
        self.tela.grafico.canvas.axes.set_xlabel("Data da Coleta")
        self.tela.grafico.canvas.axes.set_ylabel("Contagem de Impressão")
        self.tela.grafico.canvas.axes.plot(x, y, label="HP 2055",color = self.Color())
        self.tela.grafico.canvas.axes.plot(x, y1, label="HP 4020",color = self.Color())
        self.tela.grafico.canvas.axes.plot(x, y2, color=self.Color())
        self.tela.grafico.canvas.axes.legend()
        self.tela.grafico.canvas.draw()

    ## Gera cor aleatoria ##
    def Color(self):
        cor = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
        return cor[0]

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.graf = FigureCanvas()
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:', 'C:\\')
        self.tela = uic.loadUi("{}View\Telas\CD_Relatorio.ui".format(Local))
        self.tela.addToolBar(NavigationToolbar(self.tela.grafico.canvas, self))
