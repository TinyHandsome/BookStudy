from django.http import JsonResponse
from .BookAPI import book, books


def index(request):
    data = {
        'status': 200,
        'msg': 'ok'
    }
    return JsonResponse(data=data)
