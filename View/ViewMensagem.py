from PyQt5 import uic, QtWidgets
from functools import partial

class viewMensagem():
    def __init__(self):
        self.tela = uic.loadUi(".\View\Telas\mensagem.ui")
        self.Mensagem.BT_OK.clicked.connect(partial(self.MenClose))

    def MenShow(self,texto):
        self.Mensagem.TX_Atencao.setText(texto)
        self.Mensagem.show()

    def MenClose(self):
        self.Mensagem.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    mensagem = viewMensagem()

    # Show das telas
    mensagem.tela.show()
    sys.exit(app.exec())
