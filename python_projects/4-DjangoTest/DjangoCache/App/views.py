from time import sleep

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views.decorators.cache import cache_page


def index(request):
    return HttpResponse('Index')


@cache_page(30)
def news(request):
    news_list = []
    for i in range(10):
        news_list.append("最近贸易战又开始了 %d" % i)

    sleep(5)

    data = {
        'news_list': news_list
    }

    return render(request, 'news.html', context=data)