from PyQt5 import uic, QtWidgets


class ViewUser():
    def __init__(self):
        self.tela = uic.loadUi(".\Telas\CD_Usuario.ui")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    User = ViewUser()

    # Show das telas
    User.tela.show()
    sys.exit(app.exec())
