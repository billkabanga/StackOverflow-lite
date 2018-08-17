from flask import Flask
from instance.config import DevelopmentConfig
from api import create_app, app

app = create_app(DevelopmentConfig)


if __name__ == '__main__':
    app.run()
