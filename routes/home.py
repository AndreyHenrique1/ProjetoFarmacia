from flask import Blueprint, render_template

home_route = Blueprint('home', __name__, template_folder='../../front-end/templates')

@home_route.route('/')
def home():
    return render_template("home.html")