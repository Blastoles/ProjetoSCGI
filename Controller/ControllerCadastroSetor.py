from View.ViewCadastroSetor import viewCadastroSetor
from DAO.DAOCadastroSetor import DAOCadastrarSetor
from Model.ModelCadastroSetor import modelCadastroSetor
from Controller.ControllerMensagem import SistemaMensagem

class SistemaCSetor():

    def Show(self,opcao,setor):
        self.viewCSetor.LimpeTela()
        self.setor = setor
        self.opcao = opcao
        self.viewCSetor.Show()

    def Close(self):
        self.viewCSetor.Close()

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
            self.AlterarSetor()

    def __init__(self):
        self.viewCSetor = viewCadastroSetor()
        self.DAOSetor = DAOCadastrarSetor()
        self.ModelSetor = modelCadastroSetor()
        self.msg = SistemaMensagem()
        self.opcao = ''
        self.setor = ''
        self.viewCSetor.tela.BT_Cancelar.clicked.connect(self.Close)
        self.viewCSetor.tela.BT_Salvar.clicked.connect(self.Opcao)