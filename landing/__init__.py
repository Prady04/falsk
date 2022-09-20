from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
csrf = CSRFProtect(app)


db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
db_uri = 'sqlite:///{}'.format(db_path)

db = SQLAlchemy(app)

app.config.update(dict(
  SECRET_KEY='0828080200000!KJHasdsasda',
  WTF_CSRF_SECRET_KEY='asds678677!*aHGFYJ',
  SQLALCHEMY_DATABASE_URI=db_uri,
  SQLALCHEMY_TRACK_MODIFICATIONS=True,
  
))


from .views import *
from .jobs.views import *
from .profiles.views import *
from .home.views import *

