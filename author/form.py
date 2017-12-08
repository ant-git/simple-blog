from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField


class RegisterForm(Form):
    fullname = StringField('Full name', [validators.DataRequired()])
    email = EmailField('Email', [validators.DataRequired()])
    username = StringField('Username', [
        validators.DataRequired(),
        validators.Length(min=4, max=25)
    ])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Password does not match'),
        validators.Length(min=4, max=80)
    ])
    confirm = PasswordField('Repeat Password')


class LoginForm(Form):
    username = StringField('Username', [
        validators.DataRequired(),
        validators.Length(min=4, max=25)
    ])

    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=4, max=80)
    ])
