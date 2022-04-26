from PyQt5 import uic, QtWidgets
from os import getcwd

class viewMenu():
    def Show(self):
        self.tela.show()

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\Home.ui".format(Local))
        #self.tela = uic.loadUi(".\View\Telas\Home.ui")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    menu = viewMenu()

    # Show das telas
    menu.tela.show()
    sys.exit(app.exec())
