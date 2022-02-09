from flask import Flask, Blueprint

blue = Blueprint('blue', __name__)


def init_view(app: Flask):
    app.register_blueprint(blue)


@blue.route('/')
def index():
    return 'index'