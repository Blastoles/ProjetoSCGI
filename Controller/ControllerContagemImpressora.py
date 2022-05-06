from View.ViewContagemImpressora import viewContagem


class SistemaContagem():
    def Show(self):
        self.contagem.Show()

    def Close(self):
        self.contagem.Close()

    def __init__(self):
        self.contagem = viewContagem()
        self.contagem.tela.BT_Voltar.clicked.connect(self.Close)
        #self.contagem.tela.BT_Pesquisar.clicked.connect(self.PesquisarCadastro)
        #self.contagem.tela.BT_Criar.clicked.connect(self.Criar)
        #self.contagem.tela.BT_Alterar.clicked.connect(self.AlterarCadastro)
        #self.contagem.tela.BT_Exclui.clicked.connect(self.ExcluirSetor)
"""
    def PesquisarCadastro(self):
        texto = self.viewSetor.Dados()
        lista = self.banco.Pesquisa(texto)
        self.model.Tabela(self.viewSetor,lista)

    def Criar(self):
        self.CSetor.Show('Criar',self)

    def AlterarCadastro(self):
        linhaSelect = self.viewSetor.LinhaSelect()
        if linhaSelect != -1:
            TextoLinha = self.viewSetor.TextoSelectLinha(linhaSelect)
            DadosUser = self.banco.LocalizarSetor(TextoLinha)
            self.CSetor.Show('Alterar', self)
            self.CSetor.MostrarDados(DadosUser)
        else:
            self.msg.MsgSelecionarLinha()

    def Tabela(self):
        lista = self.banco.TodaLista()
        self.model.Tabela(self.viewSetor,lista)

    def ExcluirSetor(self):
        linhaSelect = self.viewSetor.LinhaSelect()
        if linhaSelect != -1:
            self.conf.Show(self,linhaSelect)
        else:
            self.msg.MsgSelecionarLinha()

    def ExcluirConfirmado(self,linhaSelect):
        TextoLinha = self.viewSetor.TextoSelectLinha(linhaSelect)
        self.banco.ExcluirSetor(TextoLinha)
        self.Tabela()
"""
