from flask import Flask
from flask_script import Manager

from FlaskMultiProject import create_app

app = create_app()
manager = Manager(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
