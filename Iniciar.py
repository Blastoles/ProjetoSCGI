## Bibliotecas ##
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from Controller.ControllerLogin import SistemaLogin

## Classe principal ##
class Iniciar(QMainWindow):

    def Show(self):
        self.Iniciar()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.login = SistemaLogin()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    self = SistemaLogin()
    self.Iniciar()
    sys.exit(app.exec())