import bcrypt

class ModelCadastrouser():

    def EsconderSenha(self,senha):
        Hash = bcrypt.hashpw(senha.encode('utf8'), bcrypt.gensalt())
        Hashen = Hash.decode('utf8')
        return Hashen
