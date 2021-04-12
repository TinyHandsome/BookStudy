from time import sleep

from django.core.cache import cache
from django.core.checks import caches
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page


def index(request):
    return HttpResponse('Index')


# @cache_page(30)
def news(request):
    cache = caches['redis_backend']
    result = cache.get("news")
    # 如果缓存中能找到news对应的值，直接返回该值
    if result:
        return HttpResponse(result)

    news_list = []
    for i in range(10):
        news_list.append("最近贸易战又开始了 %d" % i)

    sleep(5)

    data = {
        'news_list': news_list
    }

    # 如果缓存中没有找到news的值，则返回response，并将内容写入到缓存中
    response = render(request, 'news.html', context=data)
    cache.set('news', response.content, timeout=60)

    return response


@cache_page(60, cache='redis_backend')
def jokes(request):
    sleep(5)
    return HttpResponse('狗贼')
