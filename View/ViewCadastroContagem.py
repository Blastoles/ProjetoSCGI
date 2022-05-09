from os import getcwd
from PyQt5 import uic

class viewCadastroContagem():
    def Show(self):
        self.tela.show()

    def LimpeLista(self):
        self.tela.CP_Impressora.clear()
        self.tela.CP_Impressora.addItem("Selecione a Impressora")
        self.tela.CP_Impressora.setCurrentIndex(0)

    def LimpeTela(self):
        self.tela.CP_Contagem.setText('')
        self.tela.CP_Data.setText('')
        self.tela.CP_CPreto.setText('')
        self.tela.CP_CMargenta.setText('')
        self.tela.CP_CAmarelo.setText('')
        self.tela.CP_CAzul.setText('')
        self.tela.CP_UltimaContagem.setText('')

    def LimpaInfo(self):
        self.tela.Info_Num.setText('')
        self.tela.Info_Modelo.setText('')
        self.tela.Info_Amigavel.setText('')
        self.tela.Info_Setor.setText('')
        self.tela.Info_MPreto.setText('')
        self.tela.Info_MMargenta.setText('')
        self.tela.Info_MAmarelo.setText('')
        self.tela.Info_MAzul.setText('')
        self.tela.CP_UltimaContagem.setText('')

    def ColocarInfo(self,dado,ultima):
        self.tela.Info_Num.setText(dado[0][0])
        self.tela.Info_Modelo.setText(dado[0][1])
        self.tela.Info_Amigavel.setText(dado[0][2])
        self.tela.Info_Setor.setText(dado[0][3])
        self.tela.Info_MPreto.setText(dado[0][4])
        self.tela.Info_MMargenta.setText(dado[0][5])
        self.tela.Info_MAmarelo.setText(dado[0][6])
        self.tela.Info_MAzul.setText(dado[0][7])
        self.tela.CP_UltimaContagem.setText(ultima)

    def ImprSelect(self):
        impr = self.tela.CP_Impressora.currentText()
        return impr

    def ColocarImpressora(self,lista):
        self.tela.CP_Impressora.addItems(lista)

    def PegarImpressora(self):
        check = self.tela.Info_Num.text()
        return check

    def Close(self):
        self.tela.close()

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\CadastroContagem.ui".format(Local))
