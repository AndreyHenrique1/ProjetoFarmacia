from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Produto(db.Model):

    def to_dict(self):
        return {
            'codigo': self.codigo,
            'nome':self.nome,
            'detalhes':self.detalhes,
            'minimo_estoque':self.minimo_estoque,
            'atual_estoque': self.atual_estoque,
            'custo_valor':self.custo_valor,
            'venda_valor':self.venda_valor,
            'data_cadastro':self.data_cadastro,
            'codcategoria':self.codcategoria
        }

    codigo = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    detalhes = db.Column(db.String(100))
    minimo_estoque = db.Column(db.Integer(100))
    atual_estoque = db.Column(db.Integer(100))
    custo_valor = db.Column(db.float(8,2))
    venda_valor = db.Column(db.float(8,2))
    data_cadastro = db.Column(db.String(100))
    codcategoria = db.Column(ForeignKey('categorias.codigo'))

    codcategoria = relationship('Categoria', backref='Produto')

    def __init__(self, nome, detalhes, minimo_estoque, atual_estoque, custo_valor, venda_valor, data_cadastro, codcategoria):
        self.nome = nome
        self.detalhes = detalhes
        self.minimo_estoque = minimo_estoque
        self.atual_estoque = atual_estoque
        self.custo_valor = custo_valor
        self.venda_valor = venda_valor
        self.data_cadastro = data_cadastro
        self.codcategoria = codcategoria