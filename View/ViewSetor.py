from PyQt5 import uic

class viewSetor():
    def Show(self):
        self.tela.show()

    def Close(self):
        self.tela.close()

    def __init__(self):
        self.tela = uic.loadUi(".\View\Telas\CD_Setor.ui")
