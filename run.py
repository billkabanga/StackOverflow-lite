from flask import Flask
from qns_api.instance import config
from qns_api.api import create_app
from qns_api.api import app


app = create_app(config.DevelopmentConfig)

#this conditional statememnt runs the application
if __name__ == '__main__':
    app.run()
