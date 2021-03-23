from django.urls import path

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
]
