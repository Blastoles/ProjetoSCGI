## Classe de manipulação de dado ##
class ModelRContagem():

    ## Trata dados da tabela ##
    def Tabela(self, GRela, lista):
        self = GRela
        self.tela.TB_Contagem.clearContents()
        n = 0
        ContImpre = 0
        nLista = len(lista)
        self.tela.TB_Contagem.setRowCount(nLista)
        for i in range(0, nLista):
            for j in range(0, 3):
                if j == 1:
                    self.Lista(i, j, str(lista[i][j]))
                    if i == nLista-1:
                        self.Lista(i, j+2, str("Dado de Comparação"))
                    else:
                        self.Lista(i, j+2, str(lista[i][j] - lista[i + 1][j]))
                else:
                    self.Lista(i, j, str(lista[i][j]))
                n += 1
