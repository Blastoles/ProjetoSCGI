from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QDialog
from View.ViewLogin import viewLogin
from Model.ModelLogin import modelLogin
from functools import partial



class SistemaLogin(QDialog):
    def Iniciar(self):
        viewLogin.Show(self.login)
        self.login.tela.BT_Logar.clicked.connect(partial(modelLogin.PuxaDados,self.login))
        self.login.tela.BT_Cancelar.clicked.connect(partial(viewLogin.Close,self.login))

    def __init__(self):
        self.login = viewLogin()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sistema = SistemaLogin()

    sistema.Iniciar()

    sys.exit(app.exec())