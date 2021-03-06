import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    UPLOAD_FOLDER = './uploads'
    MAX_CONTENT_PATH = 1024
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    SQLALCHEMY_DATABASE_URI = 'sqlite:///.\\data\\mydb.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

directory = ""
