from Controller.ControllerCadastroManutencao import SistemaCManutencao
from DAO.DAOManutencao import DAOManutencao
from Model.ModelManutencao import ModelManutencao
from View.ViewManutencao import viewManutencao
from Controller.ControllerConfirmacao import SistemaConfirmacao
from Controller.ControllerMensagem import SistemaMensagem

class SistemaManutencao():

    def Show(self):
        self.viewManu.LimparTela()
        self.Lista()
        self.viewManu.Show()

    def Close(self):
        self.viewManu.Close()

    def Criar(self):
        self.CManu.Show('Criar')

    def Alterar(self):
        linhaSelect = self.viewManu.LinhaSelect()
        if linhaSelect != -1:
            TextoLinha = self.viewManu.TextoSelectLinha(linhaSelect)
            Dados = self.banco.Localizar(TextoLinha)
            self.CManu.Show('Alterar')
            self.CManu.ColoqueDados(Dados)
        else:
            self.msg.MsgSelecionarLinha()

    def Pesquisa(self):
        ImprSelect = self.viewManu.ImprSelect()
        if ImprSelect != 'Selecione a Impressora' and ImprSelect != 'Número de Serie -- Modelo -- Setor -- Sigla do Setor':
            ImprSelect = ImprSelect.split(' -- ')
            Impre = self.banco.Pesquisa(ImprSelect[0])
            self.model.Tabela(self.viewManu,Impre)
        else:
            self.msg.MsgSelecionarImpr()

    def Lista(self):
        lista = self.banco.Lista()
        lista = self.model.TratarLista(lista)
        self.viewManu.SetImpressora(lista)

    def __init__(self):
        self.viewManu = viewManutencao()
        self.msg = SistemaMensagem()
        self.CManu = SistemaCManutencao()
        self.banco = DAOManutencao()
        self.model = ModelManutencao()
        self.viewManu.tela.BT_Voltar.clicked.connect(self.Close)
        self.viewManu.tela.BT_Criar.clicked.connect(self.Criar)
        self.viewManu.tela.BT_Selecionar.clicked.connect(self.Pesquisa)
        """
        
        self.viewManu.tela.BT_Exclui.clicked.connect(self.Close)
        self.viewManu.tela.BT_Alterar.clicked.connect(self.Close)
        
        
        def Alterar(self):
            linhaSelect = self.viewManu.LinhaSelect()
            if linhaSelect != -1:
                TextoLinha = self.viewManu.TextoSelectLinha(linhaSelect)
                Dados = self.banco.Localizar(TextoLinha)
                self.CManu.Show('Alterar')
                self.CManu.ColoqueDados(Dados)
            else:
                self.msg.MsgSelecionarLinha()





    def ExcluirManutencao(self):
        linhaSelect = self.viewManu.LinhaSelect()
        if linhaSelect != -1:
            self.conf.Show(self,linhaSelect)
        else:
            self.msg.MsgSelecionarLinha()

    def ExcluirConfirmado(self,linhaSelect):
        TextoLinha = self.viewManu.TextoSelectLinha(linhaSelect)
        Dados = self.banco.Localizar(TextoLinha)
        self.banco.ExcluirContagem(Dados)
        self.Pesquisa()
        """