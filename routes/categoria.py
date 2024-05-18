from flask import Blueprint, render_template, request
from database.categoria import CATEGORIAS

categoria_route = Blueprint('categoria', __name__, template_folder='../../front-end')

@categoria_route.route('/')
def lista_categorias():
    return render_template("templates/lista_categoria.html", categorias=CATEGORIAS)
    pass


@categoria_route.route('/', methods=['POST'])
def inserir_categorias():
    #Inserir categorias

    data = request.json

    nova_categoria = {
        "id": len(CATEGORIAS) + 1,
        "nome": data['nome'],
        "descricao": data['descricao'],
    }

    CATEGORIAS.append(nova_categoria)

    return render_template('templates/item_categoria.html', categoria=nova_categoria)

@categoria_route.route('/new')
def form_categorias():
    #Formulario para cadastrar uma categoria
    return render_template("templates/form_categorias.html")
    pass

@categoria_route.route('/<int:categoria_id>')
def detalhe_categoria(categoria_id):
    #Exibir detalhes de uma categoria

    categoria = list(filter(lambda i: i['id'] == categoria_id, CATEGORIAS)) [0]
    return render_template("templates/detalhe_categoria.html", categoria=categoria)


@categoria_route.route('/<int:categoria_id>/edit')
def form_edit_categoria(categoria_id):
    #Formulario para editar a categoria
    categoria = None

    for i in CATEGORIAS:
        if i['id'] == categoria_id:
            categoria = i
    return render_template("templates/form_categorias.html", categoria=categoria)

@categoria_route.route('/<int:categoria_id>/update', methods=['PUT'])
def atualizar_categoria(categoria_id):
    #Formulario para atualizar a categoria
    categoria_editado = None
    #Obter dados do formulario de edição
    data = request.json

    #obter categoria pelo id
    for i in CATEGORIAS:
        if i['id'] == categoria_id:
            i['nome'] = data['nome']
            i['descricao'] = data['descricao']

            categoria_editado = i

    #editar categoria
    return render_template('templates/item_categoria.html', categoria=categoria_editado)

@categoria_route.route('/<int:categoria_id>/delete', methods=['DELETE'])
def deletar_categoria(categoria_id):
    #Deletar categoria
    global CATEGORIAS
    CATEGORIAS = [ i for i in CATEGORIAS if i['id'] != categoria_id ]

    return {"deleted":"ok"}