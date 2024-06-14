from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.administrador import Administrador
from models.usuario import Usuario
from database.db import db
from routes.usuario import RegistrationForm
from flask_bcrypt import bcrypt

login_route = Blueprint('login', __name__, template_folder='../../front-end/templates')

@login_route.route('/')
def login():
    return render_template('login.html')

#Registrar novos usuários
@login_route.route('/RegistrarUsuario', methods=['GET', 'POST'])
def login_registrarUsuario():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        usuario = Usuario(
            nome=form.nome.data,
            cpf=form.cpf.data,
            endereco=form.endereco.data,
            email=form.email.data,
            senha=form.senha.data
        )
        db.session.add(usuario)
        db.session.commit()
        flash('Obrigado por se cadastrar conosco!!!')
        return redirect(url_for('login.login'))
    else:
        #Caso o formulario não der certo rederiza a página do registrar_usuario
        return render_template('registrar_usuario.html', form=form)


@login_route.route('/Login/ADM', methods=['POST'])
def login_adm():
    email = request.form.get('email')
    senha = request.form.get('senha')
    adm = Administrador.query.filter_by(email=email, senha=senha).first()
    if adm:
        # Login bem-sucedido
        flash('Login como Administrador bem-sucedido!', 'success')
        return redirect(url_for('home.home'))
    else:
        flash('Email ou senha de Administrador incorretos.', 'error')
        return redirect(url_for('login.login'))

@login_route.route('/Login/Usuario', methods=['POST'])
def login_usuario():
    email = request.form.get('email')
    senha = request.form.get('senha')
    usuario = Usuario.query.filter_by(email=email, senha=senha).first()
    if usuario:
        # Login bem-sucedido
        flash('Login como Usuário bem-sucedido!', 'success')
        return redirect(url_for('home.home'))
    else:
        flash('Email ou senha de Usuário incorretos.', 'error')
        return redirect(url_for('login.login'))
