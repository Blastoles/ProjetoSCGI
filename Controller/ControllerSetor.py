## Bibliotecas ##
from PyQt5.QtWidgets import QMainWindow
from View.ViewSetor import viewSetor
from Controller.ControllerCadastroSetor import SistemaCSetor
from DAO.DAOSetor import DAOsetor
from Model.ModelSetor import ModelSetor
from Controller.ControllerMensagem import SistemaMensagem
from Controller.ControllerConfirmacao import SistemaConfirmacao

## Classe principal ##
class SistemaSetor(QMainWindow):

    ## Chama a tela ##
    def Show(self):
        self.viewSetor.Show()
        self.Tabela()

    ## Fecha a tela ##
    def Close(self):
        self.viewSetor.Close()

    ## Busca dados da tela e busca resultado no banco ##
    def PesquisarCadastro(self):
        texto = self.viewSetor.Dados()
        lista = self.banco.Pesquisa(texto)
        self.model.Tabela(self.viewSetor,lista)

    ## Chama tela de criação ##
    def Criar(self):
        self.CSetor.Show('Criar',self)

    ## Chama tela de alterar cadastro pré-selecionado  ##
    def AlterarCadastro(self):
        linhaSelect = self.viewSetor.LinhaSelect()
        if linhaSelect != -1:
            TextoLinha = self.viewSetor.TextoSelectLinha(linhaSelect)
            DadosUser = self.banco.LocalizarSetor(TextoLinha)
            self.CSetor.Show('Alterar', self)
            self.CSetor.MostrarDados(DadosUser)
        else:
            self.msg.MsgSelecionarLinha()

    ## Chama os dados do banco e mostra na tela ##
    def Tabela(self):
        lista = self.banco.TodaLista()
        self.model.Tabela(self.viewSetor,lista)

    ## Chama tela de confirmação de ação de excluir registro pré-selecionado ##
    def ExcluirSetor(self):
        linhaSelect = self.viewSetor.LinhaSelect()
        if linhaSelect != -1:
            self.conf.Show(self,linhaSelect)
        else:
            self.msg.MsgSelecionarLinha()

    ## Chama exclusão no banco de dados do registro ##
    def ExcluirConfirmado(self,linhaSelect):
        TextoLinha = self.viewSetor.TextoSelectLinha(linhaSelect)
        self.banco.ExcluirSetor(TextoLinha)
        self.Tabela()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.viewSetor = viewSetor()
        self.CSetor = SistemaCSetor()
        self.model = ModelSetor()
        self.banco = DAOsetor()
        self.msg = SistemaMensagem()
        self.conf = SistemaConfirmacao()
        #Definição dos botões
        self.viewSetor.tela.BT_Voltar.clicked.connect(self.Close)
        self.viewSetor.tela.BT_Pesquisar.clicked.connect(self.PesquisarCadastro)
        self.viewSetor.tela.BT_Criar.clicked.connect(self.Criar)
        self.viewSetor.tela.BT_Alterar.clicked.connect(self.AlterarCadastro)
        self.viewSetor.tela.BT_Exclui.clicked.connect(self.ExcluirSetor)