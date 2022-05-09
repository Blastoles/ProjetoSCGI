from os import getcwd
from PyQt5 import uic

class viewCadastroContagem():
    def Show(self):
        self.tela.show()

    def LimpeTela(self):
        self.tela.CP_Impressora.clear()
        self.tela.CP_Impressora.addItem("Selecione a Impressora")
        self.tela.CP_Impressora.setCurrentIndex(0)
        self.tela.CP_Contagem.setText('')
        self.tela.CP_Data.setText('')
        self.tela.CP_CPreto.setText('')
        self.tela.CP_CMargenta.setText('')
        self.tela.CP_CAmarelo.setText('')
        self.tela.CP_CAzul.setText('')
        self.tela.CP_UltimaContagem.setText('')

    def ColetarDados(self):
        lista = []
        lista.append(self.tela.CP_Nome.text().upper())
        lista.append(self.tela.CP_Sigla.text().upper())
        lista.append(self.tela.CP_Responsavel.text().upper())
        lista.append(self.tela.CP_Prioridade.currentText())
        return lista

    def ColocarImpressora(self,lista):
        self.tela.CP_Impressora.addItems(lista)

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
        self.tela = uic.loadUi("{}View\Telas\CadastroContagem.ui".format(Local))
