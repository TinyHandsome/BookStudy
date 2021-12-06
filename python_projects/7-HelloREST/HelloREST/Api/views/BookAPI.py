from django.http import JsonResponse
from django.http.request import QueryDict

from django.views.decorators.csrf import csrf_exempt

from Api.models import Book


@csrf_exempt
def books(request):
    if request.method == 'GET':
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
    elif request.method == 'POST':

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


@csrf_exempt
def book(request, bookid):
    if request.method == 'GET':
        print(bookid)
        book_obj = Book.objects.get(pk=bookid)
        data = {
            'msg': 'ok',
            'status': 200,
            'data': book_obj.to_dict()
        }
        return JsonResponse(data=data)

    elif request.method == 'DELETE':
        book_obj = Book.objects.get(pk=bookid)
        book_obj.delete()
        data = {
            'msg': 'delete success',
            'status': 204,
            # 'data': {}
        }
        return JsonResponse(data=data, status=204)
