from Controller.ControllerMensagem import SistemaMensagem
from DAO.DAOCadastroManutencao import DAOCadastrarManutencao
from Model.ModelCadastroManutencao import ModelCadastrarManutencao
from View.ViewCadastroManutencao import viewCadastroManutencao

class SistemaCManutencao():

    def Show(self,cond):
        self.opcao = cond
        self.CManu.LimpaInfo()
        self.CManu.LimpaDado()
        self.MostreLista()
        self.CManu.Show()

    def MostreLista(self):
        self.CManu.LimpeLista()
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
            if dados[0] != 'Escolha o tipo de manutenção' and dados[1] != '//' and dados[2] != '':
                dado = self.model.TratarDados(dados)
                linhadb = self.banco.ContLista()
                self.banco.InsertManutencao(dado,linhadb)
                self.CManu.Close()
            else:
                falta = ['', '', '']
                if dados[0] == 'Escolha o tipo de manutenção':
                    falta[0] = 'Tipo de Manutenção\n'
                if dados[1] == '//':
                    falta[1] = 'Data que Parou\n'
                if dados[2] == '':
                    falta[2] = 'Descrição\n'
                self.msg.MsgFaltaDados(falta)
        else:
            self.msg.MsgSelecionarImpr()

    def ColoqueDados(self, dados):
        dado = self.banco.BuscarDados(dados[0][7])
        self.CManu.ColocarInfo(dado)
        self.CManu.ColocarDados(dados)

    def Update(self):
        print('1')

    def Opcao(self):
        if self.opcao == 'Criar':
            self.Insert()
        elif self.opcao == 'Alterar':
            self.Update()

    def DataVtFuncionar(self):
        self.CManu.DataVtFuncionar()

    def __init__(self):
        self.CManu = viewCadastroManutencao()
        self.opcao = ''
        self.banco = DAOCadastrarManutencao()
        self.model = ModelCadastrarManutencao()
        self.msg = SistemaMensagem()
        self.CManu.tela.BT_Cancelar.clicked.connect(self.Close)
        self.CManu.tela.BT_Salvar.clicked.connect(self.Opcao)
        self.CManu.tela.BT_Selecionar.clicked.connect(self.Selecionado)
        self.CManu.tela.CP_Voltou.clicked.connect(self.DataVtFuncionar)
        self.CManu.tela.CP_NVoltou.clicked.connect(self.DataVtFuncionar)