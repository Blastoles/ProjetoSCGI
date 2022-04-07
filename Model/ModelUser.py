from PyQt5 import uic, QtWidgets
from View.ViewUser import viewUser

class Modeluser():
    def Tabela(self,lista):
        nLista = len(lista)
        self.viewuser.tela.TB_Cadastro.setRowCount(nLista)
        for i in range(0, nLista):
            for j in range(0, 5):
                if j == 4:
                    if lista[i][j] == 1:
                        self.viewuser.tela.TB_Cadastro.setItem(i, j, QtWidgets.QTableWidgetItem(str("Ativo")))
                    else:
                        self.viewuser.tela.TB_Cadastro.setItem(i, j, QtWidgets.QTableWidgetItem(str("Desativado")))
                else:
                    self.viewuser.tela.TB_Cadastro.setItem(i, j, QtWidgets.QTableWidgetItem(str(lista[i][j])))

    def __init__(self):
        self.viewuser = viewUser()