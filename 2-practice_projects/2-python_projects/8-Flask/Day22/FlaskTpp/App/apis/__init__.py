from App.apis.admin import admin_api
from App.apis.common import common_api
from App.apis.movie_admin import movie_client_api
from App.apis.movie_user import client_api


def init_api(app):
    client_api.init_app(app)
    movie_client_api.init_app(app)
    admin_api.init_app(app)
    common_api.init_app(app)
