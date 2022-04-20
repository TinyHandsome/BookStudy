import datetime

from flask import g
from flask_restful import Resource, reqparse, abort, fields, marshal

from App.apis.api_constant import HTTP_CREATE_OK
from App.apis.movie_user.utils import login_required, require_permission
from App.models.movie_user import VIP_USER, COMMON_USER
from App.models.movie_user.movie_order_model import MovieOrder

parse = reqparse.RequestParser()
# parse.add_argument("token", required=True, help="请登录")
parse.add_argument("hall_movie_id", required=True, help="请提供排挡信息")
parse.add_argument("o_seats", required=True, help="请正确选择座位")

movie_order_fields = {
    "o_price": fields.Float,
    "o_seats": fields.String,
    "o_hall_movie": fields.Integer,
}


class MovieOrdersResource(Resource):

    @login_required
    def post(self):
        args = parse.parse_args()
        hall_movie_id = args.get("hall_movie_id")
        o_seats = args.get("o_seats")
        user = g.user

        movie_order = MovieOrder()
        movie_order.o_hall_movie = hall_movie_id
        movie_order.o_seats = o_seats
        movie_order.o_user_id = user.id
        movie_order.o_time = datetime.datetime.now() + datetime.timedelta(minutes=15)

        if not movie_order.save():
            abort(400, msg="下单失败")

        data = {
            "msg": "success",
            "status": HTTP_CREATE_OK,
            "data": marshal(movie_order, movie_order_fields)
        }

        return data


class MovieOrderResource(Resource):

    @require_permission(VIP_USER)
    def put(self, order_id):
        return {'msg': "change success"}
