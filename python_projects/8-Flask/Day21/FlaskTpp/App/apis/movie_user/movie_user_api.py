import uuid

from flask_restful import Resource, reqparse, abort, fields, marshal

from App.apis.api_constant import HTTP_CREATE_OK, USER_ACTION_REGISTER, USER_ACTION_LOGIN, HTTP_OK
from App.apis.movie_user.model_utils import get_user
from App.ext import cache
from App.models.movie_user import MovieUser

parse = reqparse.RequestParser()
parse.add_argument('username', type=str, required=True, help='请输入用户名')
parse.add_argument('password', type=str, required=True, help='请输入密码')
parse.add_argument('phone', type=str, required=True, help='请输入手机号')
parse.add_argument('action', type=str, required=True, help='请确认请求参数')

movie_user_fields = {
    'username': fields.String,
    'phone': fields.String,
    'password': fields.String(attribute="_password"),
}

single_movie_user_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.Nested(movie_user_fields)
}


class MovieUsersResource(Resource):

    def post(self):
        args = parse.parse_args()
        username = args.get('username')
        password = args.get('password')
        phone = args.get('phone')
        action = args.get('action').lower()

        if action == USER_ACTION_REGISTER:
            movie_user = MovieUser()
            movie_user.username = username
            movie_user.password = password
            movie_user.phone = phone

            if not movie_user.save():
                abort(400, msg='create fail')

            data = {
                'status': HTTP_CREATE_OK,
                'msg': '用户创建成功',
                'data': movie_user
            }

            return marshal(data, single_movie_user_fields)

        elif action == USER_ACTION_LOGIN:
            user = get_user(username) or get_user(phone)

            if not user:
                abort(400, msg='用户不存在')

            if not user.check_password(password):
                abort(401, msg='密码错误')

            token = uuid.uuid4().hex
            cache.set(token, user.id, timeout=60 * 60 * 24 * 7)

            data = {
                'msg': 'login success',
                'status': HTTP_OK,
                'token': token
            }

            return data

        else:
            abort(400, msg='请提供正确的参数')
