from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy


from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///forum.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application.auth import models
from application.discussions import models
from application.messages import models

from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from application.auth import views

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

db.create_all()