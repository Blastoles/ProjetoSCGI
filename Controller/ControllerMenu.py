## Bibliotecas ##
from PyQt5.QtWidgets import QMainWindow
from Controller.ControllerContagemImpressora import SistemaContagem
from Controller.ControllerManutencao import SistemaManutencao
from Controller.ControllerRelatorio import SistemaRelatorio
from View.ViewMenu import viewMenu
from Controller.ControllerUser import SistemaUser
from Controller.ControllerSetor import SistemaSetor
from Controller.ControllerImpressora import SistemaImpressora

## Classe principal ##
class SistemaMenu(QMainWindow):

    ## Chama a tela ##
    def Show(self):
        self.menu.Show()

    ## Fecha a tela ##
    def Close(self):
        self.menu.tela.close()

    ## Chama a tela de usuário ##
    def UserShow(self):
        self.user.Show()

    ## Chama a tela de impressora ##
    def ImpressoraShow(self):
        self.impre.Show()

    ## Chama a tela de setor ##
    def SetorShow(self):
        self.setor.Show()

    ## Chama a tela de contagem ##
    def ContagemShow(self):
        self.contagem.Show()

    ## Chama a tela de manutencao ##
    def ManutencaoShow(self):
        self.manutencao.Show()

    ## Chama a tela de relatorio ##
    def RelatorioShow(self):
        self.relatorio.Show()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.menu = viewMenu()
        self.user = SistemaUser()
        self.setor = SistemaSetor()
        self.impre = SistemaImpressora()
        self.contagem = SistemaContagem()
        self.manutencao = SistemaManutencao()
        self.relatorio = SistemaRelatorio()
        #Definição dos botões
        self.menu.tela.BT_Usuario.clicked.connect(self.UserShow)
        self.menu.tela.BT_Setor.clicked.connect(self.SetorShow)
        self.menu.tela.BT_Impressora.clicked.connect(self.ImpressoraShow)
        self.menu.tela.BT_Contagem.clicked.connect(self.ContagemShow)
        self.menu.tela.BT_Manutencao.clicked.connect(self.ManutencaoShow)
        self.menu.tela.BT_Relatorio.clicked.connect(self.RelatorioShow)
