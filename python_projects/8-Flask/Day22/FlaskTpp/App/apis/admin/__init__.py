from flask_restful import Api

from App.apis.admin.admin_user_api import AdminUsersResource

admin_api = Api(prefix='/admin')

admin_api.add_resource(AdminUsersResource, '/users/')