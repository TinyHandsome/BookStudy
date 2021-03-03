from django.urls import path

from Two import views

app_name = '[Two]'

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('login/', views.login, name='login'),
    path('mine/', views.mine, name='mine'),
]