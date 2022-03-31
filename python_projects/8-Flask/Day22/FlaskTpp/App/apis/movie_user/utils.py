from flask import request
from flask_restful import abort

from App.apis.movie_user.model_utils import get_user
from App.ext import cache


def login_required():
    token = request.args.get('token')

    if not token:
        abort(401, msg='not login')

    user_id = cache.get(token)
    if not user_id:
        abort(401, msg='user not available')

    user = get_user(user_id)

    if not user:
        abort(401, msg='user not available')

