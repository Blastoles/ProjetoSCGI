from PyQt5 import uic, QtWidgets


class ViewMensagem():
    def __init__(self):
        self.tela = uic.loadUi(".\Telas\mensagem.ui")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    mensagem = ViewMensagem()

    # Show das telas
    mensagem.tela.show()
    sys.exit(app.exec())
