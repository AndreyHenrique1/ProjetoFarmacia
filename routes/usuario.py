from flask import Blueprint, render_template

usuario_route = Blueprint('usuario', __name__, template_folder='../../front-end')

@usuario_route.route('/')
def usuario():
    return render_template("templates/usuarios.html")