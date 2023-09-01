from flask import Flask, Blueprint, redirect, url_for, request

blue = Blueprint('blue', __name__)


def init_view(app: Flask):
    app.register_blueprint(blue)


@blue.route('/', methods=['GET', 'POST', 'DELETE'])
def index():
    return 'index'


@blue.route('/users/<int:id>')
def users(id):
    print(type(id))
    return 'Users API ' + str(id)


@blue.route('/getinfo/<string:token>/')
@blue.route('/gouzei/<int:token>/')
def get_info(token):
    print(token)
    print(type(token))
    return 'get success'


@blue.route('/getpath/<path:address>/')
def get_path(address):
    print(address)
    print(type(address))
    return 'Address Success'


@blue.route('/getuuid/<uuid:uu>/')
def get_uuid(uu):
    print(uu)
    print(type(uu))
    return 'UUID Success'


@blue.route('/getany/<any(a, b):an>/')
def get_any(an):
    print(an)
    print(type(an))
    return 'Any success'


@blue.route('/redirect/')
def red():
    # return redirect('/')
    return redirect(url_for('blue.get_any', an='a'))


@blue.route('/getrequest/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_request():
    print(request.host)
    print(request.url)

    if request.method == 'GET':
        return 'GET Success %s' % request.remote_addr
    elif request.method == 'POST':
        return 'POST Success'
    else:
        return '%s not support' % request.method

    # return 'Request success'
