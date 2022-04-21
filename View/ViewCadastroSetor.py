from PyQt5 import uic, QtWidgets

class viewCadastroSetor():
    def Show(self):
        self.tela.show()

    def LimpeTela(self):
        self.tela.CP_Nome.setText('')
        self.tela.CP_Responsavel.setText('')

    def ColetarDados(self):
        lista = []
        lista.append(self.tela.CP_Nome.text().upper())
        lista.append(self.tela.CP_Sigla.text().upper())
        lista.append(self.tela.CP_Responsavel.text().upper())
        lista.append(self.tela.CP_Prioridade.currentText())
        return lista

    def Close(self):
        self.tela.close()

    def __init__(self):
        self.tela = uic.loadUi(".\View\Telas\CadastroSetor.ui")

