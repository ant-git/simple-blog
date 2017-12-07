from flask import Flask

app = Flask(__name__)
app.config.from_object('settings')  # to load settings from file

from home import views
