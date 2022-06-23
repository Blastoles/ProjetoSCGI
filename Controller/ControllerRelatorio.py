from Controller.ControllerMensagem import SistemaMensagem
from Controller.ControllerRContagem import SistemaGRelatorio
from View.ViewRelatorio import viewRelatorio
from DAO.DAORelatorio import DAORelatorio
from Model.ModelRelatorio import Modelrelatorio
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget



class SistemaRelatorio(QMainWindow):

    def Show(self):
        self.MostrarDados()
        self.ViewRela.Show()

    def Close(self):
        self.ViewRela.Close()

    def MostrarDados(self):
        filtro = self.Filtros()
        cond = []
        if filtro[0] == '':
            cond.append('NOT NULL')
        else:
            cond.append('=')
        if filtro[1] == '':
            cond.append('NOT NULL')
        else:
            cond.append('=')
        Lista = self.banco.BuscarDadosBD(filtro,cond)
        self.model.Tabela(Lista,self.ViewRela)

    def Filtros(self):
        filtro = []
        filtro.append(self.ViewRela.Status())
        filtro.append(self.ViewRela.Condicao())
        return filtro

    def Data(self):
        self.ViewRela.DataCheck()


    def GerarContagem(self):
        lista = self.ViewRela.ColetaDadosContagem()
        print(lista)
        self.GRela.Show()

    def Graf_Contagem(self):
        self.ViewRela.Grafico()


    def __init__(self):
        super().__init__()
        self.ViewRela = viewRelatorio()
        self.banco = DAORelatorio()
        self.msg = SistemaMensagem()
        self.model = Modelrelatorio()
        self.GRela = SistemaGRelatorio()
        self.ViewRela.tela.BT_GerarContagem.clicked.connect(self.GerarContagem)
        self.ViewRela.tela.BT_DataInicial.clicked.connect(self.Data)
        self.ViewRela.tela.BT_DataFinal.clicked.connect(self.Data)
        self.ViewRela.tela.BT_TodosStatus.clicked.connect(self.MostrarDados)
        self.ViewRela.tela.BT_Funcionando.clicked.connect(self.MostrarDados)
        self.ViewRela.tela.BT_Desativada.clicked.connect(self.MostrarDados)
        self.ViewRela.tela.BT_TodosCond.clicked.connect(self.MostrarDados)
        self.ViewRela.tela.BT_Comprada.clicked.connect(self.MostrarDados)
        self.ViewRela.tela.BT_Alugada.clicked.connect(self.MostrarDados)
        self.ViewRela.tela.BT_Voltar.clicked.connect(self.Close)
        self.ViewRela.tela.Graf_Contagem.clicked.connect(self.Graf_Contagem)

