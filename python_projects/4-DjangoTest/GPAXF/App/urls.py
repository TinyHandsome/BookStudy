from django.urls import path

from App import views

app_name = '[main]'

urlpatterns = [
    path('index/', views.index, name='index'),
]