


from django.shortcuts import render


def index(request):
    """mark view"""
    data = {}

    return render(request, 'index_mark.html', context=data)