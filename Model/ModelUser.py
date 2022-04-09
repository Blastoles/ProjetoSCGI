from PyQt5 import uic, QtWidgets


class Modeluser():

    def Tabela(self,user,lista):
        self = user
        self.tela.TB_Cadastro.clearContents()
        nLista = len(lista)
        self.tela.TB_Cadastro.setRowCount(nLista)
        for i in range(0, nLista):
            for j in range(0, 5):
                if j == 4:
                    if lista[i][j] == 1:
                        self.tela.TB_Cadastro.setItem(i, j, QtWidgets.QTableWidgetItem(str("Ativo")))
                    else:
                        self.tela.TB_Cadastro.setItem(i, j, QtWidgets.QTableWidgetItem(str("Desativado")))
                else:
                    self.Lista(i,j,str(lista[i][j]))
