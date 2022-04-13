from PyQt5 import uic, QtWidgets
from functools import partial

import Controller.ControllerMenu
from View.ViewUser import viewUser
from DAO.DAOUser import DAOuser
from Model.ModelUser import Modeluser
from Controller.ControllerCadastroUser import SistemaCadastroUser


class SistemaUser():
    def Show(self):
        self.user.Show()
        lista = self.banco.TodaLista()
        self.model.Tabela(self.user,lista)

    def Close(self):
        self.user.tela.close()


    def PesquisarCadastro(self):
        texto = self.user.Dados()
        lista = self.banco.Pesquisa(texto)
        self.model.Tabela(self.user,lista)

    def Criar(self):
        self.cduser.Show()




    def __init__(self):
        self.user = viewUser()
        self.banco = DAOuser()
        self.model = Modeluser()
        self.cduser = SistemaCadastroUser()
        self.user.tela.BT_Voltar.clicked.connect(self.Close)
        self.user.tela.BT_Pesquisar.clicked.connect(partial(self.PesquisarCadastro))
        self.user.tela.BT_Criar.clicked.connect(partial(self.Criar))
        #self.user.tela.BT_Alterar.clicked.connect(partial(self.AlterarCadastro))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    menu = ()

    # Show das telas
    menu.tela.show()
    sys.exit(app.exec())
