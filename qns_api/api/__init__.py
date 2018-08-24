from flask import Flask
from qns_api.instance.config import DevelopmentConfig
from qns_api.api.app import my_blue_print

#Function below creates the app,gives it a name,sets the configuration mode and registers my bluepritn that has the routes.
def create_app(DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(my_blue_print)


    return app