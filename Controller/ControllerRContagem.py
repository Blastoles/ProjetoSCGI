from PyQt5.QtWidgets import QMainWindow, QWidget

from View.ViewRContagem import GRelatorio


class SistemaGRelatorio(QWidget):
    def Show(self):
        self.GRela.Show()

    def Close(self):
        self.GRela.Close()

    def __init__(self):
        super().__init__()
        self.GRela = GRelatorio()
        self.GRela.tela.BT_Voltar.clicked.connect(self.Close)