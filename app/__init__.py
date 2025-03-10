import os
from flask import Flask

from data.db_session import global_init


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    global_init('db.db')

    return app
