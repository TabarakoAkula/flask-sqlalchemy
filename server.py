from flask import Flask, render_template
from main import main

app = Flask(__name__, template_folder='templates')


@app.route('/')
def start_page():
    return render_template('index.html', lst=main())


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)