from django.urls import path
from blog import views

urlpatterns = [
    path('', views.archive),
    path('create/', views.create_blogpost),
]
