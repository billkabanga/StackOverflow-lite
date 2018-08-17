#Parent config class
class Config(object):
    DEBUG = False
    SECRET = 'SECRET'

#development configuration class
class DevelopmentConfig(Config):
    DEBUG = True

#testing confiuration class
class TestingConfig(Config):
    DEBUG = True
    TESTING = True

#production configuration class
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
