from os import getcwd
from collections import OrderedDict
from PyQt5 import uic, QtWidgets
import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem,QToolBar, QWidget
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt



class viewRelatorio(QWidget):
    def Show(self):
        self.tela.show()

    def Close(self):
        self.tela.close()

    def Status(self):
        if self.tela.BT_TodosStatus.isChecked():
            return ''
        elif self.tela.BT_Funcionando.isChecked():
            return '1'
        elif self.tela.BT_Desativada.isChecked():
            return '0'

    def Condicao(self):
        if self.tela.BT_TodosCond.isChecked():
            return ''
        elif self.tela.BT_Comprada.isChecked():
            return '0'
        elif self.tela.BT_Alugada.isChecked():
            return '1'

    def Lista(self,i,j,texto):
        self.tela.TB_Impressora.setItem(i, j, QtWidgets.QTableWidgetItem(texto))

    def DataCheck(self):
        if self.tela.BT_DataInicial.isChecked():
            self.tela.CP_DataInicial.setDisabled(False)
        else:
            self.tela.CP_DataInicial.setDisabled(True)
        if self.tela.BT_DataFinal.isChecked():
            self.tela.CP_DataFinal.setDisabled(False)
        else:
            self.tela.CP_DataFinal.setDisabled(True)

    def TabelaCheck(self):
        if self.tela.BT_TodasImpressoras.isChecked():
            self.tela.TB_Impressora.setDisabled(True)
        else:
            self.tela.TB_Impressora.setDisabled(False)

    def ColetaDadosContagem(self):
        if self.tela.BT_TodasImpressoras.isChecked():
            return []
        else:
            lst = []
            for LinhasSelecionadas in self.tela.TB_Impressora.selectedIndexes():
                lst.append(self.tela.TB_Impressora.item(LinhasSelecionadas.row(), 0).text())
            return (list(OrderedDict.fromkeys(lst)))

    def Grafico(self):
        x = ['01/01/2022','02/01/2022','03/01/2022','04/01/2022','05/01/2022']
        y = ['2','2','3','4','5']
        y1 = ['1.3', '2.7', '3', '4.5', '5.9']
        self.tela.grafico.canvas.axes.set_xlabel("Data da Coleta")
        self.tela.grafico.canvas.axes.set_ylabel("Contagem de Impressão")
        self.tela.grafico.canvas.axes.plot(x, y1, label="HP 2055",color = self.Color())
        self.tela.grafico.canvas.axes.plot(x, y, label="HP 4020",color = self.Color())
        self.tela.grafico.canvas.axes.legend()
        self.tela.grafico.canvas.draw()

    def Color(self):
        cor = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
        return cor[0]

    def __init__(self):
        super().__init__()
        self.graf = FigureCanvas()
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:', 'C:\\')
        self.tela = uic.loadUi("{}View\Telas\CD_Relatorio.ui".format(Local))
        self.tela.addToolBar(NavigationToolbar(self.tela.grafico.canvas, self))
