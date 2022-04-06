from PyQt5 import uic, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QDialog
from functools import partial
import bcrypt
import View

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