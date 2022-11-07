## Bibliotecas ##
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from View.ViewLogin import viewLogin
from DAO.DAOLogin import DAOlogin
from Controller.ControllerMensagem import SistemaMensagem
from Controller.ControllerMenu import SistemaMenu

## Classe principal ##
class SistemaLogin(QMainWindow):

    ## Chama a tela ##
    def Iniciar(self):
        self.login.Show()

    ## Verifica os dados preenchidos e chama consulta no banco ##
    def Validar(self):
        user,senha = self.login.Dados()
        VeriUser = self.daolog.CheckUser(user)
        if user != '':
            if VeriUser != [] and VeriUser[0][0] == user.upper():
                if VeriUser[0][1] == 1:
                    VeriSenha = self.daolog.CheckSenha(senha)
                    if VeriSenha != [] and VeriSenha[0][0] == senha:
                        Permi = self.daolog.CheckPermi(user.upper())
                        self.menu.Show(Permi[0][0])
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

    ## Fecha a tela ##
    def Close(self):
        self.login.Close()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.login = viewLogin()
        self.daolog = DAOlogin()
        self.msg = SistemaMensagem()
        self.menu = SistemaMenu()
        #Definição dos botões
        self.login.tela.BT_Logar.clicked.connect(self.Validar)
        self.login.tela.BT_Cancelar.clicked.connect(self.Close)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    self = SistemaLogin()
    self.Iniciar()
    sys.exit(app.exec())