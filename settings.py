import os

SECRET_KEY = 'super-secret'
DEBUG = True
DB_USERNAME = 'root'
DB_PASSWORD = 'box'
BLOG_DATABASE_NAME = 'blog'
DB_HOST = 'localhost'
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
UPLOADED_IMAGES_DEST = '/home/ant/PycharmProjects/simple-blog/static/images'
UPLOADED_IMAGES_URL = '/static/images/'
