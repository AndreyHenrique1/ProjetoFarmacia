from database.db import db
from datetime import datetime

class DetalhesCarrinho(db.Model):
    __tablename__ = 'carrinho'

    codigo = db.Column(db.Integer, primary_key=True)
    codProduto = db.Column(db.Integer, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    valor_total = db.Column(db.Float, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    data = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __init__(self, email, produto_codigo, quantidade, valor_total):
        self.email = email
        self.produto_codigo = produto_codigo
        self.quantidade = quantidade
        self.valor_total = valor_total
