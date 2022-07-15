from re import T
from flask import Config


class Config(Config):
    """
    Flask configuration class and MONGODB.
    """
    enable_utc = True
    APP_NAME = "Flask-App"
    MONGODB_DB = "api"
    MONGODB_USERNAME = "root"
    MONGODB_PASSWORD = "root"
    MONGODB_HOST = "127.0.0.1"
    MONGODB_PORT = 27017
    JWT_SECRET_KEY = "secret"