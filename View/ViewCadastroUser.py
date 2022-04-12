from PyQt5 import uic, QtWidgets


class viewCadastroUser():
    def Show(self):
        self.tela.show()

    def Close(self):
        self.tela.close()

    def Aviso(self):
        self.tela.TX_Aviso.setText("Falta informações\nInsira todas as informações")

    def Duplicidade(self):
        self.tela.TX_Aviso.setText("Já existe um usuário cadastrado com esse usuário!!")

    def LimparDados(self):
        self.tela.CP_Nome.setText("")
        self.tela.CP_Email.setText("")
        self.tela.CP_Telefone.setText("")
        self.tela.CP_Usuario.setText("")
        self.tela.CP_Senha.setText("")
        self.tela.CP_Administrador.setCheckState(0)
        self.tela.CP_Ativo.setCheckState(-1)
        self.tela.TX_Aviso.setText("")

    def ColetaDados(self):
        Nome = self.tela.CP_Nome.text().upper()
        Email = self.tela.CP_Email.text()
        Telefone = self.tela.CP_Telefone.text()
        Usuario = self.tela.CP_Usuario.text().upper()
        Senha = self.tela.CP_Senha.text()
        Admin = self.tela.CP_Administrador.isChecked()
        Ativo = self.tela.CP_Ativo.isChecked()
        lista = [Nome,Email,Telefone,Usuario,Senha,Admin,Ativo]
        return lista

    def __init__(self):
        self.tela = uic.loadUi(".\View\Telas\CadastroUsuario.ui")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    CadastroUser = viewCadastroUser()

    # Show das telas
    CadastroUser.tela.show()
    sys.exit(app.exec())
