## Bibliotecas ##
from os import getcwd
from collections import OrderedDict
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *

## Classe visualização da tela ##
class viewRelatorio(QWidget):

    ## Chama a tela ##
    def Show(self):
        self.tela.show()

    ## Fecha a tela ##
    def Close(self):
        self.tela.close()

    ## Coleta o status ##
    def Status(self):
        if self.tela.BT_TodosStatus.isChecked():
            return ''
        elif self.tela.BT_Funcionando.isChecked():
            return '1'
        elif self.tela.BT_Desativada.isChecked():
            return '0'

    ## Coleta condição ##
    def Condicao(self):
        if self.tela.BT_TodosCond.isChecked():
            return ''
        elif self.tela.BT_Comprada.isChecked():
            return '0'
        elif self.tela.BT_Alugada.isChecked():
            return '1'

    ## Mostra lista ##
    def Lista(self,i,j,texto):
        self.tela.TB_Impressora.setItem(i, j, QtWidgets.QTableWidgetItem(texto))

    ## Mostra lista ##
    def ListaManu(self,lista):
        self.tela.CB_Impressora.clear()
        self.tela.CB_Impressora.addItem("Escolha uma Impressora")
        self.tela.CB_Impressora.addItems(lista)

    ## Mostra lista ##
    def ListaManuInfo(self,lista):
        self.tela.CB_Manutencao.clear()
        self.tela.CB_Manutencao.addItem("Escolha qual Manutenção")
        self.tela.CB_Manutencao.addItems(lista)

    ## Habilita opção na tela ##
    def DataCheck(self):
        if self.tela.BT_DataInicial.isChecked():
            self.tela.CP_DataInicial.setDisabled(False)
        else:
            self.tela.CP_DataInicial.setDisabled(True)
        if self.tela.BT_DataFinal.isChecked():
            self.tela.CP_DataFinal.setDisabled(False)
        else:
            self.tela.CP_DataFinal.setDisabled(True)

    ## Coleta dados da tela ##
    def ColetaDadosContagem(self):
        lst = []
        for LinhasSelecionadas in self.tela.TB_Impressora.selectedIndexes():
            lst.append(self.tela.TB_Impressora.item(LinhasSelecionadas.row(), 0).text())
        return (list(OrderedDict.fromkeys(lst)))

    ## Coleta Dado da Tela ##
    def PegarSelecaoImp(self):
        imp = self.tela.CB_Impressora.currentText()
        return imp

    ## Coleta Dado da Tela ##
    def PegarSelecaoManu(self):
        manu = self.tela.CB_Manutencao.currentText()
        return manu

    ## Coloca Dado ##
    def ColocarDdManu(self,campos):
        self.tela.CP_Data.setText(campos[0])
        self.tela.CP_Custo.setText(campos[1])
        if campos[2] == 1:
            self.tela.CP_Tipo.setText("Manutenção Preventiva")
        elif campos[2] == 2:
            self.tela.CP_Tipo.setText("Manutenção Corretiva")
        if campos[3] == 0:
            self.tela.CP_Status.setText("Não voltou funcionar")
        elif campos[3] == 1:
            self.tela.CP_Status.setText("Voltou funcionar")
        self.tela.CP_Quantidade.setText(str(campos[4]))
        self.tela.CP_Desc.setText(campos[5])

    ## Limpa tela ##
    def LimpaDdManu(self):
        self.tela.CP_Data.setText("")
        self.tela.CP_Custo.setText("")
        self.tela.CP_Tipo.setText("")
        self.tela.CP_Status.setText("")
        self.tela.CP_Quantidade.setText("")
        self.tela.CP_Desc.setText("")

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:', 'C:\\')
        self.tela = uic.loadUi("{}View\Telas\CD_Relatorio.ui".format(Local))
