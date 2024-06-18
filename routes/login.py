from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.administrador import Administrador
from models.usuario import Usuario
from database.db import db

login_route = Blueprint('login', __name__, template_folder='../../front-end/templates')

#Rederizar a pagina de login
@login_route.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@login_route.route('/RegistrarUsuario', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        #Obtém os dados enviados pelo formulário
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        endereco = request.form.get('endereco')
        email = request.form.get('email')
        senha = request.form.get('senha')
        #Registra no banco de dados
        novo_usuario = Usuario(nome=nome, cpf=cpf, endereco=endereco, email=email, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()
        flash('Usuário registrado com sucesso!', 'success')
        return redirect(url_for('login.login'))
    #Se o metodo não for POST chama a página registrar_usuario
    return render_template('registrar_usuario.html')


@login_route.route('/ADM', methods=['POST'])
def login_adm():
    #Recebe os dados do formulario
    email = request.form.get('email')
    senha = request.form.get('senha')
    #Encontra um adm com o mesmo email e senha
    adm = Administrador.query.filter_by(email=email, senha=senha).first()
    if adm:
        # Login bem-sucedido
        flash('Login como Administrador bem-sucedido!', 'success')
        session['email'] = email
        return redirect(url_for('ADM.administradores'))
    else:
        flash('Email ou senha de Administrador incorretos.', 'danger')
        return redirect(url_for('login.login'))

@login_route.route('/Usuario', methods=['GET', 'POST'])
def login_usuario():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        usuario = Usuario.query.filter_by(email=email, senha=senha).first()
        if usuario:
            # Login bem-sucedido
            session['email'] = email
            flash('Login como Administrador bem-sucedido!', 'success')
            return redirect(url_for('home.home'))
        else:
            flash('Email ou senha de usuário incorretos.', 'danger')
            return redirect(url_for('login.login'))
    else:
        # Se a solicitação for GET, redirecione para a página de login
        return render_template('login.html')
