from Controller.ControllerMensagem import SistemaMensagem
from View.ViewRelatorio import viewRelatorio
from DAO.DAORelatorio import DAORelatorio

class SistemaRelatorio():

    def Show(self):
        self.ViewRela.Show()

    def Close(self):
        self.ViewRela.Close()

    def MostrarDados(self):
        self.banco.BuscarDadosBD()

    def __init__(self):
        self.ViewRela = viewRelatorio()
        self.banco = DAORelatorio()
        self.msg = SistemaMensagem()
        self.ViewRela.tela.BT_Voltar.clicked.connect(self.Close)