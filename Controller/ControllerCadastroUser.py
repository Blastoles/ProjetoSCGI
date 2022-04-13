from PyQt5 import uic

import Controller.ControllerUser
from View.ViewCadastroUser import viewCadastroUser
from Model.ModelCadastroUser import ModelCadastrouser
from DAO.DAOCadastroUser import DAOCadastraruser
from Controller.ControllerMensagem import SistemaMensagem

class SistemaCadastroUser():
    def Show(self,opcao,user):
        self.user = user
        self.opcao = opcao
        self.cduser.LimparDados()
        self.cduser.Show()

    def Close(self):
        self.cduser.Close()
        self.user.Tabela()

    def Opcao(self):
        if self.opcao == "Incluir":
            self.InsertDados()
        elif self.opcao == "Alterar":
            self.AlterarDados()

    def InsertDados(self):
        ddColetado = self.cduser.ColetaDados()
        if ddColetado[5] == True:
            ddColetado[5] = 1
        else:
            ddColetado[5] = 0
        if ddColetado[6] == True:
            ddColetado[6] = 1
        else:
            ddColetado[6] = 0
        if ddColetado[0] != '' and ddColetado[3] != '' and ddColetado[4] != '':
            userbanco = self.banco.CheckUser(ddColetado[3])
            if  userbanco == []:
                ddColetado[4] = self.model.EsconderSenha(ddColetado[4])
                linhadb = self.banco.ContLista() + 1
                self.banco.InserirDados(ddColetado,linhadb)
                self.user.Tabela()
            else:
                self.msg.MsgUserJaCadastrado()
        else:
            falta = ['','','']
            if ddColetado[0] == '':
                falta[0] = 'Nome\n'
            if ddColetado[3] == '':
                falta[1] = 'Usuário\n'
            if ddColetado[4] == '':
                falta[2] = 'Senha'
            self.msg.MsgFaltaDados(falta)

    #def AlterarDados(self):


    def __init__(self):
        self.cduser = viewCadastroUser()
        self.model = ModelCadastrouser()
        self.banco = DAOCadastraruser()
        self.msg = SistemaMensagem()
        self.opcao = ''
        self.user = ''
        self.cduser.tela.BT_Cancelar.clicked.connect(self.Close)
        self.cduser.tela.BT_Salvar.clicked.connect(self.Opcao)
