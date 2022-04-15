from PyQt5 import uic

class viewCadastroImpressora():

    def Show(self):
        self.tela.show()




    def __init__(self):
        self.tela = uic.loadUi(".\View\Telas\CadastroImpressora")