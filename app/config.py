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
    MONGODB_HOST = "localhost"
    MONGODB_PORT = 27017
    JWT_SECRET_KEY = "secret"
    ERROR_404_HELP = False
    AWS_BUCKET_NAME = "kpi-spa-demo-dft"