from flask import Blueprint, render_template, session, redirect, url_for, flash, request, jsonify
from models.produtos import Produtos
from functools import wraps

carrinho_route = Blueprint('carrinho', __name__, template_folder='../../front-end/templates')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'email' not in session:
            flash('Você precisa estar logado para acessar esta página.', 'warning')
            return redirect(url_for('login.login'))  # Redireciona para a página de login
        return f(*args, **kwargs)
    return decorated_function

@carrinho_route.route('/')
@login_required
def carrinho():
    # Obtém os produtos do carrinho da sessão
    produtos_no_carrinho = session.get('carrinho', [])
    
    # Corrige os tipos de dados dos valores 'valor' e 'quantidade'
    for produto in produtos_no_carrinho:
        produto['valor'] = float(produto['valor'])  # Converte para float
        produto['quantidade'] = int(produto['quantidade'])  # Converte para int
    
    # Calcula o valor total da compra
    total = sum(produto['valor'] * produto['quantidade'] for produto in produtos_no_carrinho)
    
    # Obtém as mensagens de flash
    mensagens_flash = session.pop('_flashes', [])
    
    # Renderiza o template da página do carrinho e passa os produtos, o total e as mensagens de flash como contexto
    return render_template('carrinho.html', produtos=produtos_no_carrinho, total=total, mensagens_flash=mensagens_flash)

@carrinho_route.route('/add_carrinho/<int:produto_codigo>', methods=['POST'])
def adicionar_ao_carrinho(produto_codigo):
    try:
        quantidade = int(request.form['quantidade'])
        produto = Produtos.query.filter_by(codigo=produto_codigo).first()
        print("Produto encontrado:", produto)  # Mensagem de depuração
        if produto:
            item = {
                'codigo': produto_codigo,
                'nome': produto.nome,
                'valor': produto.vendaValor,
                'quantidade': quantidade  # Utiliza a quantidade fornecida pelo usuário
            }
            if 'carrinho' in session:
                carrinho = session['carrinho']
                # Verifica se o produto já está no carrinho
                if any(produto['codigo'] == produto_codigo for produto in carrinho):
                    flash('Este produto já foi adicionado ao carrinho.', 'danger')
                else:
                    carrinho.append(item)
            else:
                session['carrinho'] = [item]
            
            session.modified = True  # Marca a sessão como modificada para garantir que ela seja salva

    except Exception as e:
        print(e)
        return jsonify({'status': 'error', 'message': 'Ocorreu um erro ao adicionar o produto ao carrinho.'})

    return redirect(url_for('carrinho.carrinho'))  # Redireciona de volta para a página do carrinho

@carrinho_route.route('/remover_do_carrinho/<int:produto_codigo>', methods=['POST'])
def remover_do_carrinho(produto_codigo):
    try:
        carrinho = session.get('carrinho', [])
        # Remove o produto do carrinho
        session['carrinho'] = [produto for produto in carrinho if produto['codigo'] != produto_codigo]
        flash('Produto removido do carrinho com sucesso.', 'success')
        session.modified = True  # Marca a sessão como modificada para garantir que ela seja salva
    except Exception as e:
        print(e)
        return jsonify({'status': 'error', 'message': 'Ocorreu um erro ao remover o produto do carrinho.'})

    return redirect(url_for('carrinho.carrinho'))  # Redireciona de volta para a página do carrinho
