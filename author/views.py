import bcrypt
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
        # looking for author in database with the same username as entered in the form
        author = Author.query.filter_by(
            username=form.username.data
        ).first()  # return first author

        # to check password
        if author:
            if bcrypt.checkpw(form.password.data.encode('utf8'), author.password.encode('utf8')):
                session["username"] = form.username.data  # storing username in the session
                session["is_author"] = author.is_author
                if 'next' in session:
                    next = session.get('next')
                    session.pop('next')
                    return redirect(next)
                else:
                    return redirect(url_for('index'))
            else:
                error = "Incorrect username and password"
        else:
            error = "Incorrect username and password"
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


@app.route('/logout')
def logout():
    session.pop('username') # logging out and removing username from session
    session.pop('is_author')
    return redirect(url_for('index'))
