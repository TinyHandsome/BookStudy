import logging

from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello_transaction(request):
    try:
        # 原子性 一致性 隔离性 持久性
        with transaction.atomic():
            ...

    except Exception as e:
        transaction.rollback()
    else:
        transaction.commit()

    return HttpResponse('Hello')


def welcome_transaction(request):
    save_point = transaction.savepoint()
    try:
        ...
    except Exception as e:
        transaction.savepoint_rollback(save_point)
    else:
        transaction.savepoint_commit(save_point)

    return HttpResponse('Welcome')


def hello_sql(request):
    # defer  不要哪些字段
    # only  要哪些字段
    result = User.objects.raw('select  * from user')
    return HttpResponse("sql")


def hello_log(request):
    logger = logging.getLogger('django')
    logger.error("哈哈 error了")
    return HttpResponse('hello log')