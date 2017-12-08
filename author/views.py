from flask import render_template, redirect
from __init__ import app
from author.form import RegisterForm


@app.route('/login')
def login():
    return "Hello user!"

@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    return render_template('author/register.html', form=form)