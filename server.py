import wtforms
from flask import Flask, render_template, redirect
from main import main, add_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class SubmitField:
    pass


class RegisterForm(FlaskForm):
    login = StringField('Login / email', validators=[DataRequired()])
    password = PasswordField('Password')
    repeat_password = PasswordField('Repeat password')
    surname = StringField('Surname')
    name = StringField('Name')
    age = StringField('Age')
    position = StringField('Position')
    speciality = StringField('Speciality')
    address = StringField('Address')
    submit = wtforms.SubmitField('Войти')
    # можно добавить validators=[DataRequired()] но т.к. лишь задача - не буду


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('register.html', form=form, title='Регистрация')


@app.route('/success')
def success():
    add_user()
    return 'Successfully registered'


@app.route('/')
def start_page():
    return render_template('index.html', lst=main())


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
