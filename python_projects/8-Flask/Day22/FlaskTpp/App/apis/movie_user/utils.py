from flask import request, g
from flask_restful import abort
from App.apis.movie_user.model_utils import get_user
from App.ext import cache


def _verify():
    token = request.args.get('token')

    if not token:
        abort(401, msg='not login')

    user_id = cache.get(token)
    if not user_id:
        abort(401, msg='user not available')

    user = get_user(user_id)

    if not user:
        abort(401, msg='user not available')

    g.user = user
    g.auth = token


def login_required(fun):
    def wrapper(*args, **kwargs):
        _verify()

        return fun(*args, **kwargs)

    return wrapper


def require_permission(permission):
    def require_permission_wrapper(func):
        def wrapper(*args, **kwargs):
            _verify()

            if not g.user.check_permission(permission):
                abort(403, msg='user can not access')

            return func(*args, **kwargs)

        return wrapper

    return require_permission_wrapper
