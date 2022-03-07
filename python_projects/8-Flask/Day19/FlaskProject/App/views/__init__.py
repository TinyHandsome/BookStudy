from flask import Flask

from App.views.HelloView import blue


def init_view(app: Flask):
    app.register_blueprint(blue)
