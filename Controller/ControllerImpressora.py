from PyQt5 import uic, QtWidgets

from Model.ModelImpressora import ModelImpressora
from View.ViewImpressora import viewImpressora
from DAO.DAOImpressora import DAOimpressora
from Controller.ControllerMensagem import SistemaMensagem
from Controller.ControllerCadastroImpressora import SistemaCadastroImpressora

class SistemaImpressora():
    def Show(self):
        self.impressora.Show()
        self.Tabela()

    def Close(self):
        self.impressora.Close()

    def Tabela(self):
        lista = self.banco.TodaLista()
        self.model.Tabela(self.impressora,lista)

    def PesquisarImpressora(self):
        print('PesquisarImpressora')

    def Criar(self):
        self.cdimpressora.Show('Incluir',self)

    def AlterarImpressora(self):
        linhaSelect = self.impressora.LinhaSelect()
        if linhaSelect != -1:
            TextoLinha = self.impressora.TextoSelectLinha(linhaSelect)
            DadosUser = self.banco.LocalizarImp(TextoLinha)
            self.cdimpressora.Show('Alterar', self)
            self.cdimpressora.MostrarDados(DadosUser)
        else:
            self.msg.MsgSelecionarLinha()

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
        self.cdimpressora = SistemaCadastroImpressora()
        self.model = ModelImpressora()
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
