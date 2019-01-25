from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return 'Home page'


@app.route('/user')
def user():
    return 'User page'


@app.route('/about')
def about():
    return 'About page'


if __name__ == '__main__':
    app.run()
