from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
]