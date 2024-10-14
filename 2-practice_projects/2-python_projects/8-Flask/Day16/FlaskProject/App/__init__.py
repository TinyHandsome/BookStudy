from flask import Flask

from App.ext import init_ext
from App.settings import envs
from App.views import init_view


def create_app(env):
    app = Flask(__name__)
    # app.register_blueprint(blue)
    # app.register_blueprint(second)

    # uri 数据库+驱动://用户名:密码@主机:端口/具体的库
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:tian19951103@localhost:3307/GP1HelloFlask'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    app.config.from_object(envs.get(env))

    init_ext(app)
    init_view(app=app)

    return app
