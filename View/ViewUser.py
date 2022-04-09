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

    def __init__(self):
        self.tela = uic.loadUi(".\View\Telas\CD_Usuario.ui")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    User = viewUser()

    # Show das telas
    User.tela.show()
    sys.exit(app.exec())
