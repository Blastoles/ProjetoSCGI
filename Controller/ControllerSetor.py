from View.ViewSetor import viewSetor
from Controller.ControllerCadastroSetor import SistemaCSetor
from DAO.DAOSetor import DAOsetor
from Model.ModelSetor import ModelSetor

class SistemaSetor():

    def Show(self):
        self.viewSetor.Show()
        self.Tabela()

    def Close(self):
        self.viewSetor.Close()

    def PesquisarCadastro(self):
        print()

    def Criar(self):
        self.CSetor.Show('Criar')

    def AlterarCadastro(self):
        self.CSetor.Show('Alterar')

    def Tabela(self):
        lista = self.banco.TodaLista()
        print(lista)
        self.model.Tabela(self.viewSetor,lista)

    def ExcluirUser(self):
        print()

    def __init__(self):
        self.viewSetor = viewSetor()
        self.CSetor = SistemaCSetor()
        self.model = ModelSetor()
        self.banco = DAOsetor()
        self.viewSetor.tela.BT_Voltar.clicked.connect(self.Close)
        self.viewSetor.tela.BT_Pesquisar.clicked.connect(self.PesquisarCadastro)
        self.viewSetor.tela.BT_Criar.clicked.connect(self.Criar)
        self.viewSetor.tela.BT_Alterar.clicked.connect(self.AlterarCadastro)
        self.viewSetor.tela.BT_Exclui.clicked.connect(self.ExcluirUser)