from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets


# Create your views here.
from REST.models import Book
from REST.serializers import UserSerializer, GroupSerializer, BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

