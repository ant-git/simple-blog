from flask import render_template, redirect, url_for
from __init__ import app
from author.form import RegisterForm, LoginForm


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    error = ''
    if form.validate_on_submit():
        # looking for author who has entered username and password
        
        pass
    return render_template('author/login.html', form=form, error=error)


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('author/register.html', form=form)


@app.route('/success')
def success():
    return "Author Registered!"
