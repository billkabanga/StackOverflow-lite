from flask import Flask
from instance.config import DevelopmentConfig
from api.app import my_blue_print

#Function below creates the app,gives it a name,sets the configuration mode and registers my bluepritn that has the routes.
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(my_blue_print)


    return app