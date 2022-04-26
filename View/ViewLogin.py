from PyQt5 import uic, QtWidgets
from os import getcwd

class viewLogin():
    def Show(self):
        self.tela.show()

    def Close(self):
        self.tela.close()

    def Dados(self):
        usuario = self.tela.CP_Login.text()
        senha = self.tela.CP_Senha.text()
        return usuario,senha

    def MensagemErro(self):
        self.tela.Tx_Status.setText("Usuário ou Senha invalido(s)!!")

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\Login.ui".format(Local))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    login = viewLogin()

    # Show das telas
    login.tela.show()
    sys.exit(app.exec())
