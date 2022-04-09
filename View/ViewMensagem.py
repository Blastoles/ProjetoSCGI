from PyQt5 import uic, QtWidgets

class viewMensagem():
    def __init__(self):
        self.tela = uic.loadUi(".\View\Telas\mensagem.ui")

    def MsgShow(self):
        self.tela.show()

    def MenClose(self):
        self.tela.close()

    def MsgErroLogin(self):
        self.tela.TX_Atencao.setText("Usuário ou Senha invalido(s)\nTente novamente!!")

    def MsgFaltaDados(self):
        self.tela.TX_Atencao.setText("Falta informações\nFavor Insira todas as informações")

    def MsgErroBando(self):
        self.tela.TX_Atencao.setText("Ocorreu um erro com o Banco de Dados!!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    mensagem = viewMensagem()

    # Show das telas
    mensagem.tela.show()
    sys.exit(app.exec())
