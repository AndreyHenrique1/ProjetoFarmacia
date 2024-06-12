from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.administrador import Administrador
from models.usuario import Usuario
from database.db import db

login_route = Blueprint('login', __name__, template_folder='../../front-end/templates')

@login_route.route('/login')
def login():
    return render_template('login.html')

@login_route.route('/login/adm', methods=['POST'])
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

@login_route.route('/login/usuario', methods=['POST'])
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
