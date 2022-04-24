import datetime

from flask import g
from flask_restful import Resource, reqparse, abort, fields, marshal
from sqlalchemy import or_

from App.apis.api_constant import HTTP_CREATE_OK
from App.apis.movie_user.utils import login_required, require_permission
from App.ext import db
from App.models.cinema_admin.cinema_hall_model import Hall
from App.models.cinema_admin.cinema_hall_movie_model import HallMovie
from App.models.movie_user import VIP_USER, COMMON_USER
from App.models.movie_user.movie_order_model import MovieOrder, ORDER_STATUS_PAYED_NOT_GET, ORDER_STATUS_NOT_PAY, \
    ORDER_STATUS_GET

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

        # 订单筛选 排挡筛选 订单状态 锁单的
        movie_orders_buyed = MovieOrder.query.filter(MovieOrder.o_hall_movie == hall_movie_id).filter(
            or_(MovieOrder.o_status == ORDER_STATUS_PAYED_NOT_GET, MovieOrder.o_status == ORDER_STATUS_GET)).all()
        movie_orders_lock = MovieOrder.query.filter(MovieOrder.o_hall_movie == hall_movie_id).filter(
            MovieOrder.o_status == ORDER_STATUS_NOT_PAY).filter(
            MovieOrder.o_time > datetime.datetime.now()).all()

        seats = []
        for movie_orders in movie_orders_buyed:
            sold_seats = movie_orders.o_seats.split("#")
            seats += sold_seats
        for movie_orders in movie_orders_lock:
            sold_seats = movie_orders.o_seats.split("#")
            seats += sold_seats

        hall_movie = HallMovie.query.get(hall_movie_id)
        hall = Hall.query.get(hall_movie.h_hall_id)

        all_seats = hall.h_seats.split("#")
        # 所有的座位减去不能选的座位，就是可以买的座位
        can_buy = list(set(all_seats) - set(seats))
        want_buy = o_seats.split("#")

        for item in want_buy:
            if item not in can_buy:
                abort(400, msg="锁座失败")

        # if set(want_buy) > set(can_buy):
        #     abort(400, msg="锁座失败")

        user = g.user

        movie_order = MovieOrder()
        movie_order.o_hall_movie = hall_movie_id
        movie_order.o_seats = o_seats
        movie_order.o_user_id = user.id
        movie_order.o_time = datetime.datetime.now() + datetime.timedelta(minutes=15)

        # 悲观加锁
        # db.session.with_lockmode("update")
        # 针对此次操作加锁
        # db.session.Query(MovieOrder).with_lockmode("update")
        # db.session.commit()

        # 事务
        # 保证代码完整执行
        # 事务开启、提交、回滚

        # db.session.rollback()

        # try:
        #     movie_order = MovieOrder.query.get(1)
        #     movie_order2 = MovieOrder.query.get(2)
        #
        #     db.session.delete(movie_order)
        #     db.session.delete(movie_order2)
        # except Exception as e:
        #     print(e)
        #     db.session.rollback()
        # else:
        #     db.session.commit()

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
