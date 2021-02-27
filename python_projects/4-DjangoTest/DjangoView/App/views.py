import random

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def hello(request):
    response = HttpResponse()
    # response.content = '德玛西亚'
    # response.status_code = 404
    response.write('听说马桶堵了')
    response.flush()
    return response


def get_ticket(request):
    if random.randrange(10) > 5:
        # 反向解析
        url = reverse('app:hello')
        # return HttpResponseRedirect(url)
        return redirect(url)
    return HttpResponse('恭喜你抢到票了！')


def get_info(request):
    data = {
        "status": 200,
        "msg": "ok"
    }
    return JsonResponse(data=data)


def set_cookie(request):
    response = HttpResponse("设置Cookie")
    response.set_cookie('username', 'Rock')
    return response


def get_cookie(request):
    username = request.COOKIES.get("username")
    return HttpResponse(username)


def login(request):
    return render(request, 'login.html')


def dologin(request):
    uname = request.POST.get('uname')
    response = HttpResponseRedirect(reverse('app:mine'))
    response.set_cookie('uname', uname)
    return response


def mine(request):
    uname = request.COOKIES.get('uname')
    if uname:
        return HttpResponse(uname)
    else:
        return redirect(reverse('app:login'))