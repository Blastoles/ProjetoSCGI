from os import getcwd
from PyQt5 import uic

class viewCadastroImpressora():

    def Show(self,setor):
        for i in setor:
            self.tela.CP_Setor.addItem(i[0]+' -- '+i[1])
        self.tela.show()

    def Close(self):
        self.tela.close()

    def LimparDados(self):
        self.tela.CP_Num_Serie.setText('')
        self.tela.CP_MAC.setText('')
        self.tela.CP_ModeloImpre.setText('')
        self.tela.CP_Fabricante.setText('')
        self.tela.CP_Nome.setText('')
        self.tela.CP_Data.setText('')
        self.tela.CP_Setor.setCurrentIndex(0)
        self.tela.CP_Ativo.setCheckState(-1)
        self.tela.CP_Terceiros.setCheckState(0)
        self.tela.CP_USB.setCheckState(0)
        self.tela.CP_Rede.setCheckState(0)
        self.tela.CP_Wifi.setCheckState(0)
        self.tela.CP_IP.setText('')
        self.tela.CP_Preto.setCheckState(0)
        self.tela.CP_MPreto.setText('')
        self.tela.CP_Color.setCheckState(0)
        self.tela.CP_MMagenta.setText('')
        self.tela.CP_MAmarelo.setText('')
        self.tela.CP_MAzul.setText('')

    def ColetaDados(self):
        lista = []
        lista.append(self.tela.CP_Num_Serie.text().upper())
        lista.append(self.tela.CP_MAC.text())
        lista.append(self.tela.CP_ModeloImpre.text().upper())
        lista.append(self.tela.CP_Fabricante.text().upper())
        lista.append(self.tela.CP_Nome.text().upper())
        lista.append(self.tela.CP_Data.text())
        sep = self.tela.CP_Setor.currentText()
        sep = sep.split(' -- ')
        lista.append(sep[0])
        lista.append(sep[1])
        lista.append(self.tela.CP_Ativo.isChecked())
        lista.append(self.tela.CP_Terceiros.isChecked())
        lista.append(self.tela.CP_USB.isChecked())
        lista.append(self.tela.CP_Rede.isChecked())
        lista.append(self.tela.CP_Wifi.isChecked())
        if ((lista[11] == True) or (lista[12] == True)):
            lista.append(self.tela.CP_IP.text())
        else:
            lista.append('')
        lista.append(self.tela.CP_Preto.isChecked())
        if lista[14] == True:
            lista.append(self.tela.CP_MPreto.text().upper())
        else:
            lista.append('')
        lista.append(self.tela.CP_Color.isChecked())
        if lista[16] == True:
            lista.append(self.tela.CP_MMagenta.text().upper())
            lista.append(self.tela.CP_MAmarelo.text().upper())
            lista.append(self.tela.CP_MAzul.text().upper())
        else:
            lista.append('')
            lista.append('')
            lista.append('')
        return lista

    def ColocarDados(self,TextoLinha,box):
        self.tela.CP_Usuario.setDisabled(True)

    def PossuiRede(self):
        marcadoRede = self.tela.CP_Rede.isChecked()
        marcadoWifi = self.tela.CP_Wifi.isChecked()
        if marcadoRede == True or marcadoWifi == True:
            self.tela.CP_IP.show()
            self.tela.TX_IP.show()
        else:
            self.tela.CP_IP.hide()
            self.tela.TX_IP.hide()

    def MonoCromatico(self):
        marcadoPreto = self.tela.CP_Preto.isChecked()
        if marcadoPreto == True:
            self.tela.CP_MPreto.show()
            self.tela.TX_MPreto.show()
        else:
            self.tela.CP_MPreto.hide()
            self.tela.TX_MPreto.hide()

    def Cromatico(self):
        marcadoColor = self.tela.CP_Color.isChecked()
        if marcadoColor == True:
            self.tela.CP_MMagenta.show()
            self.tela.TX_MMagenta.show()

            self.tela.CP_MAmarelo.show()
            self.tela.TX_MAmarelo.show()

            self.tela.CP_MAzul.show()
            self.tela.TX_MAzul.show()
        else:
            self.tela.CP_MMagenta.hide()
            self.tela.TX_MMagenta.hide()

            self.tela.CP_MAmarelo.hide()
            self.tela.TX_MAmarelo.hide()

            self.tela.CP_MAzul.hide()
            self.tela.TX_MAzul.hide()

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\CadastroImpressora.ui".format(Local))
        #self.tela = uic.loadUi(".\View\Telas\CadastroImpressora.ui")
        self.tela.CP_Rede.clicked.connect(self.PossuiRede)
        self.tela.CP_Wifi.clicked.connect(self.PossuiRede)
        self.tela.CP_Preto.clicked.connect(self.MonoCromatico)
        self.tela.CP_Color.clicked.connect(self.Cromatico)
        self.tela.CP_IP.hide()
        self.tela.CP_MPreto.hide()
        self.tela.CP_MMagenta.hide()
        self.tela.CP_MAmarelo.hide()
        self.tela.CP_MAzul.hide()
        self.tela.TX_IP.hide()
        self.tela.TX_MPreto.hide()
        self.tela.TX_MMagenta.hide()
        self.tela.TX_MAmarelo.hide()
        self.tela.TX_MAzul.hide()