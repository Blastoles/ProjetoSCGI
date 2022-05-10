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
        if ((lista[0] != '') and (lista[2] != '')):
            check = self.banco.CheckImp(lista[0])
            if check == []:
                lista = self.model.TratarInsert(lista)
                linhadb = self.banco.ContLista()
                self.banco.InserirDados(lista,linhadb)
                self.viewcdImp.Close()
                self.imp.Tabela()
            else:
                self.msg.MsgImprJaCadastrado()
        else:
            falta = ['','','']
            if lista[0] == '':
                falta[0] = 'Número de Série\n'
            if lista[2] == '':
                falta[1] = 'Modelo da Impressora\n'
            self.msg.MsgFaltaDados(falta)

    def AlterarDados(self):
        dados = self.viewcdImp.ColetaDados()
        dados = self.model.TratarInsert(dados)
        self.banco.UpdateDados(dados)
        self.viewcdImp.Close()
        self.imp.Tabela()

    def MostrarDados(self,TextoLinha):
        TxLinha = self.model.TratarConvert(TextoLinha[0])
        self.viewcdImp.ColocarDados(TxLinha)

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
