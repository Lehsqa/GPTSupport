from flask import Flask
from flask_cors import CORS

from src.routes import rest_api
from src.chatGPT import ChatGPT

app = Flask(__name__)

app.config.from_object('src.config.BaseConfig')

rest_api.init_app(app)
CORS(app)
