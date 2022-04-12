from PyQt5 import uic, QtWidgets
from functools import partial
from View.ViewMenu import viewMenu
from Controller.ControllerUser import SistemaUser


class SistemaMenu():
    def Show(self):
        self.menu.Show()

    def Close(self):
        self.menu.tela.close()

    def UserShow(self):
        self.user.Show()


    def __init__(self):
        self.menu = viewMenu()
        self.user = SistemaUser()
        self.menu.tela.BT_Usuario.clicked.connect(self.UserShow)
"""        self.menu.tela.BT_Impressora.clicked.connect(partial())
        self.menu.tela.BT_Setor.clicked.connect(partial())
        self.menu.tela.BT_Contagem.clicked.connect(partial())
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
