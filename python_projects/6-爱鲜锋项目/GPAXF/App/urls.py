from django.conf.urls import url

from App import views

app_name = 'App'
urlpatterns = [
    url(r'index/', views.index)
]