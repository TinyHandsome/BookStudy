import random
from time import sleep

from django.core.cache import cache, caches
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse('Index')


# @cache_page(30)
def news(request):
    temp_cache = caches['redis_backend']
    result = temp_cache.get("news")
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


def home(request):
    return HttpResponse("Home")


def get_phone(request):
    if random.randrange(100) > 95:
        return HttpResponse("恭喜您，抢到小米8了！")
    return HttpResponse("正在排队。。。")


def get_ticket(request):
    if random.randrange(100) > 10:
        return HttpResponse("还剩余99张满100-99")
    return None


def search(request):
    return HttpResponse("这是你搜索到的种子资源")


def calc(request):
    a = 250
    b = 250
    result = (a + b) / 0
    return HttpResponse(result)


@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        return HttpResponse("POST请求成功！")
    return None
