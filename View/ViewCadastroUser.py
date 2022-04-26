from os import getcwd
from PyQt5 import uic, QtWidgets


class viewCadastroUser():
    def Show(self):
        self.tela.show()

    def Close(self):
        self.tela.close()

    def LimparDados(self):
        self.tela.CP_Nome.setText("")
        self.tela.CP_Email.setText("")
        self.tela.CP_Telefone.setText("")
        self.tela.CP_Usuario.setText("")
        self.tela.CP_Senha.setText("")
        self.tela.CP_Administrador.setCheckState(0)
        self.tela.CP_Ativo.setCheckState(-1)
        self.tela.CP_Usuario.setDisabled(False)

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

    def ColocarDados(self,TextoLinha,box):
        self.tela.CP_Usuario.setDisabled(True)
        self.tela.CP_Nome.setText('{}'.format(TextoLinha[0][1]))
        self.tela.CP_Email.setText('{}'.format(TextoLinha[0][3]))
        self.tela.CP_Telefone.setText('{}'.format(TextoLinha[0][4]))
        self.tela.CP_Usuario.setText('{}'.format(TextoLinha[0][2]))
        self.tela.CP_Senha.setText('{:.20}'.format(TextoLinha[0][7]))
        self.tela.CP_Administrador.setCheckState(box[0])
        self.tela.CP_Ativo.setCheckState(box[1])

    def __init__(self):
        Local = getcwd()
        Local = Local.split('Controller')
        Local = Local[0].replace('C:','C:\\')
        self.tela = uic.loadUi("{}View\Telas\CadastroUsuario.ui".format(Local))
