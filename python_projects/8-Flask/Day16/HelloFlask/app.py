from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    a = 10
    b = 6
    f = 9
    c = 0
    result = (a + b + f) / c

    return '<h1>今天居然下雨了</h1> %d' % result


if __name__ == '__main__':
    app.run(debug=True)
