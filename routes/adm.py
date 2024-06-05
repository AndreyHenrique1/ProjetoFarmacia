from flask import Blueprint, render_template

adm_route = Blueprint('adm', __name__, template_folder='../../front-end')

@adm_route.route('/')
def adm():
    return render_template("templates/ADM.html")