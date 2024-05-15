from flask import Flask, render_template, url_for
from routes.home import home_route
from routes.categoria import categoria_route

#Inicializar o flask
app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(categoria_route, url_prefix='/Categorias')

#Execução
app.run(debug=True)