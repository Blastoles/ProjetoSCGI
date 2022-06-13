from PyQt5.QtWidgets import QMainWindow

from Controller.ControllerCadastroContagem import SistemaCContagem
from Controller.ControllerConfirmacao import SistemaConfirmacao
from Controller.ControllerMensagem import SistemaMensagem
from Model.ModelContagemImpressora import ModelContagemImpressora
from View.ViewContagemImpressora import viewContagem
from DAO.DAOContagemImpressora import DAOContagemimpressora

class SistemaContagem(QMainWindow):
    def Show(self):
        self.contagem.LimparTela()
        self.Lista()
        self.contagem.Show()

    def Close(self):
        self.contagem.Close()

    def Criar(self):
        self.Ccontagem.Show('Criar')

    def Alterar(self):
        linhaSelect = self.contagem.LinhaSelect()
        if linhaSelect != -1:
            TextoLinha = self.contagem.TextoSelectLinha(linhaSelect)
            Dados = self.banco.Localizar(TextoLinha)
            self.Ccontagem.Show('Alterar')
            self.Ccontagem.ColoqueDados(Dados)
        else:
            self.msg.MsgSelecionarLinha()

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

    def ExcluirContagem(self):
        linhaSelect = self.contagem.LinhaSelect()
        if linhaSelect != -1:
            self.conf.Show(self,linhaSelect)
        else:
            self.msg.MsgSelecionarLinha()

    def ExcluirConfirmado(self,linhaSelect):
        TextoLinha = self.contagem.TextoSelectLinha(linhaSelect)
        Dados = self.banco.Localizar(TextoLinha)
        self.banco.ExcluirContagem(Dados)
        self.Pesquisa()


    def __init__(self):
        super().__init__()
        self.contagem = viewContagem()
        self.Ccontagem = SistemaCContagem()
        self.banco = DAOContagemimpressora()
        self.model = ModelContagemImpressora()
        self.msg = SistemaMensagem()
        self.conf = SistemaConfirmacao()
        self.contagem.tela.BT_Voltar.clicked.connect(self.Close)
        self.contagem.tela.BT_Criar.clicked.connect(self.Criar)
        self.contagem.tela.BT_Selecionar.clicked.connect(self.Pesquisa)
        self.contagem.tela.BT_Alterar.clicked.connect(self.Alterar)
        self.contagem.tela.BT_Exclui.clicked.connect(self.ExcluirContagem)