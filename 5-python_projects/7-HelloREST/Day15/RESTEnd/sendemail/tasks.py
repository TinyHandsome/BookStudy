from time import sleep

from celery import shared_task
from django.core.mail import send_mail
from password import from_email


@shared_task
def add(a, b):
    print('睡着了')
    sleep(5)
    return a + b


@shared_task
def send_email(receive):
    subject = "你真是一个小天才"
    message = "真的"
    recipient_list = (receive,)
    send_mail(subject, message, from_email, recipient_list)
