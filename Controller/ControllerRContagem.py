## Bibliotecas ##
from PyQt5.QtWidgets import QWidget
from DAO.DAORContagem import DAORContagem
from Model.ModelRContagem import ModelRContagem
from View.ViewRContagem import viewRContagem


## Classe principal ##
class SistemaRContagem(QWidget):

    ## Chama a tela ##
    def Show(self,Impressora):
        self.GRela.LimpaDados()
        self.imp = Impressora
        self.ChamaDados()
        self.ChamaContagem()
        self.GRela.Show()

    def ChamaDados(self):
        DadoImp = self.banco.BuscarDadosImp(self.imp)
        self.GRela.PreenchaDados(DadoImp[0])

    def ChamaContagem(self):
        DadoCont = self.banco.BuscarContagemImp(self.imp)
        self.model.Tabela(self.GRela,DadoCont)

    ## Fecha a tela ##
    def Close(self):
        self.GRela.Close()

    ## Regras, Constante, e Ações ##
    def __init__(self):
        super().__init__()
        self.GRela = viewRContagem()
        self.banco = DAORContagem()
        self.model = ModelRContagem()
        self.imp = ''
        #Definição dos botões
        self.GRela.tela.BT_Voltar.clicked.connect(self.Close)