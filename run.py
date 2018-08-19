from flask import Flask
from instance.config import DevelopmentConfig
from api import create_app
from api import app

app = create_app(DevelopmentConfig)

#this conditional statememnt runs the application
if __name__ == '__main__':
    app.run()
