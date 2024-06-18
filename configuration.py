import os
from routes.home import home_route
from routes.categoria import categoria_route
from routes.login import login_route
from routes.produto import produto_route
from routes.adm import adm_route
from routes.fornecedor import fornecedor_route
from routes.usuario import usuario_route
from database.db import db
<<<<<<< HEAD
import os
=======
from routes.carrinho import carrinho_route
>>>>>>> 574e6909fb8cd0db32a8cd9759b79864585b7568

def configure_all(app):
    configure_routes(app)
    configure_db(app)
<<<<<<< HEAD
    configure_uploads(app)
    app.config['SECRET_KEY'] = 'dervfgvfgf1234'
=======
    app.config['SECRET_KEY'] = 'dervfgvfgf1234'
    app.config['UPLOAD_FOLDER'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/Imagens')
>>>>>>> 574e6909fb8cd0db32a8cd9759b79864585b7568

def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(login_route, url_prefix='/Login')
    app.register_blueprint(adm_route, url_prefix='/Login/ADM')
<<<<<<< HEAD
    app.register_blueprint(usuario_route, url_prefix='/Login/Usuarios')  
=======
    app.register_blueprint(carrinho_route, url_prefix='/Login/Carrinho')
    app.register_blueprint(usuario_route, url_prefix='/Login/Cadastrado')  
>>>>>>> 574e6909fb8cd0db32a8cd9759b79864585b7568
    app.register_blueprint(fornecedor_route, url_prefix='/Login/ADM/Fornecedor')
    app.register_blueprint(categoria_route, url_prefix='/Login/ADM/Categorias')
    app.register_blueprint(produto_route, url_prefix='/Login/ADM/Produtos')

def configure_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3308/farmacia'
    db.init_app(app)

def configure_uploads(app):
    app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/uploads')
