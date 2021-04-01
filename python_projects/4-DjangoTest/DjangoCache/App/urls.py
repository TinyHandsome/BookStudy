from django.urls import path

from App import views

app_name = '[App]'

urlpatterns = [
    path('index/', views.index, name='index'),
]
