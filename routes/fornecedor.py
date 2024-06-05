from flask import Blueprint, render_template, redirect, url_for

fornecedor_route = Blueprint('fornecedor', __name__, template_folder='../../front-end')

@fornecedor_route.route('/')
def fornecedor():
    return render_template("templates/fornecedor.html")