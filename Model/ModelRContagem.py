## Classe de manipulação de dado ##
class ModelRContagem():

    ## Trata dados da tabela ##
    def Tabela(self, GRela, lista):
        self = GRela
        self.tela.TB_Contagem.clearContents()
        n = 0
        nLista = len(lista)
        self.tela.TB_Contagem.setRowCount(nLista)
        for i in range(0, nLista):
            for j in range(0, 3):
                if j != 2:
                    self.Lista(i, j, str(lista[i][j]))
                else:
                    self.Lista(i, j + 1, str(lista[i][j]))
                    if i != nLista-1:
                        self.Lista(i, j, str(lista[i][j - 1] - lista[i + 1][j - 1]))
                n += 1
