from flask_restful import Api

from App.apis.admin.admin_user_api import AdminUsersResource
from App.apis.admin.cinema_auth_api import AdminCinemaUsersResource, AdminCinemaUserResource

admin_api = Api(prefix='/admin')

admin_api.add_resource(AdminUsersResource, '/users/')
admin_api.add_resource(AdminCinemaUsersResource, '/cinemausers/')
admin_api.add_resource(AdminCinemaUserResource, '/cinemausers/<int:id>/')
