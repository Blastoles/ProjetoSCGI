from View.ViewCadastroSetor import viewCadastroSetor
from DAO.DAOCadastroSetor import DAOCadastrarSetor
from Model.ModelCadastroSetor import modelCadastroSetor

class SistemaCSetor():

    def Show(self,opcao):
        self.viewCSetor.LimpeTela()
        self.opcao = opcao
        self.viewCSetor.Show()

    def Close(self):
        self.viewCSetor.Close()

    def InsertSetor(self):
        dados = self.viewCSetor.ColetarDados()
        linhadb = self.DAOSetor.ContLista()
        dados[3] = self.ModelSetor.PrioridadeInt(dados[3])
        self.DAOSetor.InserirDados(dados,linhadb)

    def AlterarSetor(self):
        print()

    def Opcao(self):
        if self.opcao == 'Criar':
            self.InsertSetor()
        elif self.opcao == 'Alterar':
            self.AlterarSetor()

    def __init__(self):
        self.viewCSetor = viewCadastroSetor()
        self.DAOSetor = DAOCadastrarSetor()
        self.ModelSetor = modelCadastroSetor()
        self.opcao = ''
        self.viewCSetor.tela.BT_Cancelar.clicked.connect(self.Close)
        self.viewCSetor.tela.BT_Salvar.clicked.connect(self.Opcao)