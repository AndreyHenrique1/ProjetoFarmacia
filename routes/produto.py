from flask import Blueprint, render_template, request
from database.produto import PRODUTOS
from models.produtos import Produtos
from database.db import db

produto_route = Blueprint('produto', __name__, template_folder='../../front-end/templates/Pasta_Produtos')

@produto_route.route('/')
def produto():
    return render_template("produtos.html")

@produto_route.route('/listas')
def lista_produtos():
    # Listar todos os produtos
    produtos = Produtos.query.all()

    return render_template("lista_produto.html", produtos=[produto.to_dict() for produto in produtos])


@produto_route.route('/', methods=['POST'])
def inserir_produtos():
    #Inserir produtos

    data = request.get_json()

    novo_produto = Produtos(
        nome = data['nome'],
        detalhes =  data['detalhes'],
        minimoEstoque =  data['minimoEstoque'],
        atualEstoque =  data['atualEstoque'],
        custoProduto =  data['custoProduto'],
        valorVenda =  data['valorVenda'],
        dataCadastro =  data['dataCadastro'],
    )

    # Adicionar um novo produto ao banco de dados
    db.session.add(novo_produto)
    db.session.commit()

    PRODUTOS.append(novo_produto)

    return render_template('item_produto.html', categoria=novo_produto)

@produto_route.route('/new')
def form_produtos():
    #Formulario para cadastrar um produto
    return render_template("form_produtos.html")

@produto_route.route('/<int:produto_codigo>')
def detalhe_produto(produto_codigo):
    #Exibir detalhes de um produto

    # O codigo abaixo é um exemplo sem um banco de dados
    #produto = list(filter(lambda i: i['codigo'] == produto_codigo, PRODUTOS)) [0]

    produto = Produtos.query.filter_by(codigo=produto_codigo).first()

    return render_template("detalhes_produtos.html", produto=produto)


@produto_route.route('/<int:produto_codigo>/edit')
def form_edit_produto(produto_codigo):
    #Formulario para editar a produto
    produto = None

    # O codigo abaixo é um exemplo para ser usado caso não tenha um banco de dados
    '''for i in PRODUTOS:
        if i['codigo'] == produto_codigo:
            produto = i'''
    
    produto = Produtos.query.filter_by(codigo=produto_codigo).first()
    return render_template("form_produtos.html", produto=produto)

@produto_route.route('/<int:produto_codigo>/update', methods=['PUT'])
def atualizar_produto(produto_codigo):
    #Formulario para atualizar um produto

    data = request.json

    produto_editado = Produtos.query.filter_by(codigo=produto_codigo).first()
    produto_editado.nome = data['nome']
    produto_editado.detalhes = data['detalhes']
    produto_editado.minimoEstoque = data['minimoEstoque']
    produto_editado.atualEstoque = data['atualEstoque']
    produto_editado.custoProduto = data['custoProduto']
    produto_editado.vendaValor = data['vendaValor']
    produto_editado.dataCadastro = data['dataCadastro']
    db.session.commit()

    
    # O codigo abaixo é para ser usado sem um banco de dados
    '''#obter produto pelo id
    for i in PRODUTOS:
        if i['codigo'] == categoria_codigo:
            i['nome'] = data['nome']
            i['detalhes'] = data['detalhes']
            i['minimoEstoque'] = data['minimoEstoque']
            i['atualEstoque'] = data['atualEstoque']
            i['custoProduto'] = data['custoProduto']
            i['vendaValor'] = data['vendaValor']
            i['dataCadastro'] = data['dataCadastro']

            produto_editado = i'''

    #editar produto
    return render_template('item_produto.html', produto=produto_editado)

@produto_route.route('/<int:produto_codigo>/delete', methods=['DELETE'])
def deletar_produto(produto_codigo):
    #Deletar produto

    # O codigo abaixo é para ser usado sem um banco de dados
    '''global PRODUTOS
    PRODUTOS = [ i for i in PRODUTOS if i['codigo'] != produto_codigo ]'''

    produto = Produtos.query.filter_by(codigo=produto_codigo).first()
    db.session.delete(produto)
    db.session.commit()

    return {"deleted":"ok"}