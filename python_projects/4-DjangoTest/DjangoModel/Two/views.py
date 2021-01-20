from django.shortcuts import render
from django.shortcuts import HttpResponse

from Two.models import User


def get_user(request):
    username = "Sunck"
    password = "123"

    users = User.objects.filter(u_name=username)
    print(users.count())

    # if users.count():
    if users.exists():
        user = users.first()
        if user.u_password == password:
            print("获取用户信息成功")
        else:
            print("密码错误")
    else:
        print("用户不存在！")

    return HttpResponse('获取成功')
