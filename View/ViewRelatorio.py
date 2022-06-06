from os import getcwd
from collections import OrderedDict
from PyQt5 import uic, QtWidgets



class viewRelatorio():
    def Show(self):
        self.tela.show()

    def Close(self):
        self.tela.close()

    def Status(self):
        if self.tela.BT_TodosStatus.isChecked():
            return ''
        elif self.tela.BT_Funcionando.isChecked():
            return '1'
        elif self.tela.BT_Desativada.isChecked():
            return '0'

    def Condicao(self):
        if self.tela.BT_TodosCond.isChecked():
            return ''
        elif self.tela.BT_Comprada.isChecked():
            return '0'
        elif self.tela.BT_Alugada.isChecked():
            return '1'

    def Lista(self,i,j,texto):
        self.tela.TB_Impressora.setItem(i, j, QtWidgets.QTableWidgetItem(texto))

    def DataCheck(self):
        if self.tela.BT_DataInicial.isChecked():
            self.tela.CP_DataInicial.setDisabled(False)
        else:
            self.tela.CP_DataInicial.setDisabled(True)
        if self.tela.BT_DataFinal.isChecked():
            self.tela.CP_DataFinal.setDisabled(False)
        else:
            self.tela.CP_DataFinal.setDisabled(True)

    def TabelaCheck(self):
        if self.tela.BT_TodasImpressoras.isChecked():
            self.tela.TB_Impressora.setDisabled(True)
        else:
            self.tela.TB_Impressora.setDisabled(False)

    def ColetaDadosContagem(self):
        if self.tela.BT_TodasImpressoras.isChecked():
            return []
        else:
            lst = []
            for LinhasSelecionadas in self.tela.TB_Impressora.selectedIndexes():
                lst.append(self.tela.TB_Impressora.item(LinhasSelecionadas.row(), 0).text())
            return (list(OrderedDict.fromkeys(lst)))


    def __init__(self):
            Local = getcwd()
            Local = Local.split('Controller')
            Local = Local[0].replace('C:', 'C:\\')
            self.tela = uic.loadUi("{}View\Telas\CD_Relatorio.ui".format(Local))

