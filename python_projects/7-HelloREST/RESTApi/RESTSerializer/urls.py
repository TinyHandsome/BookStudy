from django.conf.urls import url

from RESTSerializer import views

urlpatterns = [
    url(r'^persons/', views.PersonView.as_view()),
]