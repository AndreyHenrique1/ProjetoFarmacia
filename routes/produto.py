from flask import Blueprint, render_template

produto_route = Blueprint('produto', __name__, template_folder='../../front-end')

@produto_route.route('/')
def produto():
    return render_template("templates/produtos.html")