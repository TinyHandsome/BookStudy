from django.http import HttpResponse

from sendemail.tasks import add, send_email


def index(request):
    result = add(5, 6)
    return HttpResponse(result)


def my_async(request):
    result_id = add.delay(5, 8)
    return HttpResponse(result_id)


def email(request):

    mail_address = request.GET.get('address')
    send_result = send_email.delay(mail_address)

    return HttpResponse(send_result)


def home(request):
    return HttpResponse('我不困！')