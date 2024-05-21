from database.db import db

class Categorias(db.Model):
    
    def to_dict(self):
        return {
            'codigo': self.codigo,
            'nome': self.nome,
            'descricao': self.descricao

        }

    codigo = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.String(100))

    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao