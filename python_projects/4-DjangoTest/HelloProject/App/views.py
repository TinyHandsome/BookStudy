from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Index")


def edit_blog(request):
    return render(request, 'edit_blog.html')