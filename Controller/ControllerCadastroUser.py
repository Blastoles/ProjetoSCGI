from PyQt5 import uic, QtWidgets
from functools import partial
from View.ViewCadastroUser import viewCadastroUser
from Controller.ControllerMensagem import SistemaMensagem

class SistemaCadastroUser():
    def Show(self):
        self.cduser.LimparDados()
        self.cduser.Show()

    def Close(self):
        self.cduser.Close()

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
            print('tem dados')
        else:
            self.msg.MsgFaltaDados()
        print(ddColetado)


    def __init__(self):
        self.msg = SistemaMensagem()
        self.cduser = viewCadastroUser()
        self.cduser.tela.BT_Cancelar.clicked.connect(self.Close)
        self.cduser.tela.BT_Salvar.clicked.connect(partial(self.InsertDados))