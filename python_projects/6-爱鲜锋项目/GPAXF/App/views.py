from django.http import HttpResponse
from django.shortcuts import render

from App.models import MainWheel


def home(request):
    main_wheels =  MainWheel.objects.all()

    data = {
        "title": "首页",
        "main_wheels": main_wheels,
    }
    return render(request, 'main/home.html', context=data)


def market(request):
    return render(request, 'main/market.html')


def cart(request):
    return render(request, 'main/cart.html')


def mine(request):
    return render(request, 'main/mine.html')