from flask import Blueprint, render_template, redirect, url_for

login_route = Blueprint('login', __name__, template_folder='../../front-end')

@login_route.route('/')
def produtos():
    return render_template("templates/login.html")




