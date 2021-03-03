from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('Hello Two')


def login(request):
    if request.method == 'GET':
        return render(request, 'two_login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        request.session['username'] = username
        return HttpResponse("登录成功")


def mine(request):
    username = request.session.get('username')
    return HttpResponse(username)