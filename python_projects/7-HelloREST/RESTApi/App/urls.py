from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^hello/', views.HelloView.as_view(), name='hello'),
    url(r'^template/', views.HelloTemplateView.as_view(), name='template'),
    url(r'^listview/', views.HelloListView.as_view(), name='listview'),
    url(r'^single/(?P<pk>\d+)', views.HeDetailView.as_view(), name='single'),
]