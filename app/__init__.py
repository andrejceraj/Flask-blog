from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'
mail = Mail(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

from app.main import routes

import logging
from logging.handlers import RotatingFileHandler
import os
from app.errors import bp as error_bp
from app.auth import bp as auth_bp
from app.main import bp as main_bp

app.register_blueprint(error_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(main_bp)

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')
