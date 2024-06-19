from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Produtos(db.Model):
    __tablename__ = 'produtos'

    def to_dict(self):
        return {
            'codigo': self.codigo,
            'nome': self.nome,
            'detalhes': self.detalhes,
            'minimoEstoque': self.minimoEstoque,
            'atualEstoque': self.atualEstoque,
            'custoProduto': round(self.custoProduto, 2),
            'vendaValor': round(self.vendaValor, 2),
            'dataCadastro': self.dataCadastro,
            'codcategoria': self.codcategoria,
            'codFornecedor': self.codFornecedor,
        }

    codigo = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    detalhes = db.Column(db.String(200))
    minimoEstoque = db.Column(db.Integer())
    atualEstoque = db.Column(db.Integer())
    custoProduto = db.Column(db.Float(8, 2), nullable=False)
    vendaValor = db.Column(db.Float(8, 2), nullable=False)
    dataCadastro = db.Column(db.String(100))
    codcategoria = db.Column(db.Integer, ForeignKey('categorias.codigo'))
    codFornecedor = db.Column(db.Integer, ForeignKey('fornecedores.codigo'))

    categoria_relacionado = relationship('Categorias', backref='produtos')
    fornecedor_relacionado = relationship('Fornecedores', backref='produtos')

    def __init__(self, nome, detalhes, minimoEstoque, atualEstoque, custoProduto, vendaValor, dataCadastro, codcategoria=None, codFornecedor=None):
        self.nome = nome
        self.detalhes = detalhes
        self.minimoEstoque = minimoEstoque
        self.atualEstoque = atualEstoque
        self.custoProduto = custoProduto
        self.vendaValor = vendaValor
        self.dataCadastro = dataCadastro
        self.codcategoria = codcategoria
        self.codFornecedor = codFornecedor
