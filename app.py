import flask
from flask import Flask

app = Flask(__name__)
data = {}

@app.route('/save', methods=['post',])
def save():
    title = flask.request.values["title"]
    content = flask.request.values["content"]
    data[title] = content
    return content

@app.route('/')
def index():
    return  flask.render_template('index.html')

@app.route('/fetchall')
def fetch():
    return "\n".join(data.values())

@app.route('/fetch/<title>')
def fetch_single(title):
    if title in data:
        return data[title]
    else:
        return flask.abort(404)

@app.route('/clear')
def clear():
    global data
    data = {}
    return "", 200

if __name__ == '__main__':
    # to make it work with pycharm debugging
    app.run(debug=True)
