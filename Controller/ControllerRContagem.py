## Bibliotecas ##
from PyQt5.QtWidgets import QWidget
from View.ViewRContagem import GRelatorio

## Classe principal ##
class SistemaGRelatorio(QWidget):

    ## Chama a tela ##
    def Show(self):
        self.GRela.Show()

    ## Fecha a tela ##
    def Close(self):
        self.GRela.Close()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.GRela = GRelatorio()
        #Definição dos botões
        self.GRela.tela.BT_Voltar.clicked.connect(self.Close)