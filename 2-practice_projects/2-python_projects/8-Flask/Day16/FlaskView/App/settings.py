import os
from App.password import password

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_db_uri(dbinfo):
    engine = dbinfo.get('ENGINE') or 'sqlite'
    driver = dbinfo.get('DRIVER') or 'sqlite'
    user = dbinfo.get('USER') or ''
    password = dbinfo.get('PASSWORD') or ''
    host = dbinfo.get("HOST") or ''
    port = dbinfo.get("PORT") or ''
    name = dbinfo.get("NAME") or ''

    return '{}+{}://{}:{}@{}:{}/{}'.format(engine, driver, user, password, host, port, name)


class Config:
    DEBUG = False
    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True

    dbinfo = {
        'ENGINE': 'mysql',
        "DRIVER": 'pymysql',
        'USER': 'root',
        'PASSWORD': password,
        'HOST': 'localhost',
        'PORT': 3307,
        'NAME': 'GP1HelloFlaskView',
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class TestConfig(Config):
    TESTING = True

    dbinfo = {
        'ENGINE': 'mysql',
        "DRIVER": 'pymysql',
        'USER': 'root',
        'PASSWORD': password,
        'HOST': 'localhost',
        'PORT': 3307,
        'NAME': 'GP1HelloFlask',
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class StagingConfig(Config):
    dbinfo = {
        'ENGINE': 'mysql',
        "DRIVER": 'pymysql',
        'USER': 'root',
        'PASSWORD': password,
        'HOST': 'localhost',
        'PORT': 3307,
        'NAME': 'GP1HelloFlask',
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class ProductConfig(Config):
    dbinfo = {
        'ENGINE': 'mysql',
        "DRIVER": 'pymysql',
        'USER': 'root',
        'PASSWORD': password,
        'HOST': 'localhost',
        'PORT': 3307,
        'NAME': 'GP1HelloFlask',
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


envs = {
    'develop': DevelopConfig,
    'testing': TestConfig,
    'staging': StagingConfig,
    'product': ProductConfig,
    'default': DevelopConfig
}
