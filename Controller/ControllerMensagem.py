from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from View.ViewMensagem import viewMensagem

class SistemaMensagem(QMainWindow):

    def MsgErroLogin(self):
        self.msg.MsgErroLogin()
        self.MsgShow()

    def MsgFaltaDados(self,falta):
        self.msg.MsgFaltaDados(falta)
        self.MsgShow()

    def MsgUserAtivo(self):
        self.msg.MsgUserAtivo()
        self.MsgShow()

    def MsgErroBancoDados(self):
        self.msg.MsgErroBando()
        self.MsgShow()

    def MsgUserJaCadastrado(self):
        self.msg.MsgUserCadastrado()
        self.MsgShow()

    def MsgSelecionarImpr(self):
        self.msg.MsgSelecionarImpr()
        self.MsgShow()

    def MsgSelecionarLinha(self):
        self.msg.MsgSelecionarLinha()
        self.MsgShow()

    def MsgRealizadoComSucesso(self):
        self.msg.MsgRealizadoComSucesso()
        self.MsgShow()

    def MsgSetorJaCadastrado(self):
        self.msg.MsgSetorJaCadastrado()
        self.MsgShow()

    def MsgImprJaCadastrado(self):
        self.msg.MsgImprJaCadastrado()
        self.MsgShow()

    def MsgClose(self):
        self.msg.MsgClose()

    def MsgShow(self):
        self.msg.MsgShow()

    def __init__(self):
        super().__init__()
        self.msg = viewMensagem()
        self.msg.tela.BT_OK.clicked.connect(self.MsgClose)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sistema = SistemaMensagem()

    sistema.Iniciar()

    sys.exit(app.exec())