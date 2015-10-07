import flask
from flask import Flask

app = Flask(__name__)
data = []

@app.route('/save', methods=['post',])
def save():
    content = flask.request.values["content"]
    data.append(content)
    return content

@app.route('/')
def index():
    return  flask.render_template('index.html')

@app.route('/fetch')
def fetch():
    return "\n".join(data)


if __name__ == '__main__':
    # to make it work with pycharm debugging
    app.run(debug=True)
