## Bibliotecas ##
from PyQt5.QtWidgets import QWidget
from DAO.DAORContagem import DAORContagem
from View.ViewRContagem import viewRContagem


## Classe principal ##
class SistemaRContagem(QWidget):

    ## Chama a tela ##
    def Show(self,Impressora):
        self.imp = Impressora
        self.GRela.Show()

    ## Fecha a tela ##
    def Close(self):
        self.GRela.Close()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.GRela = viewRContagem()
        self.banco = DAORContagem()
        self.imp = ''
        #Definição dos botões
        self.GRela.tela.BT_Voltar.clicked.connect(self.Close)