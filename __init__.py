from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate

app = Flask(__name__)
app.config.from_object('settings')  # to load settings from file
db = SQLAlchemy(app)

#migration
migrate = Migrate(app, db)

# always import new views to init file
from blog import views
from author import views


