from os import getcwd
from PyQt5 import uic

class viewCadastroSetor():
    def Show(self):
        self.tela.show()

    def LimpeTela(self):
        self.tela.CP_Nome.setText('')
        self.tela.CP_Responsavel.setText('')
        self.tela.CP_Sigla.setText('')
        self.tela.CP_Prioridade.setCurrentIndex(0)
        self.tela.CP_Sigla.setDisabled(False)

    def ColetarDados(self):
        lista = []
        lista.append(self.tela.CP_Nome.text().upper())
        lista.append(self.tela.CP_Sigla.text().upper())
        lista.append(self.tela.CP_Responsavel.text().upper())
        lista.append(self.tela.CP_Prioridade.currentText())
        return lista

    def ColocarDados(self,dados):
        self.tela.CP_Sigla.setDisabled(True)
        self.tela.CP_Nome.setText(dados[0][1])
        self.tela.CP_Sigla.setText(dados[0][2])
        self.tela.CP_Responsavel.setText(dados[0][3])
        self.tela.CP_Prioridade.setCurrentIndex(dados[0][4])

    def Close(self):
        self.tela.close()

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\CadastroSetor.ui".format(Local))
