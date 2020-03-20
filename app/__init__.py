from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='', static_folder='./static')
app.config.from_object('config')
app.config['JSON_AS_ASCII'] = False
app.secret_key = app.config['SECRET_KEY']

db = SQLAlchemy(app)

from . import notifier
from . import scheduler
from . import controller

controller.initialize()
