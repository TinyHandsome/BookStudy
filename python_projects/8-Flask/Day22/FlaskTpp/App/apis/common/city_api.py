from flask_restful import Resource

from App.models.common.city_model import City


class CitiesResource(Resource):
    def get(self):

        return {'msg': 'city list'}