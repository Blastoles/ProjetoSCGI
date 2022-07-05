## Bibliotecas ##
from os import getcwd
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget

## Classe visualização da tela ##
class viewRContagem(QWidget):

    ## Chama a tela ##
    def Show(self):
        self.tela.show()

    def LimpaDados(self):
        self.tela.DD_Num.setText('Falta dados')
        self.tela.DD_Modelo.setText('Falta dados')
        self.tela.DD_MAC.setText('Falta dados')
        self.tela.DD_Setor.setText('Falta dados')
        self.tela.DD_IP.setText('Falta dados')
        self.tela.DD_Data.setText('Falta dados')

    ## Mostra lista na tela ##
    def Lista(self,i,j,texto):
        self.tela.TB_Contagem.setItem(i, j, QtWidgets.QTableWidgetItem(texto))

    def PreenchaDados(self,DadoImp):
        self.tela.DD_Num.setText(DadoImp[0])
        self.tela.DD_Modelo.setText(DadoImp[1])
        self.tela.DD_MAC.setText(DadoImp[2])
        self.tela.DD_Setor.setText(DadoImp[3])
        self.tela.DD_IP.setText(DadoImp[4])
        self.tela.DD_Data.setText(DadoImp[5])

    ## Fecha a tela ##
    def Close(self):
        self.tela.close()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:', 'C:\\')
        self.tela = uic.loadUi("{}View\Telas\TelaRelatorio.ui".format(Local))
