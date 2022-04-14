from PyQt5 import uic, QtWidgets
from View.ViewSetor import viewSetor

class SistemaSetor():

    def Show(self):
        self.viewSetor.Show()

    def __init__(self):
        self.viewSetor = viewSetor()