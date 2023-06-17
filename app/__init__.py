from flask import Flask, request
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
    UserMixin,
)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

cors = CORS(app, resources={r"/foo": {"origins": 'localhost'}})
app.config['CORS_HEADERS'] = 'Content-Type'



login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/login"


class User:
    def __init__(self, id):
        self.id = id

    def is_authenticated(self):
        return False


from .urls import *
