from PyQt5.QtWidgets import QMainWindow

from View.ViewConfirmacao import viewConfirmacao


class SistemaConfirmacao(QMainWindow):
    def Show(self,Self,lista):
        self.Chamado = Self
        self.lista = lista
        self.conf.Show()

    def Nao(self):
        self.conf.Close()

    def Sim(self):
        self.conf.Close()
        self.Chamado.ExcluirConfirmado(self.lista)


    def __init__(self):
        super().__init__()
        self.conf = viewConfirmacao()
        self.Chamado = ''
        self.lista = ''
        self.conf.tela.BT_Sim.clicked.connect(self.Sim)
        self.conf.tela.BT_Nao.clicked.connect(self.Nao)
