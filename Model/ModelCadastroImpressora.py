## Classe de manipulação de dado ##
class ModelCadastroImpressora():

    ## Trata setor ##
    def TratarSetor(self,setor):
        lista = []
        for i in setor:
            lista.append(i)
        return lista

    ## Trata inteiro para escrita ##
    def TratarConvert(self,dados):
        n = 0
        Dados = []
        for i in dados:
            if i == 1:
                Dados.append(-1)
                n += 1
            else:
                Dados.append(i)
                n += 1
        return Dados

    ## Trata escrita para inteiro ##
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
