from flask import request


def load_middleware(app):
    @app.before_request
    def before():
        print('中间件：', request.url)

        """
            统计
            优先级
            反爬
                频率
            用户认证
            用户权限
        """

    @app.after_request
    def after(response):
        print('中间件', response)

        return response
