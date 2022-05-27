from View.ViewManutencao import viewManutencao


class SistemaManutencao():

    def Show(self):
        self.viewManu.Show()

    def Close(self):
        self.viewManu.Close()

    def __init__(self):
        self.viewManu = viewManutencao()
        self.viewManu.tela.BT_Voltar.clicked.connect(self.Close)
        """
        self.viewManu.tela.BT_Criar.clicked.connect(self.Close)
        self.viewManu.tela.BT_Exclui.clicked.connect(self.Close)
        self.viewManu.tela.BT_Alterar.clicked.connect(self.Close)
        self.viewManu.tela.BT_Selecionar.clicked.connect(self.Close)
        
        """