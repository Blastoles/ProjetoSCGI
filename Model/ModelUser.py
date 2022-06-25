## Classe de manipulação de dado ##
class Modeluser():

    ## Manipula o dado da tabela para ser exibido ##
    def Tabela(self,user,lista):
        self = user
        self.tela.TB_Cadastro.clearContents()
        nLista = len(lista)
        self.tela.TB_Cadastro.setRowCount(nLista)
        for i in range(0, nLista):
            for j in range(0, 5):
                if j == 4:
                    if lista[i][j] == 1:
                        self.Lista(i, j, str("Ativo"))
                    else:
                        self.Lista(i, j, str("Desativado"))
                else:
                    self.Lista(i,j,str(lista[i][j]))
