from django.urls import path

from App import views

urlpatterns = [
    path('hello/', views.hello),
    path('index/', views.index),
    path('getstudents', views.get_students),
    path('temp/', views.template),
    path('home/', views.home),
    path('hehe', views.hehe),
    path('hehehe', views.hehehe),

]