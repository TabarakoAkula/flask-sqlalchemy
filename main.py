from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    users_info = [(i.id, i.title_of_activity, i.team_leader, i.duration, i.list_of_coll, i.is_finished) for i in users]
    return users_info
    # app.run()


def add_user():
    print('CONGRATULATIONS, NEW USER!!!')


if __name__ == '__main__':
    main()
