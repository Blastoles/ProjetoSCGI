## Bibliotecas ##
from PyQt5.QtWidgets import QMainWindow
from View.ViewCadastroSetor import viewCadastroSetor
from DAO.DAOCadastroSetor import DAOCadastrarSetor
from Model.ModelCadastroSetor import modelCadastroSetor
from Controller.ControllerMensagem import SistemaMensagem

## Classe principal ##
class SistemaCSetor(QMainWindow):

    ## Chama a tela ##
    def Show(self,opcao,setor):
        self.viewCSetor.LimpeTela()
        self.setor = setor
        self.opcao = opcao
        self.viewCSetor.Show()

    ## Fecha a tela ##
    def Close(self):
        self.viewCSetor.Close()

    ## Coleta os dados da tela para inserção dos dados no registro ##
    def InsertSetor(self):
        dados = self.viewCSetor.ColetarDados()
        if dados[1] != '' and dados[0] != '':
            check = self.DAOSetor.CheckUser(dados[1])
            if check == []:
                linhadb = self.DAOSetor.ContLista()
                dados[3] = self.ModelSetor.PrioridadeInt(dados[3])
                self.DAOSetor.InserirDados(dados,linhadb)
                self.viewCSetor.Close()
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

    ## Mostra os dados na tela ##
    def MostrarDados(self,TextoLinha):
        self.viewCSetor.ColocarDados(TextoLinha)

    ## Coleta os dados da tela para alterar registro ##
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
        self.viewCSetor.Close()
        self.setor.Tabela()

    ## Determina qual a configuração da tela ##
    def Opcao(self):
        if self.opcao == 'Criar':
            self.InsertSetor()
        elif self.opcao == 'Alterar':
            self.AlterarSetor()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.viewCSetor = viewCadastroSetor()
        self.DAOSetor = DAOCadastrarSetor()
        self.ModelSetor = modelCadastroSetor()
        self.msg = SistemaMensagem()
        self.opcao = ''
        self.setor = ''
        #Definição dos botões
        self.viewCSetor.tela.BT_Cancelar.clicked.connect(self.Close)
        self.viewCSetor.tela.BT_Salvar.clicked.connect(self.Opcao)