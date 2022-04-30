
class ModelCadastroImpressora():
    def TratarSetor(self,setor):
        lista = []
        for i in setor:
            lista.append(i)
        return lista

    def TratarInsert(self,dados):
        n = 0
        for i in dados:
            if i == True:
                dados[n] = 1
                n += 1
            elif i == False:
                dados[n] = 0
                n += 1
            else:
                n += 1
        return dados