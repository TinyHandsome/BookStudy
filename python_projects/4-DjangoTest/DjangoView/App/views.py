from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    response = HttpResponse()
    # response.content = '德玛西亚'
    # response.status_code = 404
    response.write('听说马桶堵了')
    response.flush()
    return response
