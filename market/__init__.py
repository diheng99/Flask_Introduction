from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY']='680d06223bae899ff44a5790'
app.app_context().push()
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from market import route