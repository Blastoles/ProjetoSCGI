## Bibliotecas ##
from os import getcwd
from PyQt5 import uic,QtWidgets

## Classe visualização da tela ##
class viewCadastroContagem(QtWidgets):

    ## Chama a tela ##
    def Show(self):
        self.tela.show()

    ## Limpa lista ##
    def LimpeLista(self):
        self.tela.CP_Impressora.clear()
        self.tela.CP_Impressora.addItem("Selecione a Impressora")
        self.tela.CP_Impressora.setCurrentIndex(0)

    ## Limpa tela ##
    def LimpeTela(self):
        self.tela.CP_Impressora.setDisabled(False)
        self.tela.BT_Selecionar.setDisabled(False)
        self.tela.CP_Contagem.setText('')
        self.tela.CP_Data.setText('')
        self.tela.CP_CPreto.setValue(0.00)
        self.tela.CP_CMargenta.setValue(0.00)
        self.tela.CP_CAmarelo.setValue(0.00)
        self.tela.CP_CAzul.setValue(0.00)
        self.tela.CP_UltimaContagem.setText('')

    ## Limpa info ##
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
        self.tela.CP_UltimaContagem.setText('')

    ## Mostra infomação ##
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

    ## Mostra dados ##
    def ColocarDados(self,dados):
        self.tela.CP_Impressora.setDisabled(True)
        self.tela.BT_Selecionar.setDisabled(True)
        self.tela.CP_ID.setText(str(dados[0][0]))
        self.tela.CP_Contagem.setText(str(dados[0][2]))
        self.tela.CP_Data.setText(str(dados[0][3]))
        self.tela.CP_CPreto.setValue(float(dados[0][4].replace(",",".")))
        self.tela.CP_CMargenta.setValue(float(dados[0][5].replace(",",".")))
        self.tela.CP_CAmarelo.setValue(float(dados[0][6].replace(",",".")))
        self.tela.CP_CAzul.setValue(float(dados[0][7].replace(",",".")))

    ## Coleta impressora ##
    def ImprSelect(self):
        impr = self.tela.CP_Impressora.currentText()
        return impr

    ## Mostra impressora
    def ColocarImpressora(self,lista):
        self.tela.CP_Impressora.addItems(lista)

    ## Coleta impressora ##
    def PegarImpressora(self):
        check = self.tela.Info_Num.text()
        return check

    ## Coleta dados ##
    def ColetaDados(self):
        dados = []
        dados.append(self.tela.CP_Contagem.text())
        dados.append(self.tela.CP_Data.text())
        dados.append(self.tela.CP_CPreto.text())
        dados.append(self.tela.CP_CMargenta.text())
        dados.append(self.tela.CP_CAmarelo.text())
        dados.append(self.tela.CP_CAzul.text())
        dados.append(self.tela.CP_ID.text())
        return dados

    ## Fecha a tela ##
    def Close(self):
        self.tela.close()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\CadastroContagem.ui".format(Local))
