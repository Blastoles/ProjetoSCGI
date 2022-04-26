from View.ViewCadastroImpressora import viewCadastroImpressora

class SistemaCadastroImpressora():

    def Show(self,opcao,Self):
        self.opcao = opcao
        self.imp = Self
        self.viewcdImp.LimparDados()
        self.viewcdImp.Show()

    def Close(self):
        self.viewcdImp.Close()

    def InsertDados(self):
        self.viewcdImp.ColetaDados()

    def AlterarDados(self):
        print()




    def Opcao(self):
        if self.opcao == "Incluir":
            self.InsertDados()
        elif self.opcao == "Alterar":
            self.AlterarDados()

    def __init__(self):
        self.viewcdImp = viewCadastroImpressora()
        self.opcao = ''
        self.imp = ''
        self.viewcdImp.tela.BT_Cancelar.clicked.connect(self.Close)
        self.viewcdImp.tela.BT_Salvar.clicked.connect(self.Opcao)