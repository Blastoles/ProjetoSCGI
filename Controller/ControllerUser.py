from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QDialog
from functools import partial
from View.ViewUser import viewUser
from DAO.DAOUser import DAOuser
from Model.ModelUser import Modeluser


class SistemaUser():
    def Show(self):
        self.user.Show()

    def Lista(self):
        self.user.tela.TB_Cadastro.clearContents()

    def PesquisarCadastro(self):
        texto = self.user.Dados()
        lista = self.banco.Pesquisa(texto)
        self.model.Tabela(lista)

    def __init__(self):
        self.user = viewUser()
        self.banco = DAOuser()
        self.model = Modeluser()
        self.user.tela.BT_Voltar.clicked.connect(partial(self.user.Close))
        self.user.tela.TB_Cadastro.setColumnWidth(0, 254)
        self.user.tela.BT_Pesquisar.clicked.connect(partial(self.PesquisarCadastro))

'''        self.user.tela.BT_Criar.clicked.connect(partial(self.Criar,'Criar'))
        self.user.tela.BT_Alterar.clicked.connect(partial(self.AlterarCadastro))'''


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    menu = ()

    # Show das telas
    menu.tela.show()
    sys.exit(app.exec())
