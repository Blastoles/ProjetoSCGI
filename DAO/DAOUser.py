import sqlite3


class DAOuser():
    def Pesquisa(self,texto):
        banco = sqlite3.connect('db_contator.db')
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT "
                           "NOME,"
                           "USUARIO,"
                           "EMAIL,"
                           "TELEFONE,"
                           "ATIVO "
                           "FROM "
                           "USUARIO "
                           "WHERE "
                           "NOME LIKE '%{}%' "
                           "OR "
                           "USUARIO LIKE '%{}%' "
                           "OR "
                           "EMAIL LIKE '%{}%' "
                           "OR "
                           "TELEFONE LIKE '%{}%'"
                           "".format(texto,texto,texto,texto))
            lista = cursor.fetchall()
        except:
            print()
            # Mensagem Erro
        banco.close()
        return lista
