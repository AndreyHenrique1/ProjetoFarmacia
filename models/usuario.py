from database.db import db

class Usuario(db.Model): 

    def to_dict(self):
        return {
            'codigo': self.codigo,
            'nome':self.nome,
            'cpf':self.cpf,
            'endereco':self.endereco,
            'email':self.email,
            'senha':self.senha
        }

    codigo = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(100))
    endereco = db.Column(db.String(100))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(100))


    def __init__(self, nome, cpf, endereco, email, senha):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.email = email
        self.senha = senha