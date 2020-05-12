from os import environ


class Config:
    # Database
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/social_network"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
