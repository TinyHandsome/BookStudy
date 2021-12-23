from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^games/$', views.GamesView.as_view()),
    url(r'^games/(?P<pk>\d+)', views.GameView.as_view(), name='game-detail'),
]