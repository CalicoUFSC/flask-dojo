import flask
from flask import Flask

app = Flask(__name__)


@app.route('/<n>')
def primo(n):
    return "Yes!!"



if __name__ == '__main__':
    # to make it work with pycharm debugging
    app.run(debug=True, use_debugger=False)
