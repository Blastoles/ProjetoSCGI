from View.ViewCadastroImpressora import viewCadastroImpressora

class SistemaCadastroImpressora():

    def Show(self):
        self.viewcdImp.Show()

    def Close(self):
        self.viewcdImp.Close()

    def InsertDados(self):
        self.viewcdImp.ColetaDados()

    def Opcao(self):
        self.InsertDados()
        print('opcao')

    def __init__(self):
        self.viewcdImp = viewCadastroImpressora()

        self.viewcdImp.tela.BT_Cancelar.clicked.connect(self.Close)
        self.viewcdImp.tela.BT_Salvar.clicked.connect(self.Opcao)