from database.db import db

class Fornecedor(db.Model):

    def to_dict(self):
        return {
            'codigo': self.codigo,
            'nome':self.nome,
            'contato':self.contato,
            'endereco':self.endereco,
            'email': self.email
        }

    codigo = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    contato = db.Column(db.String(100))
    endereco = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, nome, contato, endereco, email):
        self.nome = nome
        self.contato = contato
        self.endereco = endereco
        self.email = email