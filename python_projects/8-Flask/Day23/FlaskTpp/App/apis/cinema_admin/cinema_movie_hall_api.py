from flask_restful import Resource, reqparse

from App.apis.cinema_admin.utils import login_required

parse = reqparse.RequestParser()
parse.add_argument("movie_id", required=True, help="请选择电影")
parse.add_argument("hall_id", required=True, help="请选择大厅")
parse.add_argument("h_time", required=True, help="请选择排挡时间")


class CinemaMovieHallResource(Resource):
    def get(self):
        return {"msg": "get ok"}

    @login_required
    def post(self):
        args = parse.parse_args()

        movie_id = args.get("movie_id")
        hall_id = args.get("hall_id")
        h_time = args.get("h_time")

        return {"msg": "post ok"}
