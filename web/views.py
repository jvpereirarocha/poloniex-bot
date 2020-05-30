from flask import Blueprint, render_template
from sql import Database

endpoint = Blueprint('app', __name__)


@endpoint.route('/', methods=['GET'])
def index():
    db = Database()
    candles = db.get()
    return render_template('index.html', candles=candles)
