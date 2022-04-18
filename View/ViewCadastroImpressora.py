from PyQt5 import uic,QtWidgets

class viewCadastroImpressora():

    def Show(self):
        self.tela.show()

    def Close(self):
        self.tela.close()

    def ColetaDados(self):
        lista = []
        lista.append(self.tela.CP_Num_Serie.text().upper())
        lista.append(self.tela.CP_MAC.text())
        lista.append(self.tela.CP_ModeloImpre.text())
        lista.append(self.tela.CP_Fabricante.text())
        lista.append(self.tela.CP_Nome.text())
        lista.append(self.tela.CP_Data.text())
        lista.append(self.tela.CP_Ativo.isChecked())
        lista.append(self.tela.CP_Terceiros.isChecked())
        lista.append(self.tela.CP_USB.isChecked())
        lista.append(self.tela.CP_Rede.isChecked())
        lista.append(self.tela.CP_Wifi.isChecked())
        lista.append(self.tela.CP_IP.text())
        lista.append(self.tela.CP_Preto.isChecked())
        lista.append(self.tela.CP_MPreto.text())
        lista.append(self.tela.CP_Color.isChecked())
        lista.append(self.tela.CP_MMagenta.text())
        lista.append(self.tela.CP_MAmarelo.text())
        lista.append(self.tela.CP_MAzul.text())
        print(lista)

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
        self.tela = uic.loadUi(".\View\Telas\CadastroImpressora.ui")
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