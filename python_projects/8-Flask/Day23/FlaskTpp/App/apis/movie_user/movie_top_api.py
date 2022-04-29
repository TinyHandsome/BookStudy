from flask_restful import Resource

from App.ext import db
from App.models.common.movie_model import Movie


class MovieTopResource(Resource):

    def get(self):
        # Movie.query.get(2)
        movie = db.session.query(Movie).get(2)
        print(movie)

        data = {
            "msg": "ok"
        }

        return data
