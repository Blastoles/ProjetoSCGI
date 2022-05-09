from Controller.ControllerCadastroContagem import SistemaCContagem
from Controller.ControllerMensagem import SistemaMensagem
from Model.ModelContagemImpressora import ModelContagemImpressora
from View.ViewContagemImpressora import viewContagem
from DAO.DAOContagemImpressora import DAOContagemimpressora

class SistemaContagem():
    def Show(self):
        self.contagem.LimparTela()
        self.Lista()
        self.contagem.Show()

    def Close(self):
        self.contagem.Close()

    def Criar(self):
        self.Ccontagem.Show('Criar')

    def Alterar(self):
        self.Ccontagem.Show('Alterar')

    def Lista(self):
        lista = self.banco.Lista()
        lista = self.model.TratarLista(lista)
        self.contagem.SetImpressora(lista)

    def Pesquisa(self):
        ImprSelect = self.contagem.ImprSelect()
        if ImprSelect != 'Selecione a Impressora' and ImprSelect != 'Número de Serie -- Modelo -- Setor -- Sigla do Setor':
            ImprSelect = ImprSelect.split(' -- ')
            Impre = self.banco.Pesquisa(ImprSelect[0])
            self.model.Tabela(self.contagem,Impre)
        else:
            self.msg.MsgSelecionarImpr()


    def __init__(self):
        self.contagem = viewContagem()
        self.Ccontagem = SistemaCContagem()
        self.banco = DAOContagemimpressora()
        self.model = ModelContagemImpressora()
        self.msg = SistemaMensagem()
        self.contagem.tela.BT_Voltar.clicked.connect(self.Close)
        self.contagem.tela.BT_Criar.clicked.connect(self.Criar)
        self.contagem.tela.BT_Selecionar.clicked.connect(self.Pesquisa)
        #self.contagem.tela.BT_Pesquisar.clicked.connect(self.PesquisarCadastro)
        #self.contagem.tela.BT_Alterar.clicked.connect(self.AlterarCadastro)
        #self.contagem.tela.BT_Exclui.clicked.connect(self.ExcluirSetor)
"""
    def PesquisarCadastro(self):
        texto = self.viewSetor.Dados()
        lista = self.banco.Pesquisa(texto)
        self.model.Tabela(self.viewSetor,lista)


    def AlterarCadastro(self):
        linhaSelect = self.viewSetor.LinhaSelect()
        if linhaSelect != -1:
            TextoLinha = self.viewSetor.TextoSelectLinha(linhaSelect)
            DadosUser = self.banco.LocalizarSetor(TextoLinha)
            self.CSetor.Show('Alterar', self)
            self.CSetor.MostrarDados(DadosUser)
        else:
            self.msg.MsgSelecionarLinha()

    def Tabela(self):
        lista = self.banco.TodaLista()
        self.model.Tabela(self.viewSetor,lista)

    def ExcluirSetor(self):
        linhaSelect = self.viewSetor.LinhaSelect()
        if linhaSelect != -1:
            self.conf.Show(self,linhaSelect)
        else:
            self.msg.MsgSelecionarLinha()

    def ExcluirConfirmado(self,linhaSelect):
        TextoLinha = self.viewSetor.TextoSelectLinha(linhaSelect)
        self.banco.ExcluirSetor(TextoLinha)
        self.Tabela()
"""
