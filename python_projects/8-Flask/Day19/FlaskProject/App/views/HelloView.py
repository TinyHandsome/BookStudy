import random

from flask import Blueprint, render_template

from App.ext import db
from App.models import News

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
    return render_template("NewsList.html", news_list=news_list)
