## Bibliotecas ##
from os import getcwd
from PyQt5 import uic, QtWidgets

## Classe visualização da tela ##
class viewUser(QtWidgets):

    ## Chama a tela ##
    def Show(self):
        self.tela.show()

    ## Fecha a tela ##
    def Close(self):
        self.tela.close()

    ## Busca texto da tela ##
    def Dados(self):
        texto = str(self.tela.BR_Pesquisa.text())
        self.tela.BR_Pesquisa.setText("")
        return texto

    ## Preenche a tabela ##
    def Lista(self,i,j,texto):
        self.tela.TB_Cadastro.setItem(i, j, QtWidgets.QTableWidgetItem(texto))

    ## Coleta qual linha foi selecionada ##
    def LinhaSelect(self):
        linha = self.tela.TB_Cadastro.currentRow()
        return linha

    ## Coleta qual e o texto da linha selecionada ##
    def TextoSelectLinha(self,linhaSelect):
        TextoLinha = self.tela.TB_Cadastro.item(linhaSelect,1).text()
        return TextoLinha

    ## Regras, Constante, e Ações ##
    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\CD_Usuario.ui".format(Local))
