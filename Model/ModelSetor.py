from PyQt5 import QtWidgets

class ModelSetor():

    def Tabela(self,setor,lista):
        self = setor
        self.tela.TB_Setor.clearContents()
        nLista = len(lista)
        self.tela.TB_Setor.setRowCount(nLista)
        for i in range(0, nLista):
            for j in range(0, 4):
                if j == 2:
                    if lista[i][j] == 0:
                        self.tela.TB_Setor.setItem(i, j, QtWidgets.QTableWidgetItem(str("Normal")))
                    elif lista[i][j] == 1:
                        self.tela.TB_Setor.setItem(i, j, QtWidgets.QTableWidgetItem(str("Baixa")))
                    elif lista[i][j] == 2:
                        self.tela.TB_Setor.setItem(i, j, QtWidgets.QTableWidgetItem(str("Alta")))
                    elif lista[i][j] == 3:
                        self.tela.TB_Setor.setItem(i, j, QtWidgets.QTableWidgetItem(str("Urgente")))
                    else:
                        self.tela.TB_Setor.setItem(i, j, QtWidgets.QTableWidgetItem(str("Não Específico")))
                else:
                    self.Lista(i,j,str(lista[i][j]))
