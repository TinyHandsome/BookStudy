import hashlib
import time
from random import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from Two.models import Student


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
    return render(request, 'two_mine.html', context=locals())


def logout(request):
    response = redirect(reverse('two:mine'))

    # 删除Cookie
    # response.delete_cookie('sessionid')
    # 删除Session
    # del request.session['username']

    # 上面的删除方法不能完全删除，用下面的方式完全删除
    # session和cookie一起干掉
    request.session.flush()

    return response


def register(request):
    if request.method == "GET":
        return render(request, 'student_register.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            student = Student()
            student.s_name = username
            student.s_password = password
            student.save()
        except Exception as e:
            return redirect(reverse("two:register"))

        return HttpResponse("注册成功")


def student_login(request):
    if request.method == "GET":
        return render(request, 'student_login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        students = Student.objects.filter(s_name=username).filter(s_password=password)
        if students.exists():
            student = students.first()

            ip = request.META.get("REMOTE_ADDR")
            token = generate_token(ip, username)
            student.s_token = token

            student.save()
            response = HttpResponse("用户登录成功")
            response.set_cookie("token", token)

            ''' 移动端用JsonResponse返回
            data = {
                "status": 200,
                "msg": "login success",
                "token": token
            }
            return JsonResponse(data=data)

            '''
            return response

        return redirect(reverse("two:student_login"))


def generate_token(ip, username):
    c_time = time.ctime()
    r = username
    return hashlib.new('md5', (ip + c_time + r).encode('utf-8')).hexdigest()


def student_mine(request):
    token = request.COOKIES.get('token')
    try:
        student = Student.objects.get(s_token=token)
    except Exception as e:
        return redirect(reverse('two:student_login'))
    return HttpResponse(student.s_name)
