## Bibliotecas ##
from os import getcwd
from PyQt5 import uic, QtWidgets

## Classe visualização da tela ##
class viewCadastroUser(QtWidgets):

    ## Chama a tela ##
    def Show(self):
        self.tela.show()

    ## Fecha a tela ##
    def Close(self):
        self.tela.close()

    ## Limpa os dados ##
    def LimparDados(self):
        self.tela.CP_Nome.setText("")
        self.tela.CP_Email.setText("")
        self.tela.CP_Telefone.setText("")
        self.tela.CP_Usuario.setText("")
        self.tela.CP_Senha.setText("")
        self.tela.CP_Administrador.setCheckState(0)
        self.tela.CP_Ativo.setCheckState(-1)
        self.tela.CP_Usuario.setDisabled(False)

    ## Coleta os dados da tela ##
    def ColetaDados(self):
        lista = []
        lista.append(self.tela.CP_Nome.text().upper())
        lista.append(self.tela.CP_Email.text())
        lista.append(self.tela.CP_Telefone.text())
        lista.append(self.tela.CP_Usuario.text().upper())
        lista.append(self.tela.CP_Senha.text())
        lista.append(self.tela.CP_Administrador.isChecked())
        lista.append(self.tela.CP_Ativo.isChecked())
        return lista

    ## Mostra dados na tela ##
    def ColocarDados(self,TextoLinha,box):
        self.tela.CP_Usuario.setDisabled(True)
        self.tela.CP_Nome.setText('{}'.format(TextoLinha[0][1]))
        self.tela.CP_Email.setText('{}'.format(TextoLinha[0][3]))
        self.tela.CP_Telefone.setText('{}'.format(TextoLinha[0][4]))
        self.tela.CP_Usuario.setText('{}'.format(TextoLinha[0][2]))
        self.tela.CP_Senha.setText('{:.20}'.format(TextoLinha[0][7]))
        self.tela.CP_Administrador.setCheckState(box[0])
        self.tela.CP_Ativo.setCheckState(box[1])

    ## Regras, Constante, e Ações ##
    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\CadastroUsuario.ui".format(Local))
