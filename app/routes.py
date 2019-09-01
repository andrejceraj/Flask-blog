import flask
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Hello this is John'
        },
        {
            'author': {'username' : 'Susy'},
            'body': 'I love it here'
        }
    ]
    date = 'danas'
    return flask.render_template('index.html', title='Home', user=user, date = date, posts=posts)

@app.route('/index2')
def index2():
    return "Hello world nomero duo!"