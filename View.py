from PyQt5 import uic, QtWidgets

class ViewLogin():
    def __init__(self):
        self.tela = uic.loadUi(".\Telas\Login.ui")
        ##self.Login.BT_Cancelar.clicked.connect(partial(self.LoginClose))

class ViewMenu():
    def __init__(self):
        self.tela = uic.loadUi(".\Telas\Home.ui")
        #self.Tela.BT_Usuario.clicked.connect(partial(CD_Usuario.Show))

class ViewMensagem():
    def __init__(self):
        self.tela = uic.loadUi(".\Telas\mensagem.ui")
        #self.Mensagem.BT_OK.clicked.connect(partial(self.MenClose))

class ViewUser():
    def __init__(self):
        self.tela = uic.loadUi(".\Telas\CD_Usuario.ui")
        #self.tela.BT_Pesquisar.clicked.connect(partial(self.PesquisaCadastro))
        #self.tela.BT_Voltar.clicked.connect(partial(self.Close))
        #self.tela.BT_Criar.clicked.connect(partial(self.Criar,'Criar'))
        #self.tela.TB_Cadastro.setColumnWidth(0, 254)
        #self.tela.BT_Alterar.clicked.connect(partial(self.AlterarCadastro))

class ViewCadastroUser():
    def __init__(self):
        self.tela = uic.loadUi(".\Telas\CadastroUsuario.ui")
'''
    if cond == 'Criar':
        self.criar.BT_Salvar.clicked.connect(partial(self.InsertDados))
    elif cond == 'Alterar':
        self.criar.BT_Salvar.clicked.connect(partial(self.UpdateDados))
    self.criar.BT_Cancelar.clicked.connect(partial(self.InsertClose))
'''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    login = ViewLogin()
    menu = ViewMenu()
    mensagem = ViewMensagem()
    usuario = ViewUser()
    cadastrouser = ViewCadastroUser()


    # Show das telas
    login.tela.show()
    menu.tela.show()
    mensagem.tela.show()
    usuario.tela.show()
    cadastrouser.tela.show()

    sys.exit(app.exec())
