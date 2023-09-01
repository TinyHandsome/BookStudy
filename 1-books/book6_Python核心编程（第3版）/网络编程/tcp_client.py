#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: tcp_client.py
@time: 2020/12/26 10:32
@desc: 创建TCP用户端
"""

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(bytes(data, encoding="utf-8"))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(str(data, encoding="utf-8"))

tcpCliSock.close()
