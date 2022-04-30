from View.ViewCadastroImpressora import viewCadastroImpressora
from DAO.DAOCadastroImpressora import DAOCadastrarimpressora
from Model.ModelCadastroImpressora import ModelCadastroImpressora
from Controller.ControllerMensagem import SistemaMensagem

class SistemaCadastroImpressora():

    def Show(self,opcao,Self):
        self.opcao = opcao
        self.imp = Self
        setor = self.banco.ConsultaSetor()
        self.viewcdImp.LimparDados()
        self.viewcdImp.Show(setor)

    def Close(self):
        self.viewcdImp.Close()

    def InsertDados(self):
        lista = self.viewcdImp.ColetaDados()
        lista = self.model.TratarInsert(lista)
        if ((lista[0] != '') and (lista[2] != '')):
            linhadb = self.banco.ContLista()
            self.banco.InserirDados(lista,linhadb)
        else:
            falta = ['','','']
            if lista[0] == '':
                falta[0] = 'Número de Série\n'
            if lista[2] == '':
                falta[1] = 'Modelo da Impressora\n'
            self.msg.MsgFaltaDados(falta)

    def AlterarDados(self):
        print()




    def Opcao(self):
        if self.opcao == "Incluir":
            self.InsertDados()
        elif self.opcao == "Alterar":
            self.AlterarDados()

    def __init__(self):
        self.viewcdImp = viewCadastroImpressora()
        self.opcao = ''
        self.imp = ''
        self.banco = DAOCadastrarimpressora()
        self.model = ModelCadastroImpressora()
        self.msg = SistemaMensagem()
        self.viewcdImp.tela.BT_Cancelar.clicked.connect(self.Close)
        self.viewcdImp.tela.BT_Salvar.clicked.connect(self.Opcao)
