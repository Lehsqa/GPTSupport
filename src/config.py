import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class BaseConfig():
    SECRET_KEY = os.getenv('SECRET_KEY', None)
    API_KEY = "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"
