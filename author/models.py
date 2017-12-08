from __init__ import db


# Module class for Author
class Author(db.Model):
    # columns for Author
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80))
    email = db.Column(db.String(35), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(60))
    is_author = db.Column(db.Boolean)  # True if author is able to post

    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, fullname, email, username, password, is_author=False):
        self.fullname = fullname
        self.email = email
        self.username = username
        self.password = password
        self.is_author = is_author

    # for fetching records while working in shell
    def __repr__(self):
        return self.username
