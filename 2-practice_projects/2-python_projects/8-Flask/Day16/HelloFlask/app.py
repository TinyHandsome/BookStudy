from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def hello_world():
    a = 10
    b = 6
    f = 9
    c = 0
    # result = (a + b + f) / c

    # return '<h1>今天居然下雨了</h1> %d' % result
    return 'Hello World'


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=8000)
    manager.run()
