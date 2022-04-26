from PyQt5 import uic, QtWidgets
from Controller.ControllerConfirmacao import SistemaConfirmacao
from View.ViewUser import viewUser
from DAO.DAOUser import DAOuser
from Model.ModelUser import Modeluser
from Controller.ControllerCadastroUser import SistemaCadastroUser
from Controller.ControllerMensagem import SistemaMensagem

class SistemaUser():
    def Show(self):
        self.user.Show()
        self.Tabela()

    def Tabela(self):
        lista = self.banco.TodaLista()
        self.model.Tabela(self.user,lista)

    def Close(self):
        self.user.Close()


    def PesquisarCadastro(self):
        texto = self.user.Dados()
        lista = self.banco.Pesquisa(texto)
        self.model.Tabela(self.user,lista)

    def Criar(self):
        self.cduser.Show('Incluir',self)

    def AlterarCadastro(self):
        linhaSelect = self.user.LinhaSelect()
        if linhaSelect != -1:
            TextoLinha = self.user.TextoSelectLinha(linhaSelect)
            DadosUser = self.banco.LocalizarUser(TextoLinha)
            self.cduser.Show('Alterar', self)
            self.cduser.MostrarDados(DadosUser)
        else:
            self.msg.MsgSelecionarLinha()

    def ExcluirUser(self):
        linhaSelect = self.user.LinhaSelect()
        if linhaSelect != -1:
            self.conf.Show(self, linhaSelect)
        else:
            self.msg.MsgSelecionarLinha()

    def ExcluirConfirmado(self,LinhaSelect):
        TextoLinha = self.user.TextoSelectLinha(LinhaSelect)
        self.banco.ExcluirUser(TextoLinha)
        self.Tabela()

    def __init__(self):
        self.user = viewUser()
        self.banco = DAOuser()
        self.model = Modeluser()
        self.cduser = SistemaCadastroUser()
        self.msg = SistemaMensagem()
        self.conf = SistemaConfirmacao()
        self.user.tela.BT_Voltar.clicked.connect(self.Close)
        self.user.tela.BT_Pesquisar.clicked.connect(self.PesquisarCadastro)
        self.user.tela.BT_Criar.clicked.connect(self.Criar)
        self.user.tela.BT_Alterar.clicked.connect(self.AlterarCadastro)
        self.user.tela.BT_Exclui.clicked.connect(self.ExcluirUser)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    menu = ()

    # Show das telas
    menu.tela.show()
    sys.exit(app.exec())
