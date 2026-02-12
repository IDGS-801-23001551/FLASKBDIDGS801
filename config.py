import os

from sqlalchemy import create_engine

class config(object):
    SECRET_KEY = "ClaveSecreta"
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://usuario:contraseña@host:puerto/nombre_base'
    SQLALCHEMY_TRACK_MODIFICATIONS = False