import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class BaseConfig():
    SECRET_KEY = os.getenv('SECRET_KEY', None)
    API_KEY = "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"
