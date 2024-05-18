from flask import Blueprint, render_template

home_route = Blueprint('home', __name__, template_folder='../../front-end')

@home_route.route('/')
def home():
    return render_template("templates/index.html")