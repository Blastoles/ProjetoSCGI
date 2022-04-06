from View.ViewLogin import viewLogin

class modelLogin():

    def PuxaDados(self):
        user,senha = viewLogin.Dados(self)
        print(user,senha)