from flask import Flask
from .views import endpoint
from .config import Config
from .db import db


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(endpoint)
    app.add_url_rule('/', endpoint='index')

    return app
