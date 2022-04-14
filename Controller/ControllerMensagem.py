from PyQt5 import uic, QtWidgets
from functools import partial

from PyQt5.QtWidgets import QMessageBox

from View.ViewMensagem import viewMensagem


class SistemaMensagem(QMessageBox):

    def MsgErroLogin(self):
        self.msg.MsgErroLogin()
        self.msg.MsgShow()

    def MsgFaltaDados(self,falta):
        self.msg.MsgFaltaDados(falta)
        self.msg.MsgShow()

    def MsgUserAtivo(self):
        self.msg.MsgUserAtivo()
        self.msg.MsgShow()

    def MsgErroBancoDados(self):
        self.msg.MsgErroBando()
        self.msg.MsgShow()

    def MsgUserJaCadastrado(self):
        self.msg.MsgUserCadastrado()
        self.msg.MsgShow()

    def MsgSelecionarLinha(self):
        self.msg.MsgSelecionarLinha()
        self.msg.MsgShow()

    def MsgRealizadoComSucesso(self):
        self.msg.MsgRealizadoComSucesso()
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