from PyQt5 import uic, QtWidgets


class ViewCadastroUser():
    def __init__(self):
        self.tela = uic.loadUi(".\Telas\CadastroUsuario.ui")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    CadastroUser = ViewCadastroUser()

    # Show das telas
    CadastroUser.tela.show()
    sys.exit(app.exec())
