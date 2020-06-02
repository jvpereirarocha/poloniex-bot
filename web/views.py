from flask import Blueprint, render_template
from .db import Candles

endpoint = Blueprint('app', __name__)


@endpoint.route('/', methods=['GET'])
def index():
    candles = Candles.query.all()
    return render_template('index.html', candles=candles)
