from datetime import datetime
from flask import Blueprint, render_template

from app.data import db_session
from app.data.__all_models import Jobs


main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def get_jobs():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template('jobs.html', jobs=jobs)


@main_blueprint.route('/add')
def add_jobs():
    ...
