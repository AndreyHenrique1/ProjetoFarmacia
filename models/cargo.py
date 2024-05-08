from database.db import db

class Cargo(db.Model):
    def to_dict(self):
        return {
            'codigo': self.codigo,
            'nome': self.nome,
            'salario': self.salario

        }

    codigo = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    nome = db.Column(db.String(100))
    salario = db.Column(db.Float(100))

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario