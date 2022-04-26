from View.ViewConfirmacao import viewConfirmacao


class SistemaConfirmacao():
    def Show(self):
        self.conf.Show()

    def Nao(self):
        self.conf.Close()
        return 0

    def Sim(self):
        self.conf.Close()
        return 1

    def __init__(self):
        self.conf = viewConfirmacao()
        self.conf.tela.BT_Sim.clicked.connect(self.Sim)
        self.conf.tela.BT_Nao.clicked.connect(self.Nao)
