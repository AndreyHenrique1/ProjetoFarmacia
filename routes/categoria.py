from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from database.categoria import CATEGORIAS
from models.categorias import Categorias
from database.db import db

categoria_route = Blueprint('categoria', __name__, template_folder='../../front-end/templates/Pasta_categorias')

@categoria_route.route('/')
def categorias():
    return render_template("categorias.html")

@categoria_route.route('/listas')
def lista_categorias():
    # Listar todos as categorias
    categorias = Categorias.query.all()

    return render_template("lista_categoria.html", categorias=[categoria.to_dict() for categoria in categorias])


@categoria_route.route('/', methods=['POST'])
def inserir_categorias():
    #Inserir categorias

    data = request.get_json()

    nova_categoria = Categorias(
        nome = data['nome'],
        descricao =  data['descricao'],
    )

    # Adicionar a nova categoria ao banco de dados
    db.session.add(nova_categoria)
    db.session.commit()

    CATEGORIAS.append(nova_categoria)

    return render_template('item_categoria.html', categoria=nova_categoria)

@categoria_route.route('/new')
def form_categorias():
    #Formulario para cadastrar uma categoria
    return render_template("form_categorias.html")

@categoria_route.route('/<int:categoria_codigo>')
def detalhe_categoria(categoria_codigo):
    #Exibir detalhes de uma categoria

    # O codigo abaixo é um exemplo sem um banco de dados
    #categoria = list(filter(lambda i: i['codigo'] == categoria_codigo, CATEGORIAS)) [0]

    categoria = Categorias.query.filter_by(codigo=categoria_codigo).first()

    return render_template("detalhes_categorias.html", categoria=categoria)


@categoria_route.route('/<int:categoria_codigo>/edit')
def form_edit_categoria(categoria_codigo):
    #Formulario para editar a categoria
    categoria = None

    # O codigo abaixo é um exemplo para ser usado sem um banco de dados
    '''for i in CATEGORIAS:
        if i['codigo'] == categoria_codigo:
            categoria = i'''
    
    categoria = Categorias.query.filter_by(codigo=categoria_codigo).first()
    return render_template("form_categorias.html", categoria=categoria)

@categoria_route.route('/<int:categoria_codigo>/update', methods=['PUT'])
def atualizar_categoria(categoria_codigo):
    #Formulario para atualizar a categoria

    data = request.json

    categoria_editado = Categorias.query.filter_by(codigo=categoria_codigo).first()
    categoria_editado.nome = data['nome']
    categoria_editado.descricao = data['descricao']
    db.session.commit()

    
    # O codigo abaixo é para ser usado sem um banco de dados
    '''#obter categoria pelo id
    for i in CATEGORIAS:
        if i['codigo'] == categoria_codigo:
            i['nome'] = data['nome']
            i['descricao'] = data['descricao']

            categoria_editado = i'''

    #editar categoria
    return render_template('item_categoria.html', categoria=categoria_editado)

@categoria_route.route('/<int:categoria_codigo>/delete', methods=['DELETE'])
def deletar_categoria(categoria_codigo):
    #Deletar categoria

    # O codigo abaixo é para ser usado sem um banco de dados
    '''global CATEGORIAS
    CATEGORIAS = [ i for i in CATEGORIAS if i['codigo'] != categoria_codigo ]'''

    categoria = Categorias.query.filter_by(codigo=categoria_codigo).first()
    db.session.delete(categoria)
    db.session.commit()

    return {"deleted":"ok"}