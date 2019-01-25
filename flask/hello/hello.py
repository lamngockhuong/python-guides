from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"


if __name__ == '__main__':
    app.run()

'''
Run web with the bellow commands:
cd flask/hello
FLASK_APP=hello.py flask run
'''
