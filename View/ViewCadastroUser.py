from PyQt5 import uic, QtWidgets


class viewCadastroUser():
    def Show(self):
        self.tela.show()

    def Close(self):
        self.tela.close()

    def LimparDados(self):
        self.tela.CP_Nome.setText("")
        self.tela.CP_Email.setText("")
        self.tela.CP_Telefone.setText("")
        self.tela.CP_Usuario.setText("")
        self.tela.CP_Senha.setText("")
        self.tela.CP_Administrador.setCheckState(0)
        self.tela.CP_Ativo.setCheckState(-1)


    def __init__(self):
        self.tela = uic.loadUi(".\View\Telas\CadastroUsuario.ui")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    CadastroUser = viewCadastroUser()

    # Show das telas
    CadastroUser.tela.show()
    sys.exit(app.exec())
