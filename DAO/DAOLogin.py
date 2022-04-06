import sqlite3


class DAOlogin():

    def CheckUser(self,user):
        banco = sqlite3.connect('db_contator.db')
        cursor = banco.cursor()
        user_db = ''
        print(user,'usuario')
        try:
            cursor.execute("SELECT USUARIO FROM USUARIO WHERE USUARIO = '{}'".format(user))
            print('passou o cursor')
            user_db = cursor.fetchall()
            print(user_db,'teste')
        except:
            print()
            #Mensagem Erro
        banco.close()
        return user_db

    def CheckSenha(self,senha):
        banco = sqlite3.connect('db_contator.db')
        cursor = banco.cursor()
        senha_db = ''
        try:
            cursor.execute("SELECT SENHA FROM USUARIO WHERE SENHA = '{}'".format(senha))
            senha_db = cursor.fetchall()
        except:
            print()
            #Mensagem Erro
        banco.close()
        return senha_db