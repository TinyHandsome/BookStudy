from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello(request):
    return HttpResponse("双击666")


def hh(request):
    return HttpResponse('呵呵')


def haha(request):
    return HttpResponse("<h1>睡觉的站起来！<h1>")


def index(request):
    return render(request, 'index.html')


def wengui(request):
    return HttpResponse("<h1>憨批文贵！</h1>")


def home(request):
    return render(request, 'home.html')