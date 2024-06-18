import os
from flask import Blueprint, render_template, request, session, flash, redirect, url_for, current_app
from werkzeug.utils import secure_filename
from models.produtos import Produtos
from models.categorias import Categorias
from models.fornecedores import Fornecedores
from database.db import db

produto_route = Blueprint('produto', __name__, template_folder='../../front-end/templates/Pasta_Produtos')

@produto_route.route('/')
def produto():
    if 'email' not in session:
        redirect(url_for('login.login'))
    return render_template("produtos.html")

@produto_route.route('/listas')
def lista_produtos():
    produtos = Produtos.query.all()
    return render_template("lista_produto.html", produtos=[produto.to_dict() for produto in produtos])

@produto_route.route('/categorias')
def listar_categorias():
    categorias = Categorias.query.all()
    return [{'codigo': categoria.codigo, 'nome': categoria.nome} for categoria in categorias]

@produto_route.route('/fornecedores')
def listar_fornecedores():
    fornecedores = Fornecedores.query.all()
    return [{'codigo': fornecedor.codigo, 'nome': fornecedor.nome} for fornecedor in fornecedores]

@produto_route.route('/new')
def form_produtos():
    categorias = Categorias.query.all()
    fornecedores = Fornecedores.query.all()
    return render_template("form_produtos.html", categorias=categorias, fornecedores=fornecedores)

@produto_route.route('/', methods=['POST'])
def inserir_produtos():
    data = request.form
    file = request.files['imagem_produto']  # Nome correto do campo

    if file and file.filename != '':
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
    else:
        filename = None

    novo_produto = Produtos(
        nome=data['nome'],
        detalhes=data['detalhes'],
        minimoEstoque=data['minimoEstoque'],
        atualEstoque=data['atualEstoque'],
        custoProduto=data['custoProduto'],
        vendaValor=data['vendaValor'],
        dataCadastro=data['dataCadastro'],
        codcategoria=data.get('codcategoria'),
        codFornecedor=data.get('codFornecedor'),
        imagem_produto=filename  # Passando o nome do arquivo da imagem
    )

    db.session.add(novo_produto)
    db.session.commit()

    return render_template('item_produtos.html', produto=novo_produto.to_dict())

@produto_route.route('/<int:produto_codigo>')
def detalhe_produto(produto_codigo):
    produto = Produtos.query.filter_by(codigo=produto_codigo).first()
    return render_template("detalhes_produtos.html", produto=produto.to_dict())

@produto_route.route('/<int:produto_codigo>/edit')
def form_edit_produto(produto_codigo):
    produto = Produtos.query.filter_by(codigo=produto_codigo).first()
    categorias = Categorias.query.all()
    fornecedores = Fornecedores.query.all()
    return render_template("form_produtos.html", produto=produto.to_dict(), categorias=categorias, fornecedores=fornecedores)

@produto_route.route('/<int:produto_codigo>/update', methods=['POST'])
def atualizar_produto(produto_codigo):
    data = request.form
    produto_editado = Produtos.query.filter_by(codigo=produto_codigo).first()
    
    file = request.files['imagem_produto']  # Nome correto do campo
    if file and file.filename != '':
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        produto_editado.imagem_produto = filename

    produto_editado.nome = data['nome']
    produto_editado.detalhes = data['detalhes']
    produto_editado.minimoEstoque = data['minimoEstoque']
    produto_editado.atualEstoque = data['atualEstoque']
    produto_editado.custoProduto = data['custoProduto']
    produto_editado.vendaValor = data['vendaValor']
    produto_editado.dataCadastro = data['dataCadastro']
    produto_editado.codcategoria = data.get('codcategoria')
    produto_editado.codFornecedor = data.get('codFornecedor')

    db.session.commit()
    return render_template('item_produto.html', produto=produto_editado.to_dict())

@produto_route.route('/<int:produto_codigo>/delete', methods=['DELETE'])
def deletar_produto(produto_codigo):
    produto = Produtos.query.filter_by(codigo=produto_codigo).first()
    db.session.delete(produto)
    db.session.commit()

    return {"deleted": "ok"}
