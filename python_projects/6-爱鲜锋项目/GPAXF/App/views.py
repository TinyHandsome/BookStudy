from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from App.models import MainWheel, MainNav, MainMustBuy, MainShop, MainShow, FoodType, Goods


def home(request):
    main_wheels = MainWheel.objects.all()
    main_navs = MainNav.objects.all()
    main_mustbuys = MainMustBuy.objects.all()
    main_shops = MainShop.objects.all()

    main_shop0_1 = main_shops[0: 1]
    main_shop1_3 = main_shops[1: 3]
    main_shop3_7 = main_shops[3: 7]
    main_shop7_11 = main_shops[7: 11]
    main_shows = MainShow.objects.all()

    data = {
        "title": "首页",
        "main_wheels": main_wheels,
        "main_navs": main_navs,
        "main_mustbuys": main_mustbuys,
        "main_shop0_1": main_shop0_1,
        "main_shop1_3": main_shop1_3,
        "main_shop3_7": main_shop3_7,
        "main_shop7_11": main_shop7_11,
        "main_shows": main_shows,
    }
    return render(request, 'main/home.html', context=data)


def market(request):
    return redirect(reverse('axf:market_with_params', kwargs={
        "typeid": 104749
    }))


def market_with_params(request, typeid):
    foodtypes = FoodType.objects.all()
    goods_list = Goods.objects.filter(categoryid=typeid)

    data = {
        "title": "闪购",
        "foodtypes": foodtypes,
        "goods_list": goods_list,
        "typeid": int(typeid),
    }

    return render(request, 'main/market.html', context=data)


def cart(request):
    return render(request, 'main/cart.html')


def mine(request):
    return render(request, 'main/mine.html')


def learn(request):
    return redirect(reverse('axf:home'))
