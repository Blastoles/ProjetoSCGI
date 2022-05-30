from Controller.ControllerMensagem import SistemaMensagem
from DAO.DAOCadastroManutencao import DAOCadastrarManutencao
from Model.ModelCadastroManutencao import ModelCadastrarManutencao
from View.ViewCadastroManutencao import viewCadastroManutencao

class SistemaCManutencao():

    def Show(self,cond):
        self.opcao = cond
        self.CManu.LimpaInfo()
        self.CManu.LimpeLista()
        self.MostreLista()
        self.CManu.Show()

    def MostreLista(self):
        lista = self.banco.Lista()
        lista = self.model.TratarLista(lista)
        self.CManu.ColocarImpressora(lista)

    def Selecionado(self):
        selec = self.CManu.ImprSelect()
        self.CManu.LimpaDado()
        if selec != 'Selecione a Impressora':
            selec = selec.split(' -- ')
            dados = self.banco.BuscarDados(selec[0])
            self.CManu.ColocarInfo(dados)
        else:
            self.CManu.LimpaInfo()
            self.msg.MsgSelecionarImpr()

    def Close(self):
        self.CManu.Close()

    def Insert(self):
        check = self.CManu.PegarImpressora()
        if check != '':
            dados = self.CManu.ColetarDados()
            dados.append(check)
            if dados[0] != 'Escolha o tipo de manutenção':
                print(dados)
            else:
                falta = ['Tipo de Manutenção','','']
                self.msg.MsgFaltaDados(falta)


    def Update(self):
        print('1')

    def Opcao(self):
        if self.opcao == 'Criar':
            self.Insert()
        elif self.opcao == 'Alterar':
            self.Update()


    def __init__(self):
        self.CManu = viewCadastroManutencao()
        self.opcao = ''
        self.banco = DAOCadastrarManutencao()
        self.model = ModelCadastrarManutencao()
        self.msg = SistemaMensagem()
        self.CManu.tela.BT_Cancelar.clicked.connect(self.Close)
        self.CManu.tela.BT_Salvar.clicked.connect(self.Opcao)
        self.CManu.tela.BT_Selecionar.clicked.connect(self.Selecionado)