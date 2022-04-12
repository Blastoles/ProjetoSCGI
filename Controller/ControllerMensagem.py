from PyQt5 import uic, QtWidgets
from functools import partial
from View.ViewMensagem import viewMensagem


class SistemaMensagem():

    def MsgErroLogin(self):
        self.msg.MsgErroLogin()
        self.msg.MsgShow()

    def MsgFaltaDados(self):
        self.msg.MsgFaltaDados()
        self.msg.MsgShow()

    def MsgErroBancoDados(self):
        self.msg.MsgErroBando()
        self.msg.MsgShow()

    def MsgUserJaCadastrado(self):
        self.msg.MsgUserCadastrado()
        self.msg.MsgShow()

    def __init__(self):
        self.msg = viewMensagem()
        self.msg.tela.BT_OK.clicked.connect(partial(self.msg.MenClose))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sistema = SistemaMensagem()

    sistema.Iniciar()

    sys.exit(app.exec())