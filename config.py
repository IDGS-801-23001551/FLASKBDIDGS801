import os

from sqlalchemy import create_engine

class config(object):
    SECRET_KEY = "ClaveSecreta"
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://root:root@localhost/bdidgs801'
    SQLALCHEMY_TRACK_MODIFICATIONS = False