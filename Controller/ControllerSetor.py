from View.ViewSetor import viewSetor
from Controller.ControllerCadastroSetor import SistemaCSetor
from DAO.DAOSetor import DAOsetor
from Model.ModelSetor import ModelSetor
from Controller.ControllerMensagem import SistemaMensagem

class SistemaSetor():

    def Show(self):
        self.viewSetor.Show()
        self.Tabela()

    def Close(self):
        self.viewSetor.Close()

    def PesquisarCadastro(self):
        print()

    def Criar(self):
        self.CSetor.Show('Criar',self)

    def AlterarCadastro(self):
        linhaSelect = self.viewSetor.LinhaSelect()
        if linhaSelect != -1:
            TextoLinha = self.viewSetor.TextoSelectLinha(linhaSelect)
            DadosUser = self.banco.LocalizarSetor(TextoLinha)
            self.CSetor.Show('Alterar', self)
            self.CSetor.MostrarDados(DadosUser)
        else:
            self.msg.MsgSelecionarLinha()

    def Tabela(self):
        lista = self.banco.TodaLista()
        self.model.Tabela(self.viewSetor,lista)

    def ExcluirSetor(self):
        linhaSelect = self.viewSetor.LinhaSelect()
        if linhaSelect != -1:
            TextoLinha = self.viewSetor.TextoSelectLinha(linhaSelect)
            self.banco.ExcluirSetor(TextoLinha)
            self.Tabela()
        else:
            self.msg.MsgSelecionarLinha()

    def __init__(self):
        self.viewSetor = viewSetor()
        self.CSetor = SistemaCSetor()
        self.model = ModelSetor()
        self.banco = DAOsetor()
        self.msg = SistemaMensagem()
        self.viewSetor.tela.BT_Voltar.clicked.connect(self.Close)
        self.viewSetor.tela.BT_Pesquisar.clicked.connect(self.PesquisarCadastro)
        self.viewSetor.tela.BT_Criar.clicked.connect(self.Criar)
        self.viewSetor.tela.BT_Alterar.clicked.connect(self.AlterarCadastro)
        self.viewSetor.tela.BT_Exclui.clicked.connect(self.ExcluirSetor)