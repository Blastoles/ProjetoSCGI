## Bibliotecas ##
from PyQt5.QtWidgets import QMainWindow
from Controller.ControllerConfirmacao import SistemaConfirmacao
from Model.ModelImpressora import ModelImpressora
from View.ViewImpressora import viewImpressora
from DAO.DAOImpressora import DAOimpressora
from Controller.ControllerMensagem import SistemaMensagem
from Controller.ControllerCadastroImpressora import SistemaCadastroImpressora

## Classe principal ##
class SistemaImpressora(QMainWindow):

    ## Chama a tela ##
    def Show(self):
        self.impressora.Show()
        self.Tabela()

    ## Fecha a tela ##
    def Close(self):
        self.impressora.Close()

    ## Chama os dados do banco e mostra na tela ##
    def Tabela(self):
        lista = self.banco.TodaLista()
        self.model.Tabela(self.impressora,lista)

    ## Busca dados da tela e busca resultado no banco ##
    def PesquisarImpressora(self):
        texto = self.impressora.Dados()
        lista = self.banco.Pesquisa(texto)
        self.model.Tabela(self.impressora, lista)

    ## Chama tela de criação ##
    def Criar(self):
        self.cdimpressora.Show('Incluir',self)

    ## Chama tela de alterar cadastro pré-selecionado  ##
    def AlterarImpressora(self):
        linhaSelect = self.impressora.LinhaSelect()
        if linhaSelect != -1:
            TextoLinha = self.impressora.TextoSelectLinha(linhaSelect)
            DadosUser = self.banco.LocalizarImp(TextoLinha)
            self.cdimpressora.Show('Alterar', self)
            self.cdimpressora.MostrarDados(DadosUser)
        else:
            self.msg.MsgSelecionarLinha()

    ## Chama tela de confirmação de ação de excluir registro pré-selecionado ##
    def ExcluirImpressora(self):
        linhaSelect = self.impressora.LinhaSelect()
        if linhaSelect != -1:
            self.conf.Show(self, linhaSelect)
        else:
            self.msg.MsgSelecionarLinha()

    ## Chama exclusão no banco de dados do registro ##
    def ExcluirConfirmado(self,linhaSelect):
        TextoLinha = self.impressora.TextoSelectLinha(linhaSelect)
        self.banco.ExcluirImpr(TextoLinha)
        self.Tabela()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.impressora = viewImpressora()
        self.msg = SistemaMensagem()
        self.banco = DAOimpressora()
        self.cdimpressora = SistemaCadastroImpressora()
        self.model = ModelImpressora()
        self.conf = SistemaConfirmacao()
        #Definição dos botões
        self.impressora.tela.BT_Voltar.clicked.connect(self.Close)
        self.impressora.tela.BT_Pesquisar.clicked.connect(self.PesquisarImpressora)
        self.impressora.tela.BT_Criar.clicked.connect(self.Criar)
        self.impressora.tela.BT_Alterar.clicked.connect(self.AlterarImpressora)
        self.impressora.tela.BT_Exclui.clicked.connect(self.ExcluirImpressora)
