


class ModelCadastrarContagem():
    def TratarLista(self,lista):
        n = 0
        Lst = []
        for i in lista:
            lst = i
            n += 1
            lst = ' -- '.join(lst)
            Lst.append(lst)
        return Lst
