from View.ViewCadastroManutencao import viewCadastroManutencao

class SistemaCManutencao():

    def Show(self,cond):
        self.CManu.Show()

    def __init__(self):
        self.CManu = viewCadastroManutencao()