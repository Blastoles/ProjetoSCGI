from PyQt5 import uic, QtWidgets

class viewLogin():
    def __init__(self):
        self.tela = uic.loadUi(".\View\Telas\Login.ui")

    def Show(self):
        self.tela.show()

    def Close(self):
        self.tela.close()

    def Dados(self):
        usuario = self.tela.CP_Login.text()
        senha = self.tela.CP_Senha.text()
        return usuario,senha

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    login = viewLogin()

    # Show das telas
    login.tela.show()
    sys.exit(app.exec())
