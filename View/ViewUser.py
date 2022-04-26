from os import getcwd
from PyQt5 import uic, QtWidgets


class viewUser():
    def Show(self):
        self.tela.show()

    def Close(self):
        self.tela.close()

    def Dados(self):
        texto = str(self.tela.BR_Pesquisa.text())
        self.tela.BR_Pesquisa.setText("")
        return texto

    def Lista(self,i,j,texto):
        self.tela.TB_Cadastro.setItem(i, j, QtWidgets.QTableWidgetItem(texto))

    def LinhaSelect(self):
        linha = self.tela.TB_Cadastro.currentRow()
        return linha

    def TextoSelectLinha(self,linhaSelect):
        TextoLinha = self.tela.TB_Cadastro.item(linhaSelect,1).text()
        return TextoLinha


    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\CD_Usuario.ui".format(Local))
        #self.tela = uic.loadUi(".\View\Telas\CD_Usuario.ui")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    User = viewUser()

    # Show das telas
    User.tela.show()
    sys.exit(app.exec())
