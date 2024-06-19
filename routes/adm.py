from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.administrador import Administrador
from database.db import db
from functools import wraps

adm_route = Blueprint('ADM', __name__, template_folder='../../front-end/templates/Pasta_adm')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'senha' not in session:
            flash('Você precisa estar logado para acessar esta página.', 'danger')
            return redirect(url_for('login.login'))  # Redireciona para a página de login
        return f(*args, **kwargs)
    return decorated_function

@adm_route.route('/')
@login_required
def administradores():
    return render_template('ADM.html')

@adm_route.route('/CadastrarADM')
#Formulario de cadastro de adms
def administradores_cadastrar():
    return render_template('cadastrar_adm.html')


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
    flash("Novo administrador registrado com sucesso!!")
    db.session.commit()

@adm_route.route('/new')
def form_administrador():
    # Formulário para cadastrar um administrador
    return render_template("form_administrador.html")

