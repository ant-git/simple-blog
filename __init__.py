from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from flask.ext.markdown import Markdown

app = Flask(__name__)
app.config.from_object('settings')  # to load settings from file
db = SQLAlchemy(app)

#migration
migrate = Migrate(app, db)

#Markdown
Markdown(app)

# always import new views to init file
from blog import views
from author import views


