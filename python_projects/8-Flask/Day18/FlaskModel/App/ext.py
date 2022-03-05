from flask_cache import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
cache = Cache(config={
    'CACHE_TYPE': 'simple',
})


def init_ext(app):
    db.init_app (app)
    migrate.init_app(app, db)
    DebugToolbarExtension(app)
    cache.init_app(app)
