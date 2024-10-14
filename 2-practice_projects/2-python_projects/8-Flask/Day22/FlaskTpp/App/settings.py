import os

from App.email.base64_encode_decode import base64_decode_json2dict
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
    SECRET_KEY = 'abaaba'


class DevelopConfig(Config):
    DEBUG = True

    dbinfo = {
        'ENGINE': 'mysql',
        "DRIVER": 'pymysql',
        'USER': 'root',
        'PASSWORD': password,
        'HOST': 'localhost',
        'PORT': 3307,
        'NAME': 'GP1FlaskTpp',
    }

    with open('App/email/myemail', 'r', encoding='utf-8') as f:
        email = f.read()
    my_email = base64_decode_json2dict(email)

    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USERNAME = my_email.get('username')
    MAIL_PASSWORD = my_email.get('imap_smtp')
    MAIL_DEFAULT_SENDER = MAIL_USERNAME

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
        'NAME': 'GP1FlaskDay04',
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
        'NAME': 'GP1FlaskDay04',
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
        'NAME': 'GP1FlaskDay04',
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


envs = {
    'develop': DevelopConfig,
    'testing': TestConfig,
    'staging': StagingConfig,
    'product': ProductConfig,
    'default': DevelopConfig
}


ADMINS = (
    'Rock',
    'Tom',
)

FILE_PATH_PREFIX = "/static/uploads/icons"
UPLOADS_DIR = os.path.join(BASE_DIR, 'App/static/uploads/icons')