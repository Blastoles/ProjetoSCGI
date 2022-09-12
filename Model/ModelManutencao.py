## Classe de manipulação de dado ##
class ModelManutencao():

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
        self.tela.TB_Manutencao.clearContents()
        n = 0
        nLista = len(lista)
        self.tela.TB_Manutencao.setRowCount(nLista)
        for i in range(0, nLista):
            for j in range(0, 10):
                if j == 5:
                    if lista[i][j] == 1:
                        self.Lista(i, j, "Manutenção Preventiva")
                    if lista[i][j] == 2:
                        self.Lista(i, j, "Manutenção Corretiva")
                elif j == 8:
                    if lista[i][j] == 1:
                        self.Lista(i, j, str("Sim"))
                    if lista[i][j] == 0:
                        self.Lista(i, j, str("Não"))
                else:
                    self.Lista(i, j , str(lista[i][j]))
                n += 1

    ## Trata Motivo ##
    def Motivo(self,mot):
        dado = []
        for i in mot:
            if i == "Manutenção Preventiva":
                dado.append(1)
            elif i == "Manutenção Corretiva":
                dado.append(2)
            else:
                dado.append(i)
        return dado