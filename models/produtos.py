from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Produtos(db.Model):

    def to_dict(self):
        return {
            'codigo': self.codigo,
            'nome':self.nome,
            'detalhes':self.detalhes,
            'minimoEstoque':self.minimoEstoque,
            'atualEstoque': self.atualEstoque,
            'custoProduto':self.custoProduto,
            'vendaValor':self.vendaValor,
            'dataCadastro':self.dataCadastro,
            'codproduto':self.codproduto
        }

    codigo = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    detalhes = db.Column(db.String(100))
    minimoEstoque = db.Column(db.Integer())
    atualEstoque = db.Column(db.Integer())
    custoProduto = db.Column(db.Float(8,2), nullable=False)
    vendaValor = db.Column(db.Float(8,2), nullable=False)
    dataCadastro = db.Column(db.String(100))
    codproduto = db.Column(ForeignKey('produtos.codigo'))

    codproduto = relationship('Produtos', backref='Produtos')

    def __init__(self, nome, detalhes, minimoEstoque, atualEstoque, custoProduto, vendaValor, dataCadastro, codproduto):
        self.nome = nome
        self.detalhes = detalhes
        self.minimoEstoque = minimoEstoque
        self.atualEstoque = atualEstoque
        self.custoProduto = custoProduto
        self.vendaValor = vendaValor
        self.dataCadastro = dataCadastro
        self.codproduto = codproduto