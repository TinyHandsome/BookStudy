from django.http import HttpResponse
from django.shortcuts import render

from Two.models import Person, IDCard, Customer, Goods, Cat, Dog


def hello(request):
    return HttpResponse('Two hello')


def add_person(request):
    username = request.GET.get("username")
    person = Person()
    person.p_name = username
    person.save()
    return HttpResponse("Person创建成功 %d" % person.id)


def add_id_card(request):
    id_num = request.GET.get('id_num')
    id_card = IDCard()
    id_card.id_num = id_num
    id_card.save()
    return HttpResponse("IDCard %d" % id_card.id)


def bind_card(request):
    person = Person.objects.last()
    id_card = IDCard.objects.last()
    id_card.id_person = person
    id_card.save()
    return HttpResponse("绑定成功")


def remove_person(request):
    person = Person.objects.last()
    person.delete()
    return HttpResponse("人员移除成功")


def remove_id_card(request):
    idcard = IDCard.objects.last()
    idcard.delete()
    return HttpResponse("身份证移除成功")


def get_person(request):
    idcard = IDCard.objects.last()
    person = idcard.id_person
    return HttpResponse(person.p_name)


def get_id_card(request):
    person = Person.objects.last()
    person = Person()
    idcard = person.idcard
    return HttpResponse(idcard.id_num)


def add_customer(request):
    c_name = request.GET.get("cname")
    customer = Customer()
    customer.c_name = c_name
    customer.save()
    return HttpResponse('创建消费者成功 %d' % customer.id)


def add_goods(request):
    g_name = request.GET.get("gname")
    goods = Goods()
    goods.g_name = g_name
    goods.save()
    return HttpResponse("创建商品成功 %d" % goods.id)


def add_to_cart(request):
    customer = Customer.objects.last()
    goods = Goods.objects.last()
    # goods.g_customer.add(customer)
    # goods.g_customer.remove(customer)
    customer.goods_set.add(goods)

    return HttpResponse("添加成功")


def get_goods_list(request, customerid):
    customer = Customer.objects.get(pk=customerid)
    goods_list = customer.goods_set.all()
    return render(request, 'goodslist.html', context=locals())


def add_cat(request):
    cat = Cat()
    cat.a_name = "Tom"
    cat.c_eat = 'Fish'
    cat.save()
    return HttpResponse("Cat 创建成功 %d" % cat.id)


def add_dog(request):
    dog = Dog()
    dog.a_name = "Gouzei"
    dog.save()
    return HttpResponse("Dog 创建成功 %d" % dog.id)
