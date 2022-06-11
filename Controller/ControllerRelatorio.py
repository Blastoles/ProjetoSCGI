from Controller.ControllerMensagem import SistemaMensagem
from View.ViewRelatorio import viewRelatorio
from DAO.DAORelatorio import DAORelatorio
from Model.ModelRelatorio import Modelrelatorio

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import pandas as pd
import numpy as np


class SistemaRelatorio():

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

    def Tabela(self):
        self.ViewRela.TabelaCheck()

    def GerarContagem(self):
        lista = self.ViewRela.ColetaDadosContagem()

    def __init__(self):
        self.ViewRela = viewRelatorio()
        self.banco = DAORelatorio()
        self.msg = SistemaMensagem()
        self.model = Modelrelatorio()
        self.ViewRela.tela.BT_GerarContagem.clicked.connect(self.GerarContagem)
        self.ViewRela.tela.BT_TodasImpressoras.clicked.connect(self.Tabela)
        self.ViewRela.tela.BT_DataInicial.clicked.connect(self.Data)
        self.ViewRela.tela.BT_DataFinal.clicked.connect(self.Data)
        self.ViewRela.tela.BT_TodosStatus.clicked.connect(self.MostrarDados)
        self.ViewRela.tela.BT_Funcionando.clicked.connect(self.MostrarDados)
        self.ViewRela.tela.BT_Desativada.clicked.connect(self.MostrarDados)
        self.ViewRela.tela.BT_TodosCond.clicked.connect(self.MostrarDados)
        self.ViewRela.tela.BT_Comprada.clicked.connect(self.MostrarDados)
        self.ViewRela.tela.BT_Alugada.clicked.connect(self.MostrarDados)
        self.ViewRela.tela.BT_Voltar.clicked.connect(self.Close)
