from PyQt5 import uic, QtWidgets

class ViewLogin():
    def __init__(self):
        self.tela = uic.loadUi(".\Telas\Login.ui")

    def Show(self):
        self.tela.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    login = ViewLogin()

    # Show das telas
    login.tela.show()
    sys.exit(app.exec())
