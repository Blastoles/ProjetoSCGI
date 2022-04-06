from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QDialog
from View.ViewLogin import viewLogin
from Model.ModelLogin import modelLogin
from functools import partial
from DAO.DAOLogin import DAOlogin


class SistemaLogin(QDialog):
    def Iniciar(self):
        self.login.Show()
        self.login.tela.BT_Logar.clicked.connect(partial(self.Validar))
        self.login.tela.BT_Cancelar.clicked.connect(partial(self.login.Close))

    def Validar(self):
        user,senha = self.login.Dados()
        print(user,senha)
        VeriUser = DAOlogin.CheckUser(user)
        if VeriUser[0][0] == user:
            VeriSenha = DAOlogin.CheckSenha(senha)
            if VeriSenha[0][0] == senha:
                print('passou')
            else:
                print('não passou')
        else:
            print('não passou')


    def __init__(self):
        self.login = viewLogin()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sistema = SistemaLogin()

    sistema.Iniciar()

    sys.exit(app.exec())