## Bibliotecas ##
from PyQt5.QtWidgets import QMainWindow
from Controller.ControllerCadastroManutencao import SistemaCManutencao
from DAO.DAOManutencao import DAOManutencao
from Model.ModelManutencao import ModelManutencao
from View.ViewManutencao import viewManutencao
from Controller.ControllerConfirmacao import SistemaConfirmacao
from Controller.ControllerMensagem import SistemaMensagem

## Classe principal ##
class SistemaManutencao(QMainWindow):

    ## Chama a tela ##
    def Show(self):
        self.viewManu.LimparTela()
        self.Lista()
        self.viewManu.Show()

    ## Fecha a tela  ##
    def Close(self):
        self.viewManu.Close()

    ## Chama tela de cadastro ##
    def Criar(self):
        self.CManu.Show('Criar')

    ## Chama tela de alterar cadastro pré-selecionado  ##
    def Alterar(self):
        linhaSelect = self.viewManu.LinhaSelect()
        if linhaSelect != -1:
            TextoLinha = self.viewManu.TextoSelectLinha(linhaSelect)
            Dados = self.banco.Localizar(TextoLinha)
            Dados = self.model.Motivo(Dados)
            self.CManu.Show('Alterar')
            self.CManu.ColoqueDados(Dados)
        else:
            self.msg.MsgSelecionarLinha()

    ## Busca dados da tela e busca resultado no banco ##
    def Pesquisa(self):
        ImprSelect = self.viewManu.ImprSelect()
        if ImprSelect != 'Selecione a Impressora' and ImprSelect != 'Número de Serie -- Modelo -- Setor -- Sigla do Setor':
            ImprSelect = ImprSelect.split(' -- ')
            Impre = self.banco.Pesquisa(ImprSelect[0])
            self.model.Tabela(self.viewManu,Impre)
        else:
            self.msg.MsgSelecionarImpr()

    ## Chama os dados do banco e mostra na tela ##
    def Lista(self):
        lista = self.banco.Lista()
        lista = self.model.TratarLista(lista)
        self.viewManu.SetImpressora(lista)

    ## Chama tela de confirmação de ação de excluir registro pré-selecionado ##
    def ExcluirManutencao(self):
        linhaSelect = self.viewManu.LinhaSelect()
        if linhaSelect != -1:
            self.conf.Show(self,linhaSelect)
        else:
            self.msg.MsgSelecionarLinha()

    ## Chama exclusão no banco de dados do registro ##
    def ExcluirConfirmado(self,linhaSelect):
        TextoLinha = self.viewManu.TextoSelectLinha(linhaSelect)
        Dados = self.banco.Localizar(TextoLinha)
        self.banco.ExcluirManutencao(Dados)
        self.Pesquisa()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.viewManu = viewManutencao()
        self.msg = SistemaMensagem()
        self.CManu = SistemaCManutencao()
        self.banco = DAOManutencao()
        self.model = ModelManutencao()
        self.conf = SistemaConfirmacao()
        #Definição dos botões
        self.viewManu.tela.BT_Voltar.clicked.connect(self.Close)
        self.viewManu.tela.BT_Criar.clicked.connect(self.Criar)
        self.viewManu.tela.BT_Selecionar.clicked.connect(self.Pesquisa)
        self.viewManu.tela.BT_Alterar.clicked.connect(self.Alterar)
        self.viewManu.tela.BT_Exclui.clicked.connect(self.ExcluirManutencao)
