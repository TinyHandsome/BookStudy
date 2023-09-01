from random import random

from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
from Two.models import Student


def index(request):
    return HttpResponse("Two Index! ")


def addstudent(request):
    student = Student()
    student.s_name = 'Jerry-%d' % random.randrange(100)
    student.save()

    return HttpResponse("Add Successs %s" % student.s_name)


def get_students(request):
    students = Student.objects.all()
    for stu in students:
        print(stu.s_name)

    context = {
        "hobby": "Play Games",
        "eat": "Meat",
        "students": students,
    }

    return render(request, "student_list2.html", context=context)


def update_student(request):
    # 查找主键为2的学生
    student = Student.objects.get(pk=2)
    student.s_name = 'Litian'
    student.save()

    return HttpResponse("Student update success")


def delete_student(request):
    student = Student.objects.get(pk=3)
    student.delete()
    return HttpResponse("删除学生成功！")