from flask import g
from flask_restful import Resource, reqparse, abort, marshal, fields

from App.apis.api_constant import HTTP_CREATE_OK
from App.apis.cinema_admin.utils import login_required
from App.models.cinema_admin.cinema_address_model import CinemaAddress
from App.models.cinema_admin.cinema_hall_model import Hall

parser = reqparse.RequestParser()
parser.add_argument("h_num", required=True, help="请提供放映厅编号")
parser.add_argument("h_seats", required=True, help="请提供放映厅布局")
parser.add_argument("h_address_id", required=True, help="请提供电影院地址")

hall_fields = {
    "h_address_id": fields.Integer,
    "h_num": fields.Integer,
    "h_seats": fields.String
}


class CinemaHallsResource(Resource):

    @login_required
    def post(self):
        args = parser.parse_args()
        h_num = args.get("h_num")
        h_seats = args.get("h_seats")
        address_id = args.get("h_address_id")
        cinema_addresses = CinemaAddress.query.filter_by(c_user=g.user.id).all()

        cinema_ids = [cinema_address.id for cinema_address in cinema_addresses]

        if address_id not in cinema_ids:
            abort(400, msg="error action")

        hall = Hall()
        hall.h_address_id = address_id
        hall.h_num = h_num
        hall.h_seats = h_seats

        if not hall.save():
            abort(400, msg="放映厅创建失败")

        data = {
            "msg": "create success",
            "status": HTTP_CREATE_OK,
            "data": marshal(hall, hall_fields)
        }

        return data
