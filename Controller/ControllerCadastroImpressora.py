from View.ViewCadastroImpressora import viewCadastroImpressora
from DAO.DAOCadastroImpressora import DAOCadastrarimpressora
from Model.ModelCadastroImpressora import ModelCadastroImpressora

class SistemaCadastroImpressora():

    def Show(self,opcao,Self):
        self.opcao = opcao
        self.imp = Self
        setor = self.banco.ConsultaSetor()
        self.viewcdImp.LimparDados()
        self.viewcdImp.Show(setor)

    def Close(self):
        self.viewcdImp.Close()

    def InsertDados(self):
        lista = self.viewcdImp.ColetaDados()
        print(lista)

    def AlterarDados(self):
        print()




    def Opcao(self):
        if self.opcao == "Incluir":
            self.InsertDados()
        elif self.opcao == "Alterar":
            self.AlterarDados()

    def __init__(self):
        self.viewcdImp = viewCadastroImpressora()
        self.opcao = ''
        self.imp = ''
        self.banco = DAOCadastrarimpressora()
        self.model = ModelCadastroImpressora()
        self.viewcdImp.tela.BT_Cancelar.clicked.connect(self.Close)
        self.viewcdImp.tela.BT_Salvar.clicked.connect(self.Opcao)