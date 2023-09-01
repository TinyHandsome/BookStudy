#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: email_examples.py
@time: 2021/1/8 13:22
@desc: 创建并发送了两种不同类型的电子邮件消息。
"""

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP


def make_mpa_msg():
    email = MIMEMultipart('alternative')
    text = MIMEText('Hello World!\r\n', 'plain')
    email.attach(text)
    html = MIMEText('<html><body><h4>Hello World!</h4></body></html>', 'html')
    email.attach(html)
    return email


def make_img_msg(fn):
    f = open(fn, 'r')
    data = f.read()
    f.close()
    email = MIMEImage(data, name=fn)
    email.add_header('Content-Dispostion', 'attachment; filename="%s"' % fn)
    return email


def sendMsg(fr, to, msg):
    s = SMTP('localhost')
    errs = s.sendmail(fr, to, msg)
    s.quit()


if __name__ == '__main__':
    print('Sending multipart alternative msg...')
    msg = make_mpa_msg()

    SENDER = ''
    RECIPS = ''
    SOME_IMG_FILE = r''

    msg['From'] = SENDER
    msg['To'] = ', '.join(RECIPS)
    msg['Subject'] = 'multipart alternative test'
    sendMsg(SENDER, RECIPS, msg.as_string())

    print(('Sending image msg...'))
    msg = make_img_msg(SOME_IMG_FILE)
    msg['From'] = SENDER
    msg['To'] = ', '.join(RECIPS)
    msg['Subject'] = 'Image file test'
    sendMsg(SENDER, RECIPS, msg.as_string())
