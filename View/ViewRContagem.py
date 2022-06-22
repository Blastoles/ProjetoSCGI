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



class GRelatorio(QWidget):
    def Show(self):
        self.tela.show()

    def Close(self):
        self.tela.close()

    def __init__(self):
        super().__init__()
        self.graf = FigureCanvas()
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:', 'C:\\')
        self.tela = uic.loadUi("{}View\Telas\TelaRelatorio.ui".format(Local))
        self.tela.addToolBar(NavigationToolbar(self.tela.grafico.canvas, self))
