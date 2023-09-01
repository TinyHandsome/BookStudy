#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: udp_server.py
@time: 2020/12/26 15:08
@desc: UDP服务器
"""

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('等待消息。。。')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto(bytes('[%s] %s' % (ctime(), str(data, encoding='utf-8')), encoding='utf-8'), addr)
    print('...接收自并返回给：', addr)

udpSerSock.close()

