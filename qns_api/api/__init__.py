from flask import Flask
from instance.config import DevelopmentConfig
from api.app import my_blue_print

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(DevelopmentConfig)


    return app