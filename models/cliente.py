from database.db import db

class Funcionario(db.Model):

    def to_dict(self):
        return {
            'nome':self.nome,
            'login':self.login,
            'senha':self.senha,
            'endereco':self.endereco,
            'idade':self.idade
        }

    codigo = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    login = db.Column(db.String(100))
    senha = db.Column(db.String(100))
    endereco = db.Column(db.String(100))
    idade = db.Column(db.Integer(3))


    def __init__(self,nome,login,senha,cargo,endereco,idade):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.endereco = endereco
        self.idade = idade