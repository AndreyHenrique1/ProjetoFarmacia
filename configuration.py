from routes.home import home_route
from routes.categoria import categoria_route
from database.db import db

def configure_all(app):
    configure_routes(app)
    configure_db(app)

def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(categoria_route, url_prefix='/Categorias')

def configure_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/farmacia'
    db.init_app(app)

