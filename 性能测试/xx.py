from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '123'


@app.route('/index')
def index2():
    return '123index'


if __name__ == '__main__':
    app.run(port=5000)
