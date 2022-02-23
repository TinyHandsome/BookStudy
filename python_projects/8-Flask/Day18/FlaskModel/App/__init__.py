from flask import Flask

from App.ext import init_ext
from App.settings import envs
from App.views import init_blue


def create_app(env):
    app = Flask(__name__)

    # 初始化整个项目的配置
    app.config.from_object(envs.get(env))

    # 初始化 非路由相关 扩展库
    init_ext(app)

    # 路由初始化
    init_blue(app)

    return app