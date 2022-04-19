from flask import g
from flask_restful import Resource, reqparse, abort, fields, marshal

from App.apis.api_constant import HTTP_CREATE_OK
from App.apis.cinema_admin.utils import login_required
from App.models.cinema_admin.cinema_address_model import CinemaAddress
from App.models.cinema_admin.cinema_hall_model import Hall
from App.models.cinema_admin.cinema_hall_movie_model import HallMovie
from App.models.cinema_admin.cinema_movie_model import CinemaMovie

parse = reqparse.RequestParser()
parse.add_argument("movie_id", required=True, help="请选择电影")
parse.add_argument("hall_id", required=True, help="请选择大厅")
parse.add_argument("h_time", required=True, help="请选择排挡时间")

hall_movie_fields = {
    "h_movie_id": fields.Integer,
    "h_hall_id": fields.Integer,
    "h_time": fields.DateTime,
}


class CinemaMovieHallResource(Resource):
    def get(self):
        return {"msg": "get ok"}

    @login_required
    def post(self):
        args = parse.parse_args()

        movie_id = args.get("movie_id")
        hall_id = args.get("hall_id")
        h_time = args.get("h_time")

        # 验证 movie id 是否已经购买
        cinema_movies = CinemaMovie.query.filter_by(c_cinema_id=g.user.id).all()
        movie_ids = [cinema_movie.c_movie_id for cinema_movie in cinema_movies]
        if movie_id not in movie_ids:
            abort(403, msg="电影未被授权")

        # hall id是否是咱们用户的
        # h_time 不低于当前时间
        # 同时间的同影厅是否有不同的排挡
        cinema_addresses = CinemaAddress.query.filter_by(c_user=g.user.id)
        all_halls = []
        for cinema_address in cinema_addresses:
            halls = Hall.query.filter_by(h_address_id=cinema_address.id).all()
            all_halls.append(halls)
        all_hall_ids = [hall.id for hall in all_halls]
        if hall_id not in all_hall_ids:
            abort(403, msg="大厅选择错误")

        hall_movie = HallMovie()
        hall_movie.h_movie_id = movie_id
        hall_movie.h_hall_id = hall_id
        hall_movie.h_time = h_time

        if not hall_movie.save():
            abort(400, msg="排挡失败")

        data = {
            "status": HTTP_CREATE_OK,
            "msg": "ok",
            "data": marshal(hall_movie, hall_movie_fields)
        }

        return data
