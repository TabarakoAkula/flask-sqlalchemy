import datetime
from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    users_info = [(i.id, i.title_of_activity, i.team_leader, i.duration, i.list_of_coll, i.is_finished) for i in users]
    return users_info
    # app.run()


if __name__ == '__main__':
    main()
