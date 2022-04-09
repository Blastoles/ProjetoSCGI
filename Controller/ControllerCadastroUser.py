from PyQt5 import uic, QtWidgets
from functools import partial
from View.ViewCadastroUser import viewCadastroUser

class SistemaCadastroUser():
    def Show(self):
        self.cduser.LimparDados()
        self.cduser.Show()

    def Close(self):
        self.cduser.Close()

    def __init__(self):
        self.cduser = viewCadastroUser()
        self.cduser.tela.BT_Cancelar.clicked.connect(self.Close)