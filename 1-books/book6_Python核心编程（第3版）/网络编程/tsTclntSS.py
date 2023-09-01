#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: tsTclntSS.py
@time: 2020/12/26 16:37
@desc: 创建客户端
"""

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(bytes('%s\r\n' % data, encoding='utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(str(data, encoding='utf-8').strip())
    tcpCliSock.close()