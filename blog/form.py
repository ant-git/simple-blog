from flask_wtf import Form
from wtforms import validators
from wtforms import StringField
from author.form import RegisterForm


class SetupForm(RegisterForm):
    name = StringField('Blog name', [
        validators.DataRequired(),
        validators.Length(max=80)
    ])
    # other fields will be inherited from Register Form

