from View.ViewCadastroSetor import viewCadastroSetor

class SistemaCSetor():

    def Show(self):
        self.viewCSetor.LimpeTela()
        self.viewCSetor.Show()

    def Close(self):
        self.viewCSetor.Close()

    def Opcao(self):
        print()

    def __init__(self):
        self.viewCSetor = viewCadastroSetor()
        self.viewCSetor.tela.BT_Cancelar.clicked.connect(self.Close)
        self.viewCSetor.tela.BT_Salvar.clicked.connect(self.Opcao)