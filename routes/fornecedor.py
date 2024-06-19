from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from database.fornecedor import FORNECEDORES
from models.fornecedores import Fornecedores
from database.db import db
from functools import wraps

fornecedor_route = Blueprint('fornecedor', __name__, template_folder='../../front-end/templates/Pasta_fornecedores')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'senha' not in session:
            flash('Você precisa estar logado para acessar esta página.', 'danger')
            return redirect(url_for('login.login'))  # Redireciona para a página de login
        return f(*args, **kwargs)
    return decorated_function

@fornecedor_route.route('/')
@login_required
def fornecedores():   
    return render_template("fornecedores.html")

@fornecedor_route.route('/listas')
def lista_fornecedores():
    # Listar todos os fornecedores
    fornecedores = Fornecedores.query.all()

    return render_template("lista_fornecedor.html", fornecedores=[fornecedor.to_dict() for fornecedor in fornecedores])


@fornecedor_route.route('/', methods=['POST'])
def inserir_fornecedores():
    #Inserir categorias

    data = request.get_json()

    novo_fornecedor = Fornecedores(
        nome = data['nome'],
        contato =  data['contato'],
        endereco =  data['endereco'],
        email =  data['email'],
    )

    # Adicionar o novo fornecedor ao banco de dados
    db.session.add(novo_fornecedor)
    db.session.commit()

    FORNECEDORES.append(novo_fornecedor)

    return render_template('item_fornecedor.html', fornecedor=novo_fornecedor)

@fornecedor_route.route('/new')
def form_fornecedores():
    #Formulario para cadastrar um fornecedor
    return render_template("form_fornecedores.html")

@fornecedor_route.route('/<int:fornecedor_codigo>')
def detalhe_fornecedor(fornecedor_codigo):
    #Exibir detalhes de um fornecedor

    # O codigo abaixo é um exemplo sem um banco de dados
    #fornecedor = list(filter(lambda i: i['codigo'] == fornecedor_codigo, FORNECEDORES)) [0]

    fornecedor = Fornecedores.query.filter_by(codigo=fornecedor_codigo).first()

    return render_template("detalhes_fornecedores.html", fornecedor=fornecedor)


@fornecedor_route.route('/<int:fornecedor_codigo>/edit')
def form_edit_fornecedor(fornecedor_codigo):
    #Formulario para editar o fornecedor
    fornecedor = None

    # O codigo abaixo é um exemplo para ser usado sem um banco de dados
    '''for i in FORNECEDORES:
        if i['codigo'] == fornecedor_codigo:
            fornecedor = i'''
    
    fornecedor = Fornecedores.query.filter_by(codigo=fornecedor_codigo).first()
    return render_template("form_fornecedores.html", fornecedor=fornecedor)

@fornecedor_route.route('/<int:fornecedor_codigo>/update', methods=['PUT'])
def atualizar_fornecedor(fornecedor_codigo):
    #Formulario para atualizar o fornecedor

    data = request.json

    fornecedor_editado = Fornecedores.query.filter_by(codigo=fornecedor_codigo).first()
    fornecedor_editado.nome = data['nome']
    fornecedor_editado.contato = data['contato']
    fornecedor_editado.endereco = data['endereco']
    fornecedor_editado.email = data['email']
    db.session.commit()

    # O codigo abaixo é para ser usado caso não esteja usando um banco de dados 
    '''#obter fornecedor pelo id
    for i in FORNECEDORES:
        if i['codigo'] == fornecedor_codigo:
            i['nome'] = data['nome']
            i['contato'] = data['contato']
            i['endereco'] = data['endereco']
            i['email'] = data['email']

            fornecedor_editado = i'''

    #editar fornecedor
    return render_template('item_fornecedor.html', fornecedor=fornecedor_editado)

@fornecedor_route.route('/<int:fornecedor_codigo>/delete', methods=['DELETE'])
def deletar_fornecedor(fornecedor_codigo):
    #Deletar fornecedor

    # O codigo abaixo é para ser usado sem um banco de dados
    '''global FORNECEDORES
    FORNECEDORES = [ i for i in FORNECEDORES if i['codigo'] != fornecedor_codigo ]'''

    fornecedor = Fornecedores.query.filter_by(codigo=fornecedor_codigo).first()
    db.session.delete(fornecedor)
    db.session.commit()

    return {"deleted":"ok"}