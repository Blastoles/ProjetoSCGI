from os import getcwd
from collections import OrderedDict
from PyQt5 import uic, QtWidgets
import numpy as np
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import *
import sys
import pyqtgraph as pg


class viewRelatorio():
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


    def GraficoRelatorioBar(self):
        widget = QWidget()
        btn = QPushButton('Push Button')
        text = QLineEdit("Line Edit")
        check = QCheckBox("Check Box")
        plot = pg.plot()
        y1 = [5, 5, 7, 10, 3, 8, 9, 1, 6, 2]
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        bargraph = pg.BarGraphItem(x=x, height=y1, width=0.6, brush='g')
        plot.addItem(bargraph)
        layout = QGridLayout()
        widget.setLayout(layout)
        layout.addWidget(btn, 0, 0)
        layout.addWidget(text, 1, 0)
        layout.addWidget(check, 3, 0)
        layout.addWidget(plot, 0, 1, 3, 1)
        self.tela.setCentralWidget(widget)

    def __init__(self):
            Local = getcwd()
            Local = Local.split('Controller')
            Local = Local[0].replace('C:', 'C:\\')
            self.tela = uic.loadUi("{}View\Telas\CD_Relatorio.ui".format(Local))

