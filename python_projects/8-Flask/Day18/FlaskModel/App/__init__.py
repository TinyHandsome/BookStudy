from flask import Flask


def create_app(env):
    app = Flask(__name__)

    # 初始化整个项目的配置

    return app