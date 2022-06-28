## Classe de manipulação de dado ##
class ModelContagemImpressora():

    ## Trata lista ##
    def TratarLista(self,lista):
        n = 0
        Lst = []
        for i in lista:
            lst = i
            n += 1
            lst = ' -- '.join(lst)
            Lst.append(lst)
        return Lst

    ## Trata dados da tabela ##
    def Tabela(self, imp, lista):
        self = imp
        self.tela.TB_Contagem.clearContents()
        n = 0
        ContImpre = 0
        nLista = len(lista)
        self.tela.TB_Contagem.setRowCount(nLista)
        for i in range(0, nLista):
            for j in range(0, 14):
                if j < 6:
                    self.Lista(i, j, str(lista[i][j]))
                if j == 5:
                    if i == 0:
                        ContImpre = 0
                    else:
                        ContImpre = lista[i-1][j] - lista[i][j]
                    self.Lista(i, j + 1,str(ContImpre))
                else:
                    self.Lista(i, j + 1, str(lista[i][j]))
                n += 1
