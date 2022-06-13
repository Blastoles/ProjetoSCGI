from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from Controller.ControllerConfirmacao import SistemaConfirmacao
from Model.ModelImpressora import ModelImpressora
from View.ViewImpressora import viewImpressora
from DAO.DAOImpressora import DAOimpressora
from Controller.ControllerMensagem import SistemaMensagem
from Controller.ControllerCadastroImpressora import SistemaCadastroImpressora

class SistemaImpressora(QMainWindow):
    def Show(self):
        self.impressora.Show()
        self.Tabela()

    def Close(self):
        self.impressora.Close()

    def Tabela(self):
        lista = self.banco.TodaLista()
        self.model.Tabela(self.impressora,lista)

    def PesquisarImpressora(self):
        texto = self.impressora.Dados()
        lista = self.banco.Pesquisa(texto)
        self.model.Tabela(self.impressora, lista)

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
        linhaSelect = self.impressora.LinhaSelect()
        if linhaSelect != -1:
            self.conf.Show(self, linhaSelect)
        else:
            self.msg.MsgSelecionarLinha()

    def ExcluirConfirmado(self,linhaSelect):
        TextoLinha = self.impressora.TextoSelectLinha(linhaSelect)
        self.banco.ExcluirImpr(TextoLinha)
        self.Tabela()


    def __init__(self):
        super().__init__()
        self.impressora = viewImpressora()
        self.msg = SistemaMensagem()
        self.banco = DAOimpressora()
        self.cdimpressora = SistemaCadastroImpressora()
        self.model = ModelImpressora()
        self.conf = SistemaConfirmacao()
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
