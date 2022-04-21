from PyQt5 import QtWidgets

class ModelSetor():

    def Tabela(self,setor,lista):
        self = setor
        self.tela.TB_Setor.clearContents()
        nLista = len(lista)
        self.tela.TB_Setor.setRowCount(nLista)
        for i in range(0, nLista):
            for j in range(0, 4):
                if j == 4:
                    if lista[i][j] == 1:
                        self.tela.TB_Setor.setItem(i, j, QtWidgets.QTableWidgetItem(str("Ativo")))
                    else:
                        self.tela.TB_Setor.setItem(i, j, QtWidgets.QTableWidgetItem(str("Desativado")))
                else:
                    self.Lista(i,j,str(lista[i][j]))
