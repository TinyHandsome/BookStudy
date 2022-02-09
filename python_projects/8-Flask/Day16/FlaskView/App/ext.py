from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

models = SQLAlchemy()
migrate = Migrate()


def init_ext(app):
    models.init_app(app)
    migrate.init_app(app, models)
