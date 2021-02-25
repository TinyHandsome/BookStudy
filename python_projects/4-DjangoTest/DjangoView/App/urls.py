from django.urls import path

from App import views

app_name = '[App]'

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('getticket/', views.get_ticket, name='get_ticket'),
    path('getinfo/', views.get_info, name='get_info')
]