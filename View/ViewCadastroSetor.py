## Bibliotecas ##
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

## Classe visualização da tela ##
class viewCadastroSetor(QWidget):

    ## Chama a tela ##
    def Show(self):
        self.tela.show()

    ## Limpa dados da tela ##
    def LimpeTela(self):
        self.tela.CP_Nome.setText('')
        self.tela.CP_Responsavel.setText('')
        self.tela.CP_Sigla.setText('')
        self.tela.CP_Prioridade.setCurrentIndex(0)
        self.tela.CP_Sigla.setDisabled(False)

    ## Coleta dados da tela ##
    def ColetarDados(self):
        lista = []
        lista.append(self.tela.CP_Nome.text().upper())
        lista.append(self.tela.CP_Sigla.text().upper())
        lista.append(self.tela.CP_Responsavel.text().upper())
        lista.append(self.tela.CP_Prioridade.currentText())
        return lista

    ## Mostra dados na tela ##
    def ColocarDados(self,dados):
        self.tela.CP_Sigla.setDisabled(True)
        self.tela.CP_Nome.setText(dados[0][1])
        self.tela.CP_Sigla.setText(dados[0][2])
        self.tela.CP_Responsavel.setText(dados[0][3])
        self.tela.CP_Prioridade.setCurrentIndex(dados[0][4])

    ## Fecha a tela ##
    def Close(self):
        self.tela.close()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.tela = uic.loadUi("..\\View\Telas\CadastroSetor.ui")
