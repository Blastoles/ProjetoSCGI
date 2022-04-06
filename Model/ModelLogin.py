from View.ViewLogin import viewLogin
from DAO.DAOLogin import DAOlogin
import bcrypt

class modelLogin():

    def ValidarDaDo(self,user,senha):
        ValiUser = DAOlogin(self,user,senha)
