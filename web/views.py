from flask import Blueprint, render_template

endpoint = Blueprint('app', __name__)


@endpoint.route('/')
def index():
    return render_template('index.html')
