from django.http import HttpResponse, JsonResponse, QueryDict
from django.shortcuts import render
from django.views import View

from CBV.models import Book


class HelloCBV(View):
    def get(self, request):
        return HttpResponse('hahaha')

    def post(self, request):
        return HttpResponse('POST 666')

    def put(self, request):
        return HttpResponse('PUT 666')


class BooksCBV(View):
    def get(self, request):
        book_list = Book.objects.all()
        book_list_json = []
        for book in book_list:
            book_list_json.append(book.to_dict())

        data = {
            'status': 200,
            'msg': 'ok',
            'data': book_list_json
        }
        return JsonResponse(data=data)

    def post(self, request):
        # 两种获取信息的方式
        post = request.POST
        if len(post) == 0:
            post = QueryDict(request.get_full_path().split('?')[1])

        b_name = post.get('b_name')
        b_price = post.get('b_price')

        book = Book()
        book.b_name = b_name
        book.b_price = b_price
        book.save()

        data = {
            'status': 201,
            'msg': 'add success',
            'data': book.to_dict()
        }

        return JsonResponse(data=data, status=201)
