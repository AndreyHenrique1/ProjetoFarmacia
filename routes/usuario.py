from flask import Blueprint, render_template, request, redirect, url_for, flash
from wtforms import Form, StringField, PasswordField, validators

usuario_route = Blueprint('usuario', __name__)

class RegistrationForm(Form):
    nome = StringField('Nome completo', [validators.Length(min=4, max=25)])
    cpf = StringField('CPF', [validators.Length(min=4, max=25)])
    endereco = StringField('Endereço', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=35)])
    senha = PasswordField('Nova senha', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Senha e confirmação não são iguais')
    ])
    confirm = PasswordField('Confirmação da senha')