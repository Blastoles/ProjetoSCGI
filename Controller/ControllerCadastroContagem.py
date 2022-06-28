## Bibliotecas ##
from PyQt5.QtWidgets import QMainWindow
from Controller.ControllerMensagem import SistemaMensagem
from DAO.DAOCadastroContagem import DAOCadastrarContagem
from Model.ModelCadastrarContagem import ModelCadastrarContagem
from View.ViewCadastroContagem import viewCadastroContagem

## Classe principal ##
class SistemaCContagem(QMainWindow):

    ## Chama a tela ##
    def Show(self,opcao):
        self.opcao = opcao
        self.viewCContagem.LimpeLista()
        self.viewCContagem.LimpeTela()
        self.viewCContagem.LimpaInfo()
        self.MostreLista()
        self.viewCContagem.Show()

    ## Fecha a tela ##
    def Close(self):
        self.viewCContagem.Close()

    ## Mostra na tela lista do banco ##
    def MostreLista(self):
        lista = self.banco.Lista()
        lista = self.model.TratarLista(lista)
        self.viewCContagem.ColocarImpressora(lista)

    ## Busca na tela seleção e apresenta na tela dados complementares ##
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

    ## Determina qual a configuração da tela ##
    def Opcao(self):
        if self.opcao == 'Criar':
            self.InsertContagem()
        elif self.opcao == 'Alterar':
            self.AlterarContagem()

    ## Coleta os dados da tela para inserção dos dados no registro ##
    def InsertContagem(self):
        check = self.viewCContagem.PegarImpressora()
        if check != '':
            dado = self.viewCContagem.ColetaDados()
            if dado[0] != '' and dado[1] != '//':
                linhadb = self.banco.ContLista()
                dado.append(check)
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

    ## Mostra dados na tela ##
    def ColoqueDados(self,dados):
        dado = self.banco.BuscarDados(dados[0][1])
        ultima = self.banco.UltimaContagem(dado[0][0])
        if ultima != []:
            Ucont = (str(ultima[0][0]) + ' -- ' + str(ultima[0][1]))
        else:
            Ucont = ''
        self.viewCContagem.ColocarInfo(dado, Ucont)
        self.viewCContagem.ColocarDados(dados)

    ## Coleta dados na tela para alteração de registro ##
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

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.viewCContagem = viewCadastroContagem()
        self.msg = SistemaMensagem()
        self.banco = DAOCadastrarContagem()
        self.model = ModelCadastrarContagem()
        self.opcao = ''
        #Definição dos botões
        self.viewCContagem.tela.BT_Cancelar.clicked.connect(self.Close)
        self.viewCContagem.tela.BT_Selecionar.clicked.connect(self.Selecionado)
        self.viewCContagem.tela.BT_Salvar.clicked.connect(self.Opcao)
