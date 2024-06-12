from flask import Blueprint, render_template, request
from models.usuario import Usuario
from database.db import db

usuario_route = Blueprint('usuario', __name__, template_folder='../../front-end/templates/Pasta_usuarios')

@usuario_route.route('/')
def usuarios():
    return render_template("usuarios.html")

@usuario_route.route('/listas')
def lista_usuarios():
    # Listar todos os usuários
    usuarios = Usuario.query.all()

    return render_template("lista_usuario.html", usuarios=[usuario.to_dict() for usuario in usuarios])

@usuario_route.route('/', methods=['POST'])
def inserir_usuario():
    # Inserir usuário
    data = request.get_json()

    novo_usuario = Usuario(
        nome = data['nome'],
        cpf = data['cpf'],
        endereco = data['endereco'],
        email = data['email'],
        senha = data['senha'],
    )

    # Adicionar o novo usuário ao banco de dados
    db.session.add(novo_usuario)
    db.session.commit()

    return render_template('item_usuario.html', usuario=novo_usuario)

@usuario_route.route('/new')
def form_usuario():
    # Formulário para cadastrar um usuário
    return render_template("form_usuario.html")

@usuario_route.route('/<int:usuario_codigo>')
def detalhe_usuario(usuario_codigo):
    # Exibir detalhes de um usuário
    usuario = Usuario.query.filter_by(codigo=usuario_codigo).first()

    return render_template("detalhes_usuario.html", usuario=usuario)

@usuario_route.route('/<int:usuario_codigo>/edit')
def form_edit_usuario(usuario_codigo):
    # Formulário para editar o usuário
    usuario = Usuario.query.filter_by(codigo=usuario_codigo).first()
    return render_template("form_usuario.html", usuario=usuario)

@usuario_route.route('/<int:usuario_codigo>/update', methods=['PUT'])
def atualizar_usuario(usuario_codigo):
    # Formulário para atualizar o usuário
    data = request.json

    usuario_editado = Usuario.query.filter_by(codigo=usuario_codigo).first()
    usuario_editado.nome = data['nome']
    usuario_editado.cpf = data['cpf']
    usuario_editado.endereco = data['endereco']
    usuario_editado.email = data['email']
    usuario_editado.senha = data['senha']
    db.session.commit()

    # Editar usuário
    return render_template('item_usuario.html', usuario=usuario_editado)

@usuario_route.route('/<int:usuario_codigo>/delete', methods=['DELETE'])
def deletar_usuario(usuario_codigo):
    # Deletar usuário
    usuario = Usuario.query.filter_by(codigo=usuario_codigo).first()
    db.session.delete(usuario)
    db.session.commit()

    return {"deleted": "ok"}
