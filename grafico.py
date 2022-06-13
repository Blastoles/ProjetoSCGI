from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import pandas as pd
import numpy as np


class grafico(QWidget):
    def Show(self):
        plt.plot([1, 2, 3, 4])
        plt.ylabel('some numbers')
        plt.show()


    def __init__(self,parent):
        QWidget.__init__(self, parent)



