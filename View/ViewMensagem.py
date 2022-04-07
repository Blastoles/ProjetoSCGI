from PyQt5 import uic, QtWidgets
from functools import partial

class viewMensagem():
    def __init__(self):
        self.tela = uic.loadUi(".\View\Telas\mensagem.ui")

    def MsgShow(self):
        self.tela.show()

    def MenClose(self):
        self.tela.close()

    def MsgErroLogin(self):
        self.tela.TX_Atencao.setText("Usuário ou Senha invalido(s)\nTente novamente!!")
        self.MsgShow()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    mensagem = viewMensagem()

    # Show das telas
    mensagem.tela.show()
    sys.exit(app.exec())
