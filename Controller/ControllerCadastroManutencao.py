from View.ViewCadastroManutencao import viewCadastroManutencao

class SistemaCManutencao():

    def Show(self,cond):
        self.CManu.LimpaInfo()
        self.CManu.LimpeLista()
        self.CManu.Show()

    def Close(self):
        self.CManu.Close()

    def Salve(self):
        print('1')


    def __init__(self):
        self.CManu = viewCadastroManutencao()
        self.CManu.tela.BT_Cancelar.clicked.connect(self.Close)
        self.CManu.tela.BT_Salvar.clicked.connect(self.Salve)