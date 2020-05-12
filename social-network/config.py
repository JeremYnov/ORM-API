from os import environ, path

basedir = path.abspath(path.dirname(__file__))


class Config:
    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("mysql+pymysql://root:@localhost/social_network")
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False