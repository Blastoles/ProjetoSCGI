from PyQt5 import uic, QtWidgets

from Controller.ControllerContagemImpressora import SistemaContagem
from View.ViewMenu import viewMenu
from Controller.ControllerUser import SistemaUser
from Controller.ControllerSetor import SistemaSetor
from Controller.ControllerImpressora import SistemaImpressora

class SistemaMenu():
    def Show(self):
        self.menu.Show()

    def Close(self):
        self.menu.tela.close()

    def UserShow(self):
        self.user.Show()

    def ImpressoraShow(self):
        self.impre.Show()

    def SetorShow(self):
        self.setor.Show()

    def ContagemShow(self):
        self.contagem.Show()

    def __init__(self):
        self.menu = viewMenu()
        self.user = SistemaUser()
        self.setor = SistemaSetor()
        self.impre = SistemaImpressora()
        self.contagem = SistemaContagem()
        self.menu.tela.BT_Usuario.clicked.connect(self.UserShow)
        self.menu.tela.BT_Setor.clicked.connect(self.SetorShow)
        self.menu.tela.BT_Impressora.clicked.connect(self.ImpressoraShow)
        self.menu.tela.BT_Contagem.clicked.connect(self.ContagemShow)
"""        
        self.menu.tela.BT_Manutencao.clicked.connect(partial())
        self.menu.tela.BT_Relatorio.clicked.connect(partial())"""


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    menu = ()

    # Show das telas
    menu.tela.show()
    sys.exit(app.exec())
