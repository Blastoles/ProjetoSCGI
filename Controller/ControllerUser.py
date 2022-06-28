## Bibliotecas ##
from PyQt5.QtWidgets import QMainWindow
from Controller.ControllerConfirmacao import SistemaConfirmacao
from View.ViewUser import viewUser
from DAO.DAOUser import DAOuser
from Model.ModelUser import Modeluser
from Controller.ControllerCadastroUser import SistemaCadastroUser
from Controller.ControllerMensagem import SistemaMensagem

## Classe principal ##
class SistemaUser(QMainWindow):

    ## Chama tela ##
    def Show(self):
        self.user.Show()
        self.Tabela()

    ## Chama os dados do banco e mostra na tela ##
    def Tabela(self):
        lista = self.banco.TodaLista()
        self.model.Tabela(self.user,lista)

    ## Fecha tela ##
    def Close(self):
        self.user.Close()

    ## Busca dados da tela e busca resultado no banco ##
    def PesquisarCadastro(self):
        texto = self.user.Dados()
        lista = self.banco.Pesquisa(texto)
        self.model.Tabela(self.user,lista)

    ## Chama tela de criação ##
    def Criar(self):
        self.cduser.Show('Incluir',self)

    ## Chama tela de alterar cadastro pré-selecionado  ##
    def AlterarCadastro(self):
        linhaSelect = self.user.LinhaSelect()
        if linhaSelect != -1:
            TextoLinha = self.user.TextoSelectLinha(linhaSelect)
            DadosUser = self.banco.LocalizarUser(TextoLinha)
            self.cduser.Show('Alterar', self)
            self.cduser.MostrarDados(DadosUser)
        else:
            self.msg.MsgSelecionarLinha()

    ## Chama tela de confirmação de ação de excluir registro pré-selecionado ##
    def ExcluirUser(self):
        linhaSelect = self.user.LinhaSelect()
        if linhaSelect != -1:
            self.conf.Show(self, linhaSelect)
        else:
            self.msg.MsgSelecionarLinha()

    ## Chama exclusão no banco de dados do registro ##
    def ExcluirConfirmado(self,LinhaSelect):
        TextoLinha = self.user.TextoSelectLinha(LinhaSelect)
        self.banco.ExcluirUser(TextoLinha)
        self.Tabela()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.user = viewUser()
        self.banco = DAOuser()
        self.model = Modeluser()
        self.cduser = SistemaCadastroUser()
        self.msg = SistemaMensagem()
        self.conf = SistemaConfirmacao()
        #Definição dos botões
        self.user.tela.BT_Voltar.clicked.connect(self.Close)
        self.user.tela.BT_Pesquisar.clicked.connect(self.PesquisarCadastro)
        self.user.tela.BT_Criar.clicked.connect(self.Criar)
        self.user.tela.BT_Alterar.clicked.connect(self.AlterarCadastro)
        self.user.tela.BT_Exclui.clicked.connect(self.ExcluirUser)
