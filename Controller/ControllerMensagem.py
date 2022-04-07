from PyQt5 import uic, QtWidgets
from functools import partial
from View.ViewMensagem import viewMensagem


class SistemaMensagem():

    def MsgErroLogin(self):
        self.msg.MsgErroLogin()

    def __init__(self):
        self.msg = viewMensagem()
        self.msg.tela.BT_OK.clicked.connect(partial(self.msg.MenClose))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sistema = SistemaMensagem()

    sistema.Iniciar()

    sys.exit(app.exec())