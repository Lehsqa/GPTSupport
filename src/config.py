import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class BaseConfig():
    SECRET_KEY = os.getenv('SECRET_KEY', None)
