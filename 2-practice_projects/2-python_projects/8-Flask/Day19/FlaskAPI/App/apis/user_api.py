from flask_restful import Resource


class UsersResource(Resource):
    def get(self):
        return {'msg': 'hello api'}

    def post(self):
        return {'msg': 'post ok'}


class UserResource(Resource):
    def get(self, id):
        return {"msg": "user ok " + str(id)}
