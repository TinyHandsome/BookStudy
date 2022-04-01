from flask import g
from flask_restful import Resource, reqparse, abort
from App.apis.movie_user.utils import login_required, require_permission
from App.models.movie_user import VIP_USER, COMMON_USER

parse = reqparse.RequestParser()
parse.add_argument("token", required=True, help="请登录")


class MovieOrdersResource(Resource):

    @login_required
    def post(self):
        user = g.user

        return {'msg': 'post order ok'}


class MovieOrderResource(Resource):

    @require_permission(VIP_USER)
    def put(self, order_id):
        return {'msg': "change success"}
