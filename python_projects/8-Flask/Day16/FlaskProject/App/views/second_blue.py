from flask import Blueprint

second = Blueprint('second', __name__)


@second.route('/hello/')
def hello():
    return 'Second Blue'
