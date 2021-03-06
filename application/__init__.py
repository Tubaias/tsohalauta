# flask
from flask import Flask
app = Flask(__name__)

# database
from flask_sqlalchemy import SQLAlchemy
import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"    
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# imports
from application import views

from application.messages import models
from application.messages import views

from application.threads import models
from application.threads import views

from application.supermessages import models
from application.supermessages import views

from application.boards import models
from application.boards import views

from application.auth import models
from application.auth import views

from application.statistics import views
from application.search import views

# login
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# database init
try:
    db.create_all()
except:
    pass