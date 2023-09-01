import datetime

from flask_restful import Resource, reqparse, fields, marshal
from sqlalchemy import or_

from App.apis.api_constant import HTTP_OK
from App.apis.movie_user.utils import login_required
from App.models.cinema_admin.cinema_address_model import CinemaAddress
from App.models.cinema_admin.cinema_hall_model import Hall
from App.models.cinema_admin.cinema_hall_movie_model import HallMovie
from App.models.movie_user.movie_order_model import MovieOrder, ORDER_STATUS_PAYED_NOT_GET, ORDER_STATUS_GET, \
    ORDER_STATUS_NOT_PAY

parse = reqparse.RequestParser()
parse.add_argument("address_id")
parse.add_argument("district")
parse.add_argument("movie_id")

hall_movie_fields = {
    "id": fields.Integer,
    "h_movie_id": fields.Integer,
    "h_hall_id": fields.Integer,
    "h_time": fields.DateTime
}

multi_hall_movie_fields = {
    "msg": fields.String,
    "status": fields.Integer,
    "data": fields.List(fields.Nested(hall_movie_fields))
}


class UserMovieHallsResource(Resource):
    def get(self):
        args = parse.parse_args()

        movie_id = args.get("movie_id")
        address_id = args.get("address_id")
        district = args.get("district")

        cinema_address = CinemaAddress.query.filter(CinemaAddress.district == district).filter(
            CinemaAddress.id == address_id).first()

        halls = Hall.query.filter_by(h_address_id=cinema_address.id).all()
        all_hall_movies = []
        for hall in halls:
            hall_movies = HallMovie.query.filter_by(h_hall_id=hall.id).filter_by(h_movie_id=movie_id).all()
            all_hall_movies += hall_movies

        data = {
            "msg": "ok",
            "status": HTTP_OK,
            "data": all_hall_movies
        }

        return marshal(data, multi_hall_movie_fields)


hall_fields = {
    "h_address_id": fields.Integer,
    "h_num": fields.Integer,
    "h_seats": fields.String
}


class UserMovieHallResource(Resource):
    @login_required
    def get(self, id):
        hall_movie = HallMovie.query.get(id)
        hall = Hall.query.get(hall_movie.h_hall_id)

        # 订单筛选 排挡筛选 订单状态 锁单的

        movie_orders_buyed = MovieOrder.query.filter(MovieOrder.o_hall_movie == id).filter(
            or_(MovieOrder.o_status == ORDER_STATUS_PAYED_NOT_GET, MovieOrder.o_status == ORDER_STATUS_GET)).all()
        movie_orders_lock = MovieOrder.query.filter(MovieOrder.o_hall_movie == id).filter(
            MovieOrder.o_status == ORDER_STATUS_NOT_PAY).filter(
            MovieOrder.o_time > datetime.datetime.now()).all()

        seats = []
        for movie_orders in movie_orders_buyed:
            sold_seats = movie_orders.o_seats.split("#")
            seats += sold_seats
        for movie_orders in movie_orders_lock:
            sold_seats = movie_orders.o_seats.split("#")
            seats += sold_seats

        all_seats = hall.h_seats.split("#")
        can_buy = list(set(all_seats) - set(seats))
        hall.h_seats = "#".join(can_buy)

        data = {
            "msg": "ok",
            "status": HTTP_OK,
            "data": marshal(hall, hall_fields)
        }

        return data
