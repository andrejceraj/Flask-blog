import flask
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flask.flash('Login requested for user={}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return flask.redirect(flask.url_for('index'))
    return flask.render_template('login.html', form=form, title='Sign in')