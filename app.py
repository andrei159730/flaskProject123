from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
@app.route('/about')
def hello_world():  # put application's code here
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run()