from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.usuario import Usuario
from database.db import db

usuario_route = Blueprint('usuario', __name__)

@usuario_route.route('/')
def usuario():
    return render_template("usuarios.html")


