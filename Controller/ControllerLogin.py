from PyQt5 import uic, QtWidgets
from View.ViewLogin import viewLogin
from DAO.DAOLogin import DAOlogin
from Controller.ControllerMensagem import SistemaMensagem
from Controller.ControllerMenu import SistemaMenu


class SistemaLogin():
    def Iniciar(self):
        self.login.Show()

    def Validar(self):
        user,senha = self.login.Dados()
        VeriUser = self.daolog.CheckUser(user)
        if user != '':
            if VeriUser != [] and VeriUser[0][0] == user.upper():
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
        else:
            self.login.MensagemErro()
            self.msg.MsgErroLogin()

    def Close(self):
        self.login.Close()

    def __init__(self):
        self.login = viewLogin()
        self.login.tela.BT_Logar.clicked.connect(self.Validar)
        self.login.tela.BT_Cancelar.clicked.connect(self.Close)
        self.daolog = DAOlogin()
        self.msg = SistemaMensagem()
        self.menu = SistemaMenu()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    self = SistemaLogin()
    self.Iniciar()
    sys.exit(app.exec())
