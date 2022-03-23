from flask_restful import Resource


class MovieUsersResource(Resource):

    def post(self):
        return {'msg': 'ok'}

