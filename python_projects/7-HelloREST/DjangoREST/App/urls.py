from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from App import views
from App.views import GameModelViewSet

urlpatterns = [
    url(r'^games/$', views.GamesView.as_view()),
    url(r'^games/(?P<pk>\d+)/$', views.GameView.as_view(), name='game-detail'),
]

router = DefaultRouter()
router.register(r'games', GameModelViewSet)