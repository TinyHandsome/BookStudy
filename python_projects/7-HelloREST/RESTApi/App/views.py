from django.shortcuts import render

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from App.models import Book


class HelloView(View):
    def get(self, request):
        return render(request, 'hello.html')


class HelloTemplateView(TemplateView):
    template_name = 'hello.html'


class HelloListView(ListView):
    template_name = 'BookList.html'
    model = Book


class HeDetailView(DetailView):
    template_name = 'Book.html'
    model = Book

