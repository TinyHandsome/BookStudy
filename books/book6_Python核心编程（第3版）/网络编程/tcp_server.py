#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: tcp_server.py
@time: 2020/12/26 10:32
@desc: 创建TCP服务器
"""

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('等待连接...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...连接自：', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send(bytes('[%s] %s' % (ctime(), str(data, encoding='utf-8')), encoding='utf-8'))

    tcpCliSock.close()
tcpSerSock.close()
