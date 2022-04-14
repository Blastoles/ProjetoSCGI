from PyQt5 import uic, QtWidgets
from View.ViewImpressora import viewImpressora
from DAO.DAOImpressora import DAOimpressora
from Controller.ControllerMensagem import SistemaMensagem


class SistemaImpressora():
    def Show(self):
        self.impressora.Show()

    def Close(self):
        self.impressora.Close()

    def Tabela(self):
        print('tabela')

    def PesquisarImpressora(self):
        print('PesquisarImpressora')

    def Criar(self):
        print('Criar')

    def AlterarImpressora(self):
        print('AlterarImpressora')

    def ExcluirImpressora(self):
        print('ExcluirImpressora')
        linhaSelect = self.impressora.LinhaSelect()
        if linhaSelect != -1:
            TextoLinha = self.impressora.TextoSelectLinha(linhaSelect)
            self.banco.ExcluirUser(TextoLinha)
            self.Tabela()
        else:
            self.msg.MsgSelecionarLinha()


    def __init__(self):
        self.impressora = viewImpressora()
        self.msg = SistemaMensagem()
        self.banco = DAOimpressora()

        #Definição dos botões
        self.impressora.tela.BT_Voltar.clicked.connect(self.Close)
        self.impressora.tela.BT_Pesquisar.clicked.connect(self.PesquisarImpressora)
        self.impressora.tela.BT_Criar.clicked.connect(self.Criar)
        self.impressora.tela.BT_Alterar.clicked.connect(self.AlterarImpressora)
        self.impressora.tela.BT_Exclui.clicked.connect(self.ExcluirImpressora)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    menu = ()

    # Show das telas
    menu.tela.show()
    sys.exit(app.exec())
