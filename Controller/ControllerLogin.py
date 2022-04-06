from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QDialog
from View import ViewLogin
from Model import ModelLogin


class Sistema(QDialog):
    def Iniciar(self):
        View.ViewLogin.Show(self.login)


    def __init__(self):
        self.login = View.ViewLogin()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sistema = Sistema()

    sistema.Iniciar()

    sys.exit(app.exec())