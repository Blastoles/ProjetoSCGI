from View.ViewCadastroSetor import viewCadastroSetor
from DAO.DAOCadastroSetor import DAOCadastrarSetor
from Model.ModelCadastroSetor import modelCadastroSetor

class SistemaCSetor():

    def Show(self,opcao,setor):
        self.viewCSetor.LimpeTela()
        self.setor = setor
        self.opcao = opcao
        self.viewCSetor.Show()

    def Close(self):
        self.viewCSetor.Close()

    def InsertSetor(self):
        dados = self.viewCSetor.ColetarDados()
        linhadb = self.DAOSetor.ContLista()
        dados[3] = self.ModelSetor.PrioridadeInt(dados[3])
        self.DAOSetor.InserirDados(dados,linhadb)
        self.setor.Tabela()

    def MostrarDados(self):
        print()

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
        self.setor = ''
        self.viewCSetor.tela.BT_Cancelar.clicked.connect(self.Close)
        self.viewCSetor.tela.BT_Salvar.clicked.connect(self.Opcao)