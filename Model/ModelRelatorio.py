
class Modelrelatorio():

    def Tabela(self,lista,Tela):
        self = Tela
        nLista = len(lista)
        self.tela.TB_Impressora.clearContents()
        self.tela.TB_Impressora.setRowCount(nLista)
        for i in range(0,nLista):
            for j in range(0,4):
                self.Lista(i, j, str(lista[i][j]))
