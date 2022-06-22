from PyQt5.QtWidgets import QMainWindow

from View.ViewRContagem import GRelatorio


class SistemaGRelatorio(QMainWindow):
    def Show(self):
        self.GRela.Show()


    def __init__(self):
        super().__init__()
        self.GRela = GRelatorio()