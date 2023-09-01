#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: my_mail.py
@time: 2022/3/9 13:48
@desc: 发邮件功能
        参考链接：https://www.cnblogs.com/yufeihlf/p/5726619.html
"""
import os
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from dataclasses import dataclass
from email.mime.text import MIMEText


@dataclass
class MyEmail:
    def __post_init__(self):
        self.smtp = smtplib.SMTP()
        self.smtp.connect('smtp.163.com', 25)
        # self.smtp = smtplib.SMTP_SSL('smtp.163.com')
        self.msg = MIMEMultipart('mixed')

    def login(self, username, password):
        self.smtp.login(username, password)

    def send_email(self, sender, receiver):
        """发送邮件"""
        self.smtp.sendmail(sender, receiver, self.msg.as_string())

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.smtp.quit()

    def set_subject(self, s):
        """设置标题"""
        self.msg['Subject'] = s

    def set_from(self, s):
        """设置发件人"""
        self.msg['From'] = s

    def set_to(self, l):
        """设置收件人"""
        self.msg['To'] = ';'.join(l)

    def attach_text_plain(self, text):
        """构建文字内容"""
        text_plain = MIMEText(text, 'plain', 'utf-8')
        self.msg.attach(text_plain)

    def attach_image(self, path):
        """构建图片内容"""
        img_name = os.path.split(path)[-1]
        sendimagefile = open(path, 'rb').read()
        image = MIMEImage(sendimagefile)
        image.add_header('Content-ID', '<image1>')
        image["Content-Disposition"] = 'attachment; filename="' + img_name + '"'
        self.msg.attach(image)

    def attach_html(self, html):
        """构建html"""
        text_html = MIMEText(html, 'html', 'utf-8')
        text_html["Content-Disposition"] = 'attachment; filename="texthtml.html"'
        self.msg.attach(text_html)

    def attach_file(self, path):
        """构建附件"""
        file_name = os.path.split(path)[-1]
        sendfile = open(path, 'rb').read()
        text_att = MIMEText(sendfile, 'base64', 'utf-8')
        text_att["Content-Type"] = 'application/octet-stream'

        text_att.add_header('Content-Disposition', 'attachment', filename=file_name)
        self.msg.attach(text_att)
