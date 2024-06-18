from flask import Blueprint, render_template, request
from routes.categoria import Categorias
from routes.produto import Produtos
from models.categorias import Categorias

home_route = Blueprint('home', __name__, template_folder='../../front-end/templates')

@home_route.route('/')
def home():
    produtos = Produtos.query.all()
    categorias = Categorias.query.all()
    return render_template("home.html", categorias=categorias, produtos=produtos)

@home_route.route('/categoria/<int:codigo_categoria>')
#Pesquisar produto por categorias
def produtos_por_categoria(codigo_categoria):
    produtos = Produtos.query.filter_by(codcategoria=codigo_categoria).all()   
    categorias = Categorias.query.all()
    return render_template("home.html", categorias=categorias, produtos=produtos)

@home_route.route('/pesquisar', methods=['GET', 'POST'])
#Pesquisar o nome do produto
def pesquisar_produtos():
    if request.method == 'POST':
        termo_pesquisa = request.form['termo_pesquisa']
        produtos = Produtos.query.filter(Produtos.nome.ilike(f'%{termo_pesquisa}%')).all()
    else:
        produtos = []

    categorias = Categorias.query.all()
    return render_template("home.html", categorias=categorias, produtos=produtos)