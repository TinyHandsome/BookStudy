from flask_restful import Resource, fields, marshal

from App.apis.api_constant import HTTP_OK
from App.models.common.city_model import City, Letter

city_fields = {
    'id': fields.Integer(attribute='c_id'),
    'parentId': fields.Integer(attribute='c_parent_id'),
    'regionName': fields.String(attribute='c_region_name'),
    'cityCode': fields.Integer(attribute='c_city_code'),
    'pinYin': fields.String(attribute='c_pinyin')
}


class CitiesResource(Resource):
    def get(self):
        letters = Letter.query.all()
        letters_cities = {}

        letters_cities_fields = {}

        for letter in letters:
            letter_cities = City.query.filter_by(letter_id=letter.id)
            letters_cities[letter.letter] = letter_cities

            letters_cities_fields[letter.letter] = fields.List(fields.Nested(city_fields))

        data = {
            'msg': 'ok',
            'status': HTTP_OK,
            'data': marshal(letters_cities, letters_cities_fields)
        }

        return data
