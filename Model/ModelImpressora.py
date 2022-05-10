from PyQt5 import QtWidgets

class ModelImpressora():

    def Tabela(self,impr,lista):
        self = impr
        self.tela.TB_Impressora.clearContents()
        nLista = len(lista)
        self.tela.TB_Impressora.setRowCount(nLista)
        for i in range(0, nLista):
            for j in range(0, 9):
                    self.Lista(i,j,str(lista[i][j]))
