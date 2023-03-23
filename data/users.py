import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title_of_activity = sqlalchemy.Column(sqlalchemy.String)
    team_leader = sqlalchemy.Column(sqlalchemy.String)
    duration = sqlalchemy.Column(sqlalchemy.Integer)
    list_of_coll = sqlalchemy.Column(sqlalchemy.String)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean)
