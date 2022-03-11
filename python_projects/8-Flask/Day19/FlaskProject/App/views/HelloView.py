import base64
import os
import random
import time

from flask import Blueprint, render_template, request

from App.ext import db
from App.models import News
from App.settings import BASE_DIR

blue = Blueprint('blue', __name__)


@blue.route('/')
def index():
    return 'Index'


@blue.route('/addnews/')
def add_news():
    news = News()
    news.n_title = "周润发%d" % random.randrange(10000)
    news.n_content = "福利社会%d" % random.randrange(10000)

    db.session.add(news)
    db.session.commit()

    return 'Add Success'


@blue.route('/getnews/')
def get_news():
    news_list = News.query.all()
    news_content = render_template("news_content.html", news_list=news_list)

    encode_content = base64.standard_b64encode(news_content.encode("utf-8")).decode("utf-8")
    print(encode_content)

    add_content_encode_content = "CHKa2GFL1twhMDhEZVfDfU2DoZHCLZk" + encode_content + "qOq3kRIxs26rmRtsUTJvBn9Z"
    print(add_content_encode_content)
    encode_content_twice = base64.standard_b64encode(add_content_encode_content.encode("utf-8")).decode("utf-8")
    print(encode_content_twice)

    return render_template("NewsList.html", news_content=news_content, encode_content_twice=encode_content_twice)


@blue.route('/getshow/')
def get_show():
    t = request.args.get('t')
    print(t)
    c = time.time() * 1000
    print(str(c))
    try:
        t = int(t)
    except:
        return '2'

    if c - t < 1000 and c > t:

        with open(os.path.join(BASE_DIR, 'App/static/js/show.js'), 'r') as file:
            js_content = file.read()

        return js_content

    else:
        return '1'
