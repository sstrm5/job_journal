import os
from flask import Flask

from app.data import db_session


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    db_session.global_init('db.db')

    from app.handlers import main_blueprint
    app.register_blueprint(main_blueprint)

    return app
