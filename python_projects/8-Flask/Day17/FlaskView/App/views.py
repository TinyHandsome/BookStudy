from flask import Blueprint, request, render_template, make_response

blue = Blueprint('blue', __name__)


def init_blue(app):
    app.register_blueprint(blue)


@blue.route("/")
def index():
    return "index"


@blue.route('/sendrequest/')
def send_request():
    print(request.args)
    print(type(request.args))
    print(request.form)
    return 'success'


@blue.route('/getresponse/')
def get_response():
    # return 'response', 400
    # result = render_template('Hello.html')
    # print(result)
    # print(type(result))
    # return result

    response = make_response("<h2>皮卡</h2>")
    print(response)
    print(type(response))
    return response
