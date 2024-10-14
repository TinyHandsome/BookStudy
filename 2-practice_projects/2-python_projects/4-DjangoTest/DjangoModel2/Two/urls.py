from django.urls import path, re_path

from Two import views

app_name = '[Two]'

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('addperson/', views.add_person, name='add_person'),
    path('addidcard/', views.add_id_card, name='add_id_card'),
    path('bindcard/', views.bind_card, name="bind_card"),
    path('removeperson/', views.remove_person, name='remove_person'),
    path('removeidcard/', views.remove_id_card, name='remove_id_card'),
    path('getperson/', views.get_person, name='get_person'),
    path('getidcard/', views.get_id_card, name='get_id_card'),

    path('addcustomer/', views.add_customer, name='add_customer'),
    path('addgoods/', views.add_goods, name='add_goods'),
    path('addtocart/', views.add_to_cart, name='add_to_cart'),
    re_path(r'getgoodslist/(?P<customerid>\d+)/', views.get_goods_list, name='get_goods_list'),

    path('addcat/', views.add_cat, name='add_cat'),
    path('adddog/', views.add_dog, name='add_dog'),
]
