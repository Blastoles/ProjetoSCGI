from PyQt5 import uic, QtWidgets


class viewMenu():
    def Show(self):
        self.tela.show()

    def __init__(self):
        self.tela = uic.loadUi(".\View\Telas\Home.ui")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    menu = viewMenu()

    # Show das telas
    menu.tela.show()
    sys.exit(app.exec())
