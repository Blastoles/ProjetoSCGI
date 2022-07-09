## Classe de manipulação de dado ##
class Modelrelatorio():

    ## Trata dados da tabela ##
    def Tabela(self,lista,Tela):
        self = Tela
        nLista = len(lista)
        self.tela.TB_Impressora.clearContents()
        self.tela.TB_Impressora.setRowCount(nLista)
        LtManu = []
        linhaManu = ''
        for i in range(0,nLista):
            for j in range(0,6):
                if j == 4:
                    if lista[i][j] == 1:
                        self.Lista(i, j, "Funcionando")
                        linhaManu = linhaManu + " -- Funcionando"
                    else:
                        self.Lista(i, j, "Desativada")
                        linhaManu = linhaManu + " -- Desativada"
                elif j == 5:
                    if lista[i][j] == 1:
                        self.Lista(i, j, "Alugada")
                        linhaManu = linhaManu + " -- Alugada"
                    else:
                        self.Lista(i, j, "Comprada")
                        linhaManu = linhaManu + " -- Comprada"
                else:
                    self.Lista(i, j, str(lista[i][j]))
                    if j == 0:
                        linhaManu = linhaManu + str(lista[i][j])
                    else:
                        linhaManu = linhaManu + " -- " + str(lista[i][j])
            LtManu.append(linhaManu)
            linhaManu = ''
        self.ListaManu(LtManu)
