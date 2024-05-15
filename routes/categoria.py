from flask import Blueprint, render_template
from database.categoria import categorias

categoria_route = Blueprint('categoria', __name__)

@categoria_route.route('/')
def lista_categorias():
    return render_template("lista_categoria.html", categorias=categorias)
    pass


@categoria_route.route('/', methods=['POST'])
def inserir_categorias():
    #Inserir categorias
    pass


@categoria_route.route('/new')
def form_categorias():
    #Formulario para cadastrar uma categoria
    return render_template("form_categorias.html")
    pass

@categoria_route.route('/<int:categoria_id>')
def detalhe_categoria(categoria_id):
    #Exibir detalhes de uma categoria
    return render_template("detalhe_categorias.html")
    pass

@categoria_route.route('/<int:categoria_id>/edit')
def form_edit_categoria(categoria_id):
    #Formulario para editar a categoria
    return render_template("form_edit_categorias.html")
    pass

@categoria_route.route('/<int:categoria_id>/update', methods=['PUT'])
def atualizar_categoria(categoria_id):
    #Formulario para atualizar a categoria
    pass

@categoria_route.route('/<int:categoria_id>/delete', methods=['DELETE'])
def deletar_categoria(categoria_id):
    #Deletar categoria
    pass