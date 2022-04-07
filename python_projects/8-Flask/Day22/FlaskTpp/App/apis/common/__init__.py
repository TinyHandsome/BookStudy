from flask_restful import Api

from App.apis.common.city_api import CitiesResource
from App.apis.common.movie_api import MoviesResource

common_api = Api(prefix='/common')


common_api.add_resource(CitiesResource, '/cities/')
common_api.add_resource(MoviesResource, '/movies/')