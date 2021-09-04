from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def market(request):
    return render(request, 'main/market.html')