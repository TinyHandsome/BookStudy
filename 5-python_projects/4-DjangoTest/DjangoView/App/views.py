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
    # response.set_cookie('uname', uname, max_age=60)
    response.set_signed_cookie('content', uname, "Rock")
    return response


def mine(request):
    # uname = request.COOKIES.get('content')
    try:
        uname = request.get_signed_cookie('content', salt="Rock")
        if uname:
            # return HttpResponse(uname)
            return render(request, "mine.html", context={"uname": uname})
    except Exception as e:
        print("获取失败")

    return redirect(reverse('app:login'))


def logout(request):
    response = redirect(reverse("app:login"))
    response.delete_cookie("content")
    return response