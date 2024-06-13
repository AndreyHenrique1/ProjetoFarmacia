from flask import Blueprint, render_template, request
from models.administrador import Administrador
from database.db import db

adm_route = Blueprint('ADM', __name__, template_folder='../../front-end/templates/Pasta_adm')

@adm_route.route('/')
def administradores():
    return render_template("ADM.html")

@adm_route.route('/listas')
def lista_administradores():
    # Listar todos os administradores
    administradores = Administrador.query.all()

    return render_template("lista_adm.html", administradores=[adm.to_dict() for adm in administradores])

@adm_route.route('/', methods=['POST'])
def inserir_administrador():
    # Inserir administrador
    data = request.get_json()

    novo_administrador = Administrador(
        nome = data['nome'],
        email = data['email'],
        senha = data['senha'],
    )

    # Adicionar o novo administrador ao banco de dados
    db.session.add(novo_administrador)
    db.session.commit()

    return render_template('item_adm.html', administrador=novo_administrador)

@adm_route.route('/new')
def form_administrador():
    # Formulário para cadastrar um administrador
    return render_template("form_adm.html")

@adm_route.route('/<int:administrador_codigo>')
def detalhe_administrador(administrador_codigo):
    # Exibir detalhes de um administrador
    administrador = Administrador.query.filter_by(codigo=administrador_codigo).first()

    return render_template("detalhes_adm.html", administrador=administrador)

@adm_route.route('/<int:administrador_codigo>/edit')
def form_edit_administrador(administrador_codigo):
    # Formulário para editar o administrador
    administrador = Administrador.query.filter_by(codigo=administrador_codigo).first()
    return render_template("form_adm.html", administrador=administrador)

@adm_route.route('/<int:administrador_codigo>/update', methods=['PUT'])
def atualizar_administrador(administrador_codigo):
    # Formulário para atualizar o administrador
    data = request.json

    administrador_editado = Administrador.query.filter_by(codigo=administrador_codigo).first()
    administrador_editado.nome = data['nome']
    administrador_editado.email = data['email']
    administrador_editado.senha = data['senha']
    db.session.commit()

    # Editar administrador
    return render_template('item_adm.html', administrador=administrador_editado)

@adm_route.route('/<int:administrador_codigo>/delete', methods=['DELETE'])
def deletar_administrador(administrador_codigo):
    # Deletar administrador
    administrador = Administrador.query.filter_by(codigo=administrador_codigo).first()
    db.session.delete(administrador)
    db.session.commit()

    return {"deleted": "ok"}
