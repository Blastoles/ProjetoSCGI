from Controller.ControllerMensagem import SistemaMensagem
from DAO.DAOCadastroContagem import DAOCadastrarContagem
from Model.ModelCadastrarContagem import ModelCadastrarContagem
from View.ViewCadastroContagem import viewCadastroContagem


class SistemaCContagem():

    def Show(self):
        self.viewCContagem.LimpeTela()
        self.viewCContagem.LimpaInfo()
        self.MostreLista()
        self.viewCContagem.Show()

    def Close(self):
        self.viewCContagem.Close()

    def MostreLista(self):
        lista = self.banco.Lista()
        lista = self.model.TratarLista(lista)
        self.viewCContagem.ColocarImpressora(lista)

    def Selecionado(self):
        selec = self.viewCContagem.ImprSelect()
        if selec != 'Selecione a Impressora':
            selec = selec.split(' -- ')
            dados = self.banco.BuscarDados(selec[0])
            self.viewCContagem.ColocarInfo(dados)
        else:
            self.viewCContagem.LimpaInfo()
            self.msg.MsgSelecionarImpr()

    def __init__(self):
        self.viewCContagem = viewCadastroContagem()
        self.msg = SistemaMensagem()
        self.banco = DAOCadastrarContagem()
        self.model = ModelCadastrarContagem()
        #self.opcao = ''
        #self.setor = ''
        self.viewCContagem.tela.BT_Cancelar.clicked.connect(self.Close)
        self.viewCContagem.tela.BT_Selecionar.clicked.connect(self.Selecionado)
        #self.viewCContagem.tela.BT_Salvar.clicked.connect(self.Opcao)
"""        
    def InsertSetor(self):
        dados = self.viewCSetor.ColetarDados()
        if dados[1] != '' and dados[0] != '':
            check = self.DAOSetor.CheckUser(dados[1])
            if check == []:
                linhadb = self.DAOSetor.ContLista()
                dados[3] = self.ModelSetor.PrioridadeInt(dados[3])
                self.DAOSetor.InserirDados(dados,linhadb)
                self.setor.Tabela()
            else:
                self.msg.MsgSetorJaCadastrado()
        else:
            falta = ['','','']
            if dados[0] == '':
                falta[0] = 'Nome\n'
            if dados[1] == '':
                falta[1] = 'Sigla\n'
            self.msg.MsgFaltaDados(falta)

    def MostrarDados(self,TextoLinha):
        self.viewCSetor.ColocarDados(TextoLinha)


    def AlterarSetor(self):
        dados = self.viewCSetor.ColetarDados()
        if dados[3] == 'Normal':
            dados[3] = 0
        elif dados[3] == 'Baixa':
            dados[3] = 1
        elif dados[3] == 'Alta':
            dados[3] = 2
        elif dados[3] == 'Urgente':
            dados[3] = 3
        else:
            dados[3] = -1
        self.DAOSetor.UpdateDados(dados)
        self.setor.Tabela()

    def Opcao(self):
        if self.opcao == 'Criar':
            self.InsertSetor()
        elif self.opcao == 'Alterar':
            self.AlterarSetor()"""