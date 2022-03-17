from flask import request
from flask_restful import Resource, abort, fields, marshal_with, marshal

from App.models import Goods

goods_field = {
    'g_name': fields.String,
    'g_price': fields.Float
}

single_goods_fields = {
    'data': fields.Nested(goods_field),
    'status': fields.Integer,
    "msg": fields.String
}


class GoodsListResource(Resource):

    def get(self):
        return ''

    @marshal_with(single_goods_fields)
    def post(self):
        g_name = request.form.get('g_name')
        g_price = request.form.get('g_price')

        goods = Goods()
        goods.g_name = g_name
        goods.g_price = g_price

        if not goods.save():
            abort(400)

        """
            JSON
                Response
            格式
                单个对象
                {
                    "status": 200,
                    "msg": "ok",
                    "data": {
                        "property": "value
                    }
                }
                多个对象
                {
                    "status": 200,
                    "msg": "ok",
                    "data": [
                        {}, {}, {}
                    ]
                }
        """

        data = {
            "msg": "create success",
            "status": 201,
            # "data": marshal(goods, goods_field)
            "data": goods
        }

        return data
