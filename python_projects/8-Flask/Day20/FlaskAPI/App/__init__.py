from flask import Flask

from App.apis import init_api
from App.ext import init_ext
from App.middleware import load_middleware
from App.settings import envs


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(envs.get(env))

    init_ext(app)
    init_api(app=app)
    load_middleware(app)

    return app
