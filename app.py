from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<name>')
def hello_name(name):
    return 'Hello, %s!' % (name,)


if __name__ == '__main__':
    # to make it work with pycharm debugging
    app.run(debug=True, use_debugger=False, use_reloader=False)
