## Classe de manipulação de dado ##
class modelCadastroSetor():

    ## Trata escrita para inteiro ##
    def PrioridadeInt(self,dado):
        if dado == 'Normal':
            retorno = 0
        elif dado == 'Baixa':
            retorno = 1
        elif dado == 'Alta':
            retorno = 2
        elif dado == 'Urgente':
            retorno = 3
        else:
            retorno = -1
        return retorno

    ## Trata inteiro para escrita ##
    def PrioridadeStr(self,dado):
        if dado == 0:
            retorno = 'Normal'
        elif dado == 1:
            retorno = 'Baixo'
        elif dado == 2:
            retorno = 'Alta'
        elif dado == 3:
            retorno = 'Urgente'
        else:
            retorno = -1
        return retorno
