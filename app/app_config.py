from datetime import datetime
import os
import random
from flask import Flask

from app.data import db_session
from app.data.__all_models import Jobs


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    db_session.global_init('db.db')

    from app.handlers import main_blueprint
    app.register_blueprint(main_blueprint)

    # list of 10 different works on english
    fake_jobs = [
        "Developing a new feature",
        "Optimizing the performance",
        "Fixing a bug",
        "Implementing a new algorithm",
        "Updating the design",
        "Implementing a new feature",
    ]

    session = db_session.create_session()
    for _ in range(30):
        collaborators = ", ".join(random.choices(
            list(map(str, range(1, 30))), k=random.randint(1, 3)))
        job = Jobs(
            team_leader=random.choice(range(1, 30)),
            job=random.choice(fake_jobs),
            work_size=random.randint(1, 42),
            collaborators=collaborators,
            start_date=datetime(2021, 1, 1),
            end_date=datetime(2021, 6, 30),
            is_finished=random.choice([False, True]),
        )
        session.add(job)
    session.commit()

    return app
