from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from App.models import Student


def hello(request):
    return HttpResponse("Hello")


def index(request):
    # 本质上也是返回的HttpResponse，它帮我们把模板和Context数据渲染成字符串
    return render(request, 'index.html')


def get_students(request):
    students = Student.objects.all()

    student_dict = {
        'hobby': 'coding',
        'time': 'one year'
    }

    data = {
        'students': students,
        'student_dict': student_dict,
        'count': 5
    }

    return render(request, 'student_list.html', context=data)