## Classe de manipulação de dado ##
class ModelCadastrarManutencao():

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

    ## Trata escrita ##
    def TratarDados(self,dados):
        dado = []
        for i in dados:
            if i == "Manutenção Preventiva":
                dado.append(1)
            elif i == "Manutenção Corretiva":
                dado.append(2)
            else:
                dado.append(i)
        return dado