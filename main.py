from flask import Flask
from configuration import configure_all
from flask_bcrypt import Bcrypt

#Inicializar o flask
app = Flask(__name__)

configure_all(app)

#Execução
app.run(debug=True)

