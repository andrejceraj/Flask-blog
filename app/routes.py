from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello world!"

@app.route('/index2')
def index2():
    return "Hello world nomero duo!"