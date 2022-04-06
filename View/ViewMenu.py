from PyQt5 import uic, QtWidgets


class ViewMenu():
    def __init__(self):
        self.tela = uic.loadUi(".\Telas\Home.ui")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    menu = ViewMenu()

    # Show das telas
    menu.tela.show()
    sys.exit(app.exec())
