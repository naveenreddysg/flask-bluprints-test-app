import os
class Config(object):
    """
    Common configurations
    """
    HOST = '0.0.0.0'
    PORT = 5000
    SECRET_KEY = 'p9Bv<3Eid9%$i01'
    DB_HOST = os.environ.get('DB_HOST')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_NAME = os.environ.get("DB_NAME")
    DB_USER = os.environ.get("DB_USER")
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL= True
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}:3306/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Put any configurations here that are common across all environments

class QaConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}:3306/{}'.format(
        Config.DB_USER,
        Config.DB_PASSWORD,
        Config.DB_HOST,
        Config.DB_NAME
    )
    DEBUG = False

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True


class MasterConfig(Config):
    """
    Production configurations
    """
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}:3306/{}'.format(
        Config.DB_USER,
        Config.DB_PASSWORD,
        Config.DB_HOST,
        Config.DB_NAME
    )
    DEBUG = False


app_config = {
    'dev': DevelopmentConfig,
    'qa': QaConfig,
    'prd': MasterConfig,
    'master': MasterConfig
}
