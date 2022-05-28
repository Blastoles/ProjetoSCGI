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
            if ultima != []:
                Ucont = (str(ultima[0][0])+ ' -- ' + str(ultima[0][1]))
            else:
                Ucont = ''
            self.viewCContagem.ColocarInfo(dados,Ucont)
        else:
            self.viewCContagem.LimpaInfo()
            self.msg.MsgSelecionarImpr()

    def Opcao(self):
        if self.opcao == 'Criar':
            self.InsertContagem()
        elif self.opcao == 'Alterar':
            self.AlterarContagem()

    def InsertContagem(self):
        check = self.viewCContagem.PegarImpressora()
        if check != '':
            dado = self.viewCContagem.ColetaDados()
            if dado[0] != '' and dado[1] != '//':
                linhadb = self.banco.ContLista()
                dado.append(check)
                print(dado)
                self.banco.InsertContagem(dado,linhadb)
                self.viewCContagem.Close()
            else:
                falta = ['','','']
                if dado[0] == '':
                    falta[0] = 'Contagem\n'
                if dado[1] == '//':
                    falta[1] = 'Data\n'
                self.msg.MsgFaltaDados(falta)
        else:
            self.msg.MsgSelecionarImpr()

    def ColoqueDados(self,dados):
        dado = self.banco.BuscarDados(dados[0][1])
        ultima = self.banco.UltimaContagem(dado[0][0])
        if ultima != []:
            Ucont = (str(ultima[0][0]) + ' -- ' + str(ultima[0][1]))
        else:
            Ucont = ''
        self.viewCContagem.ColocarInfo(dado, Ucont)
        self.viewCContagem.ColocarDados(dados)

    def AlterarContagem(self):
        dado = self.viewCContagem.ColetaDados()
        if dado[0] != '' and dado[1] != '//':
            self.banco.UpdateContagem(dado)
            self.viewCContagem.Close()
        else:
            falta = ['', '', '']
            if dado[0] == '':
                falta[0] = 'Contagem\n'
            if dado[1] == '//':
                falta[1] = 'Data\n'
            self.msg.MsgFaltaDados(falta)

    def __init__(self):
        self.viewCContagem = viewCadastroContagem()
        self.msg = SistemaMensagem()
        self.banco = DAOCadastrarContagem()
        self.model = ModelCadastrarContagem()
        self.opcao = ''
        self.viewCContagem.tela.BT_Cancelar.clicked.connect(self.Close)
        self.viewCContagem.tela.BT_Selecionar.clicked.connect(self.Selecionado)
        self.viewCContagem.tela.BT_Salvar.clicked.connect(self.Opcao)
