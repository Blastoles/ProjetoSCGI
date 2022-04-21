from View.ViewSetor import viewSetor
from Controller.ControllerCadastroSetor import SistemaCSetor

class SistemaSetor():

    def Show(self):
        self.viewSetor.Show()

    def Close(self):
        self.viewSetor.Close()

    def PesquisarCadastro(self):
        print()

    def Criar(self):
        self.CSetor.Show()

    def AlterarCadastro(self):
        print()

    def ExcluirUser(self):
        print()

    def __init__(self):
        self.viewSetor = viewSetor()
        self.CSetor = SistemaCSetor()
        self.viewSetor.tela.BT_Voltar.clicked.connect(self.Close)
        self.viewSetor.tela.BT_Pesquisar.clicked.connect(self.PesquisarCadastro)
        self.viewSetor.tela.BT_Criar.clicked.connect(self.Criar)
        self.viewSetor.tela.BT_Alterar.clicked.connect(self.AlterarCadastro)
        self.viewSetor.tela.BT_Exclui.clicked.connect(self.ExcluirUser)