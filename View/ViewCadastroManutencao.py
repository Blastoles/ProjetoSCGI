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
        self.tela.CP_Tipo.currentText()
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
        dados.append(self.tela.CP_Voltou.isChecked())
        dados.append(self.tela.CP_NVoltou.isChecked())
        dados.append(self.tela.CP_DataVt.text())
        return dados

    def PegarImpressora(self):
        check = self.tela.Info_Num.text()
        return check

    def Close(self):
        self.tela.close()

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\CadastroManutencao.ui".format(Local))

"""
    def LimpeTela(self):
        self.tela.CP_Impressora.setDisabled(False)
        self.tela.BT_Selecionar.setDisabled(False)
        self.tela.CP_Contagem.setText('')
        self.tela.CP_Data.setText('')
        self.tela.CP_CPreto.setText('')
        self.tela.CP_CMargenta.setText('')
        self.tela.CP_CAmarelo.setText('')
        self.tela.CP_CAzul.setText('')
        self.tela.CP_UltimaContagem.setText('')

    def ColocarDados(self,dados):
        self.tela.CP_Impressora.setDisabled(True)
        self.tela.BT_Selecionar.setDisabled(True)
        self.tela.CP_ID.setText(str(dados[0][0]))
        self.tela.CP_Contagem.setText(str(dados[0][2]))
        self.tela.CP_Data.setText(str(dados[0][3]))
        self.tela.CP_CPreto.setText(str(dados[0][4]))
        self.tela.CP_CMargenta.setText(str(dados[0][5]))
        self.tela.CP_CAmarelo.setText(str(dados[0][6]))
        self.tela.CP_CAzul.setText(str(dados[0][7]))

"""