import os
from flask_script import Manager

from App import create_app

env = os.environ.get('FLASK_ENV')
app = create_app(env)


manager = Manager(app)


if __name__ == '__main__':
    app.run()
