from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from App.models import Game
from App.serializers import GameSerializers


class GamesView(ListCreateAPIView):
    serializer_class = GameSerializers
    queryset = Game.objects.all()


class GameView(RetrieveUpdateDestroyAPIView):
    serializer_class = GameSerializers
    queryset = Game.objects.all()


class GameModelViewSet(ModelViewSet):
    serializer_class = GameSerializers
    queryset = Game.objects.all()
