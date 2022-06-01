class ModelManutencao():
    def TratarLista(self,lista):
        n = 0
        Lst = []
        for i in lista:
            lst = i
            n += 1
            lst = ' -- '.join(lst)
            Lst.append(lst)
        return Lst

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
                        self.Lista(i, j, "Manutenção Corretiva")
                    if lista[i][j] == 2:
                        self.Lista(i, j, "Manutenção Preventiva")
                elif j == 8:
                    if lista[i][j] == 1:
                        self.Lista(i, j, str("Sim"))
                    if lista[i][j] == 0:
                        self.Lista(i, j, str("Não"))
                else:
                    self.Lista(i, j , str(lista[i][j]))
                n += 1