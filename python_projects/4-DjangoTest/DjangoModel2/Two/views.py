from django.http import HttpResponse
from django.shortcuts import render


from Two.models import Person, IDCard


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