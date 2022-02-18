from flask import Blueprint, request, render_template, make_response, Response, abort, session

blue = Blueprint('blue', __name__)


def init_blue(app):
    app.register_blueprint(blue)


@blue.route("/")
def index():
    return render_template('index.html')


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

    # response = make_response("<h2>皮卡</h2>")
    # print(response)
    # print(type(response))

    abort(404)

    response = Response("自己造一个DIY")

    return response


@blue.errorhandler(404)
def handle_error(error):
    print(error)
    print(type(error))

    return 'What?'


@blue.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        username = request.form.get("username")
        response = Response("登录成功%s" % username)
        # response.set_cookie('username', username)
        session['username'] = username
        return response


@blue.route('/mine/')
def mine():
    username = session.get('username')
    return '欢迎回来: %s' % username


@blue.route('/students/')
def students():
    student_list = ["小明{}".format(i) for i in range(10)]
    return render_template('Students.html', student_list=student_list)


@blue.route('/userregister/')
def user_register():
    return render_template('user/user_register.html', title='用户注册')


@blue.route('/userregister2/')
def user_register2():
    users = ["小白用户%d" % i for i in range(10)]
    return render_template('user/user_register2.html', title='用户注册2', users=users, msg="helloMyloVe")
