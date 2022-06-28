## Classe de manipulação de dado ##
class Modelrelatorio():

    ## Trata dados da tabela ##
    def Tabela(self,lista,Tela):
        self = Tela
        nLista = len(lista)
        self.tela.TB_Impressora.clearContents()
        self.tela.TB_Impressora.setRowCount(nLista)
        for i in range(0,nLista):
            for j in range(0,6):
                if j == 4:
                    if lista[i][j] == 1:
                        self.Lista(i, j, "Funcionando")
                    else:
                        self.Lista(i, j, "Desativada")
                elif j == 5:
                    if lista[i][j] == 1:
                        self.Lista(i, j, "Alugada")
                    else:
                        self.Lista(i, j, "Comprada")
                else:
                    self.Lista(i, j, str(lista[i][j]))
