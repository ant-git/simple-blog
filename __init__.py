from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('settings')  # to load settings from file

# always import new views to init file
from blog import views
from author import views

db = SQLAlchemy(app)
