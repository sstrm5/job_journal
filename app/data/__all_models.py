from datetime import datetime
import sqlalchemy as sa
from sqlalchemy import orm

SqlAlchemyBase = orm.declarative_base()


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sa.Column(
        sa.Integer,
        primary_key=True,
        autoincrement=True,
    )
    surname = sa.Column(sa.String)
    name = sa.Column(sa.String)
    age = sa.Column(sa.Integer)
    position = sa.Column(sa.String)
    speciality = sa.Column(sa.String)
    address = sa.Column(sa.String)
    email = sa.Column(
        sa.String,
        unique=True,
    )
    hashed_password = sa.Column(sa.String)
    modified_date = sa.Column(sa.DateTime, default=datetime.now)


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sa.Column(
        sa.Integer,
        primary_key=True,
        autoincrement=True,
    )
    team_leader = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    job = sa.Column(sa.String)
    work_size = sa.Column(sa.Integer)
    collaborators = sa.Column(sa.String)
    start_date = sa.Column(sa.DateTime)
    end_date = sa.Column(sa.DateTime)
    is_finished = sa.Column(sa.Boolean)

    def __repr__(self):
        return f'{self.job} {self.work_size} {self.collaborators} {self.is_finished}'
