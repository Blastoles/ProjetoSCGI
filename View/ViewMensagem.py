from PyQt5 import uic, QtWidgets


class viewMensagem():
    def __init__(self):
        self.tela = uic.loadUi(".\View\Telas\mensagem.ui")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    mensagem = viewMensagem()

    # Show das telas
    mensagem.tela.show()
    sys.exit(app.exec())
