from Controller.ControllerMensagem import SistemaMensagem
from DAO.DAOCadastroContagem import DAOCadastrarContagem
from Model.ModelCadastrarContagem import ModelCadastrarContagem
from View.ViewCadastroContagem import viewCadastroContagem


class SistemaCContagem():

    def Show(self,opcao):
        self.opcao = opcao
        self.viewCContagem.LimpeLista()
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
        self.viewCContagem.LimpeTela()
        if selec != 'Selecione a Impressora':
            selec = selec.split(' -- ')
            dados = self.banco.BuscarDados(selec[0])
            ultima = self.banco.UltimaContagem(selec[0])
            teste = (str(ultima[0][0])+ ' -- ' + str(ultima[0][1]))
            self.viewCContagem.ColocarInfo(dados,teste)
        else:
            self.viewCContagem.LimpaInfo()
            self.msg.MsgSelecionarImpr()

    def Opcao(self):
        if self.opcao == 'Criar':
            self.InsertSetor()
        elif self.opcao == 'Alterar':
            self.AlterarSetor()

    def InsertSetor(self):
        check = self.viewCContagem.PegarImpressora()
        if check != '':
            print(check)

    def AlterarSetor(self):
        print('Alterar')

    def __init__(self):
        self.viewCContagem = viewCadastroContagem()
        self.msg = SistemaMensagem()
        self.banco = DAOCadastrarContagem()
        self.model = ModelCadastrarContagem()
        self.opcao = ''
        self.viewCContagem.tela.BT_Cancelar.clicked.connect(self.Close)
        self.viewCContagem.tela.BT_Selecionar.clicked.connect(self.Selecionado)
        self.viewCContagem.tela.BT_Salvar.clicked.connect(self.Opcao)
