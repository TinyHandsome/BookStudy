import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Person


def add_persons(request):
    for i in range(15):
        person = Person()
        flag = random.randrange(100)
        person.p_name = "Tom%d" % i
        person.p_age = flag
        person.p_sex = flag % 2
        person.save()

    return HttpResponse('批量创建成功')


def get_persons(request):
    # 查找大于18的年纪的人
    # persons = Person.objects.filter(p_age__gt=50).filter(p_age__lt=80)
    # 另一种用法
    # persons = Person.objects.exclude(p_age__lt=50)
    persons = Person.objects.all()

    context = {
        'persons': persons
    }

    return render(request, 'person_list.html', context)


def add_person(request):
    person = Person.objects.create(p_name="Sunck1", p_age=15, p_sex=True)
    person.save()
    return HttpResponse("Sunck1创建成功")
