import os


def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE")
    driver = dbinfo.get("DRIVER")
    user = dbinfo.get("USER")
    password = dbinfo.get("PASSWORD")
    host = dbinfo.get("HOST")
    port = dbinfo.get("PORT")
    name = dbinfo.get("NAME")

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRECT_KEY = "LiYingjun"


class DevelopConfig(Config):
    DEBUG = True
    dbinfo = {
        'ENGINE': "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": os.environ.get("MYPASSWORD"),
        "HOST": "localhost",
        "PORT": "3307",
        "NAME": "GP1FLaskModel"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class TestConfig(Config):
    TESTING = True
    dbinfo = {
        'ENGINE': "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": os.environ.get("MYPASSWORD"),
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "GP1FlaskModel"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class StagineConfig(Config):
    dbinfo = {
        'ENGINE': "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": os.environ.get("MYPASSWORD"),
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "GP1FlaskModel"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class ProductConfig(Config):
    dbinfo = {
        'ENGINE': "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": os.environ.get("MYPASSWORD"),
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "GP1FlaskModel"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


envs = {
    'develop': DevelopConfig,
    'testing': TestConfig,
    'staging': StagineConfig,
    'product': ProductConfig,
    'default': DevelopConfig,
}