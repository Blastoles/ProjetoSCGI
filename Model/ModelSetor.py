## Classe de manipulação de dado ##
class ModelSetor():

    ## Trata dados da tabela ##
    def Tabela(self,setor,lista):
        self = setor
        self.tela.TB_Setor.clearContents()
        nLista = len(lista)
        self.tela.TB_Setor.setRowCount(nLista)
        for i in range(0, nLista):
            for j in range(0, 4):
                if j == 2:
                    if lista[i][j] == 0:
                        self.Lista(i, j, str("Normal"))
                    elif lista[i][j] == 1:
                        self.Lista(i, j, str("Baixa"))
                    elif lista[i][j] == 2:
                        self.Lista(i, j, str("Alta"))
                    elif lista[i][j] == 3:
                        self.Lista(i, j, str("Urgente"))
                    else:
                        self.Lista(i, j, str("Não Específico"))
                else:
                    self.Lista(i,j,str(lista[i][j]))
