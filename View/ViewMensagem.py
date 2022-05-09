from PyQt5 import uic, QtWidgets
from os import getcwd

class viewMensagem():
    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\mensagem.ui".format(Local))

    def MsgShow(self):
        self.tela.show()

    def MsgClose(self):
        self.tela.close()

    def MsgErroLogin(self):
        self.tela.TX_Atencao.setText("Usuário ou Senha invalido(s)\nTente novamente!!")

    def MsgFaltaDados(self,falta):
        self.tela.TX_Atencao.setText("Está faltando informações no campo(s)!\n\n{}{}{}".format(falta[0],falta[1],falta[2]))

    def MsgRealizadoComSucesso(self):
        self.tela.TX_Atencao.setText("Realizado com sucesso!!")

    def MsgUserAtivo(self):
        self.tela.TX_Atencao.setText("Usuário Desativado!!")

    def MsgUserCadastrado(self):
        self.tela.TX_Atencao.setText("Já existe um usuário cadastrado com esse usuário!!")

    def MsgErroBando(self):
        self.tela.TX_Atencao.setText("Ocorreu um erro com o Banco de Dados!!")

    def MsgSelecionarImpr(self):
        self.tela.TX_Atencao.setText("Selecione uma impressora valida!!")

    def MsgSelecionarLinha(self):
        self.tela.TX_Atencao.setText("Selecione uma linha da tabela de Usuários!!")

    def MsgSetorJaCadastrado(self):
        self.tela.TX_Atencao.setText("Já existe um setor com essa 'SIGLA'!!")

    def MsgImprJaCadastrado(self):
        self.tela.TX_Atencao.setText("Já existe uma Impressora com esse 'Número de Série'!!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    mensagem = viewMensagem()

    # Show das telas
    mensagem.tela.show()
    sys.exit(app.exec())
