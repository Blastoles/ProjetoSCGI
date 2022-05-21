from Controller.ControllerMensagem import SistemaMensagem
from View.ViewRelatorio import viewRelatorio
from DAO.DAORelatorio import DAORelatorio
from Model.ModelRelatorio import Modelrelatorio

class SistemaRelatorio():

    def Show(self):
        self.MostrarDados()
        self.ViewRela.Show()

    def Close(self):
        self.ViewRela.Close()

    def MostrarDados(self):
        Lista = self.banco.BuscarDadosBD()
        self.model.Tabela(Lista,self.ViewRela)

    def __init__(self):
        self.ViewRela = viewRelatorio()
        self.banco = DAORelatorio()
        self.msg = SistemaMensagem()
        self.model = Modelrelatorio()
        self.ViewRela.tela.BT_Voltar.clicked.connect(self.Close)