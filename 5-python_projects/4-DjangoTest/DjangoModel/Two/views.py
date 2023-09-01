from django.db.models import Max, Avg, F, Q
from django.shortcuts import render
from django.shortcuts import HttpResponse

from Two.models import *


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


def get_users(request):
    # 左闭右开
    users = User.objects.all()[1:3]
    context = {
        'users': users
    }

    return render(request, 'user_list.html', context=context)


def get_orders(request):
    orders = Order.objects.filter(o_time__year=2021, o_time__month=8)
    for order in orders:
        print(order.o_num)

    return HttpResponse('获取订单成功')


# 级联查询
def get_grades(request):
    grades = Grade.objects.filter(student__s_name='李四')
    for grade in grades:
        print(grade.g_name)
    return HttpResponse('获取成功')


def get_customer(request):
    result = Customer.objects.aggregate(Max("c_cost"))
    avg = Customer.objects.aggregate(Avg('c_cost'))
    print(result, avg)
    return HttpResponse('获取花费成功')


def get_company(request):
    # 获取女生比男生多的公司
    # companies = Company.objects.filter(c_boy_num__lt=F('c_girl_num'))

    # 获取女生比男生多15以上的公司
    # companies = Company.objects.filter(c_boy_num__lt=F('c_girl_num')-15)

    # 公司男生人数多于1个，同时女生人数多于5个
    # companies = Company.objects.filter(c_boy_num__gt=1).filter(c_girl_num__gt=10)
    companies = Company.objects.filter(Q(c_boy_num__gt=1) & Q(c_girl_num__gt=10))

    for company in companies:
        print(company.c_name)
    return HttpResponse('获取公司成功')


def get_animals(request):
    # animals = Animal.a_m.filter(is_delete=False)
    animals = Animal.objects.all()

    for animal in animals:
        print(animal.a_name)

    a = Animal.objects.create_animal("狗子")
    print('aaa', type(a))

    b = Animal()
    b.a_name = 'qq'
    print('bbb', type(b))
    b.save()
    a.save()

    return HttpResponse("动物获取成功")