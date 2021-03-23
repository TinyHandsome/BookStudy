from django.urls import path

from App import views

app_name = '[App]'
urlpatterns = [
    path('hello/', views.hello, name='hello'),
]