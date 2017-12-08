from flask import render_template, redirect, url_for, session
from __init__ import app
from author.form import RegisterForm, LoginForm
from author.models import Author


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    error = ''
    if form.validate_on_submit():
        # looking for author who has entered username and password
        author = Author.query.filter_by(
            username=form.username.data,
            password=form.password.data
        ).limit(1)

        if author.count():
            session["username"] = form.username.data # stroing username in the session
            return redirect(url_for('login_success'))
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

@app.route('/login_success')
def login_success():
    return "Author logged in!"