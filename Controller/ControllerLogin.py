from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QDialog
from View.ViewLogin import viewLogin
from functools import partial
from DAO.DAOLogin import DAOlogin
from Controller.ControllerMensagem import SistemaMensagem
from Controller.ControllerMenu import SistemaMenu


class SistemaLogin(QDialog):
    def Iniciar(self):
        self.login.Show()
        self.login.tela.BT_Logar.clicked.connect(partial(self.Validar))
        self.login.tela.BT_Cancelar.clicked.connect(partial(self.login.Close))

    def Validar(self):
        user,senha = self.login.Dados()
        VeriUser = self.daolog.CheckUser(user)
        if VeriUser[0][0] != [] and VeriUser[0][0] == user.upper():
            if VeriUser[0][1] == 1:
                VeriSenha = self.daolog.CheckSenha(senha)
                if VeriSenha != [] and VeriSenha[0][0] == senha:
                    self.menu.Show()
                    self.login.Close()
                else:
                    self.login.MensagemErro()
                    self.msg.MsgErroLogin()
            else:
                self.msg.MsgUserAtivo()
        else:
            self.login.MensagemErro()
            self.msg.MsgErroLogin()


    def __init__(self):
        self.login = viewLogin()
        self.daolog = DAOlogin()
        self.msg = SistemaMensagem()
        self.menu = SistemaMenu()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sistema = SistemaLogin()

    sistema.Iniciar()

    sys.exit(app.exec())