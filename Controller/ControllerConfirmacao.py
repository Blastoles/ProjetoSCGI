## Bibliotecas ##
from PyQt5.QtWidgets import QMainWindow
from View.ViewConfirmacao import viewConfirmacao

## Classe principal ##
class SistemaConfirmacao(QMainWindow):

    ## Chama a tela ##
    def Show(self,Self,lista):
        self.Chamado = Self
        self.lista = lista
        self.conf.Show()

    ## Chama a negação ##
    def Nao(self):
        self.conf.Close()

    ## Chama a confirmação ##
    def Sim(self):
        self.conf.Close()
        self.Chamado.ExcluirConfirmado(self.lista)

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.conf = viewConfirmacao()
        self.Chamado = ''
        self.lista = ''
        #Definição dos botões
        self.conf.tela.BT_Sim.clicked.connect(self.Sim)
        self.conf.tela.BT_Nao.clicked.connect(self.Nao)
