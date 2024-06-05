from routes.home import home_route
from routes.categoria import categoria_route
from routes.login import login_route
from routes.produto import produto_route
from routes.adm import adm_route
from database.db import db

def configure_all(app):
    configure_routes(app)
    configure_db(app)

def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(login_route, url_prefix='/Login')
    app.register_blueprint(categoria_route, url_prefix='/Login/ADM/Categorias')
    app.register_blueprint(adm_route, url_prefix='/Login/ADM')
    app.register_blueprint(produto_route, url_prefix='/Login/ADM/Produtos')

def configure_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/farmacia'
    db.init_app(app)

