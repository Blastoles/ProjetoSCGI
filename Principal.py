from PyQt5 import QtWidgets
from Controller import ControllerLogin






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sistema = ControllerLogin.SistemaLogin()

    sistema.Iniciar()

    sys.exit(app.exec())
