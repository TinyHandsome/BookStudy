from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from App.models import Blog


def index(request):
    return HttpResponse("Index")


def edit_blog(request):
    if request.method == 'GET':
        return render(request, 'edit_blog.html')
    elif request.method == 'POST':
        content = request.POST.get("content")
        print(content)
        blog = Blog()
        blog.b_content = content
        blog.save()
        return HttpResponse("哈哈")