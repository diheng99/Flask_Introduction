from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY']='680d06223bae899ff44a5790'
app.app_context().push()

from market import route