from flask import Blueprint
from flask import render_template

views = Blueprint('views',__name__)

@views.route('/')
def main():
    return render_template("main.html")