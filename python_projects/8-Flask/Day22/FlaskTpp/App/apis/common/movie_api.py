from flask_restful import Resource, reqparse, abort

from App.apis.admin.utils import login_required
from App.models.common.movie_model import Movie

parse = reqparse.RequestParser()
parse.add_argument("showname", required=True, help="must supply showname")
parse.add_argument("shownameen", required=True, help="must supply shownameen")
parse.add_argument("director", required=True, help="must supply director")
parse.add_argument("leadingRole", required=True, help="must supply leadingRole")
parse.add_argument("type", required=True, help="must supply type")
parse.add_argument("country", required=True, help="must supply country")
parse.add_argument("language", required=True, help="must supply language")
parse.add_argument("duration", required=True, help="must supply duration")
parse.add_argument("screeningmodel", required=True, help="must supply screeningmodel")
parse.add_argument("openday", required=True, help="must supply openday")
parse.add_argument("backgroundpicture", required=True, help="must supply backgroundpicture")


class MoviesResource(Resource):
    def get(self):
        return {'msg': 'get ok'}

    @login_required
    def post(self):
        args = parse.parse_args()
        showname = args.get('showname')
        shownameen = args.get('shownameen')
        director = args.get('director')
        leadingRole = args.get('leadingRole')
        type = args.get('type')
        country = args.get('country')
        language = args.get('language')
        duration = args.get('duration')
        screeningmodel = args.get('screeningmodel')
        openday = args.get('openday')
        backgroundpicture = args.get('backgroundpicture')

        movie = Movie()
        if not movie.save():
            abort(400, )

        return {'msg': 'post ok'}


class MovieResource(Resource):
    def get(self):
        return {'msg': 'get ok'}

    @login_required
    def patch(self):
        return {'msg': 'patch ok'}

    @login_required
    def put(self):
        return {'msg': 'put ok'}

    @login_required
    def delete(self):
        return {'msg': 'delete ok'}
