from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
cache = Cache(
    config={
        "CACHE_TYPE": 'redis'
    }
)


def init_ext(app):
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
