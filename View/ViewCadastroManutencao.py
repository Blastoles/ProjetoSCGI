from os import getcwd
from PyQt5 import uic

class viewCadastroManutencao():
    def Show(self):
        self.tela.show()

    def LimpeLista(self):
        self.tela.CP_Impressora.clear()
        self.tela.CP_Impressora.addItem("Selecione a Impressora")
        self.tela.CP_Impressora.setCurrentIndex(0)

    def LimpaInfo(self):
        self.tela.CP_ID.setText('')
        self.tela.Info_Num.setText('')
        self.tela.Info_Modelo.setText('')
        self.tela.Info_Amigavel.setText('')
        self.tela.Info_Setor.setText('')
        self.tela.Info_MPreto.setText('')
        self.tela.Info_MMargenta.setText('')
        self.tela.Info_MAmarelo.setText('')
        self.tela.Info_MAzul.setText('')

    def LimpaDado(self):
        self.tela.CP_Impressora.setDisabled(False)
        self.tela.BT_Selecionar.setDisabled(False)
        self.tela.CP_Tipo.setCurrentIndex(0)
        self.tela.CP_Data.setText('')
        self.tela.CP_Descricao.setText('')
        self.tela.CP_Custo.setValue(0.00)
        self.tela.CP_Voltou.setChecked(True)
        self.tela.CP_NVoltou.setChecked(False)
        self.tela.CP_DataVt.setText('')

    def ColocarImpressora(self,lista):
        self.tela.CP_Impressora.addItems(lista)

    def ImprSelect(self):
        impr = self.tela.CP_Impressora.currentText()
        return impr

    def ColocarInfo(self,dado):
        self.tela.Info_Num.setText(dado[0][0])
        self.tela.Info_Modelo.setText(dado[0][1])
        self.tela.Info_Amigavel.setText(dado[0][2])
        self.tela.Info_Setor.setText(dado[0][3])
        self.tela.Info_MPreto.setText(dado[0][4])
        self.tela.Info_MMargenta.setText(dado[0][5])
        self.tela.Info_MAmarelo.setText(dado[0][6])
        self.tela.Info_MAzul.setText(dado[0][7])

    def ColetarDados(self):
        dados = []
        dados.append(self.tela.CP_Tipo.currentText())
        dados.append(self.tela.CP_Data.text())
        dados.append(self.tela.CP_Descricao.toPlainText())
        dados.append(self.tela.CP_Custo.text())
        if self.tela.CP_Voltou.isChecked() == True:
            dados.append(1)
        elif self.tela.CP_NVoltou.isChecked() == True:
            dados.append(0)
        if self.tela.CP_NVoltou.isChecked() == True:
            dados.append('//')
        else:
            dados.append(self.tela.CP_DataVt.text())
        return dados

    def ColetaID(self):
        dado = []
        dado.append(self.tela.CP_ID.text())
        return dado

    def PegarImpressora(self):
        check = self.tela.Info_Num.text()
        return check

    def ColocarDados(self,dados):
        self.tela.CP_Impressora.setDisabled(True)
        self.tela.BT_Selecionar.setDisabled(True)
        self.tela.CP_ID.setText(str(dados[0][0]))
        self.tela.CP_Tipo.setCurrentIndex(dados[0][1]-1)
        self.tela.CP_Data.setText(dados[0][2])
        self.tela.CP_Descricao.setText(dados[0][3])
        self.tela.CP_Custo.setValue(float(dados[0][4].replace(",",".")))
        if dados[0][5] == 1:
            self.tela.CP_Voltou.setChecked(True)
            self.tela.CP_NVoltou.setChecked(False)
        else:
            self.tela.CP_Voltou.setChecked(False)
            self.tela.CP_NVoltou.setChecked(True)
        self.tela.CP_DataVt.setText(dados[0][6])

    def DataVtFuncionar(self):
        if self.tela.CP_NVoltou.isChecked() == True:
            self.tela.CP_DataVt.setDisabled(True)
        elif self.tela.CP_NVoltou.isChecked() == False:
            self.tela.CP_DataVt.setDisabled(False)


    def Close(self):
        self.tela.close()

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\CadastroManutencao.ui".format(Local))
