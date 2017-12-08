from slugify import slugify

from __init__ import app
from __init__ import db
from flask import render_template, redirect, flash, url_for, session, abort
from blog.form import SetupForm, PostForm
from author.models import Author
from blog.models import Blog, Category, Post
from author.decorators import login_required, author_required
import bcrypt


@app.route('/')
@app.route('/index')
def index():
    blogs = Blog.query.count()
    if blogs == 0:
        return redirect(url_for('setup'))
    return "Hello World!"


@app.route('/admin')
@author_required
@login_required
def admin():
    return render_template('blog/admin.html')


@app.route('/setup', methods=('GET', 'POST'))
def setup():
    form = SetupForm()
    error = ""
    # taking data from form and adding that data it to the table
    if form.validate_on_submit():
        salt = bcrypt.gensalt()  # generating salt
        hashed_password = bcrypt.hashpw(form.password.data, salt)
        author = Author(
            form.fullname.data,
            form.email.data,
            form.username.data,
            hashed_password,
            True
        )
        db.session.add(author)
        db.session()
        db.session.flush()
        if author.id:
            blog = Blog(
                form.name.data,
                author.id
            )
            db.session.add(blog)
            db.session.flush()
        else:
            db.session.rollback()
            error = "Error Creating user"
        if author.id and blog.id:
            db.session.commit()
            flash("Blog Created")
            return redirect(url_for('admin'))
        else:
            db.session.rollback()
            error = "Error Creating Blog"
    return render_template('blog/setup.html', form=form)


@app.route('/post', methods=('GET', 'POST'))
@author_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        if form.new_category.data:
            new_category = Category(form.new_category.data)
            db.session.add(new_category)
            db.session.flush()
            category = new_category
        elif form.category.data:
            category_id = form.category.get_pk(form.category.data)
            category = Category.query.filter_by(id=category_id).first()
        else:
            category = None
        blog = Blog.query.first()
        author = Author.query.filter_by(username=session['username']).first()
        title = form.title.data
        body = form.body.data
        slug = slugify(title)
        post = Post(blog, author, title, body, category, slug)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('blog/post.html', form=form)


@app.route('/article')
def article():
    return render_template('blog/article.html')
