from PyQt5 import uic, QtWidgets


class viewUser():
    def __init__(self):
        self.tela = uic.loadUi(".\View\Telas\CD_Usuario.ui")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    User = viewUser()

    # Show das telas
    User.tela.show()
    sys.exit(app.exec())
