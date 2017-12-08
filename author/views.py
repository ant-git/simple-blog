from flask import render_template, redirect, url_for, session, request
from __init__ import app
from author.decorators import login_required
from author.form import RegisterForm, LoginForm
from author.models import Author


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    error = None

    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)

    if form.validate_on_submit():
        # looking for author who has entered username and password
        author = Author.query.filter_by(
            username=form.username.data,
            password=form.password.data
        ).limit(1)

        if author.count():
            session["username"] = form.username.data  # storing username in the session
            if 'next' in session:
                next = session.get('next')
                session.pop('next')
                return redirect(next)
            else:
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
@login_required
def login_success():
    return "Author logged in!"

