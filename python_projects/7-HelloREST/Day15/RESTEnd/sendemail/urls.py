from django.conf.urls import url

from sendemail import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^async/', views.my_async),
    url(r'^email/', views.email),
    url(r'^home/', views.home),
]