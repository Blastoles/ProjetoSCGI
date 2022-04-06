from PyQt5 import uic, QtWidgets


class viewCadastroUser():
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
