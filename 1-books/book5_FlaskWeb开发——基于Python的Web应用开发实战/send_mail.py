#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: send_mail.py
@time: 2020/10/22 18:33
@desc: 
"""

from flask_mail import Message
from hello import mail, app

msg = Message('test email', sender='694317828@qq.com', recipients=['litian_cup@163.com'])
msg.body = '这是text body.'
# msg.html = '这是<b>HTML</b> body.'
with app.app_context():
    mail.send(msg)
