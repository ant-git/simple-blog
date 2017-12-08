from flask_wtf import Form
from wtforms import validators, TextAreaField, StringField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from author.form import RegisterForm
from blog.models import Category


class SetupForm(RegisterForm):
    name = StringField('Blog name', [
        validators.DataRequired(),
        validators.Length(max=80)
    ])
    # other fields will be inherited from Register Form


def categories():
    return Category.query


class PostForm(Form):
    title = StringField('Title', [
        validators.DataRequired(),
        validators.Length(max=80)
    ])
    body = TextAreaField('Content', validators=[validators.DataRequired()])
    category = QuerySelectField('Category', query_factory=categories,
                                allow_blank=True)  # drop down menu with categories
    new_category = StringField('New Category')
