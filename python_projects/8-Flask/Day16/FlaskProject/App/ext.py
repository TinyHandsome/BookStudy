from flask_sqlalchemy import SQLAlchemy

models = SQLAlchemy()


def init_ext(app):
    models.init_app(app)
