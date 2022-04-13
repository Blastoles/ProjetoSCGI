from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class viewMensagem(QMessageBox):
    def __init__(self):
        self.tela = uic.loadUi(".\View\Telas\mensagem.ui")

    def MsgShow(self):
        self.tela.show()

    def MenClose(self):
        self.tela.close()

    def MsgErroLogin(self):
        self.tela.TX_Atencao.setText("Usuário ou Senha invalido(s)\nTente novamente!!")

    def MsgFaltaDados(self,falta):
        self.tela.TX_Atencao.setText("Está faltando informações no campo(s)!\n\n{}{}{}".format(falta[0],falta[1],falta[2]))

    def MsgUserCadastrado(self):
        self.tela.TX_Atencao.setText("Já existe um usuário cadastrado com esse usuário!!")

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
