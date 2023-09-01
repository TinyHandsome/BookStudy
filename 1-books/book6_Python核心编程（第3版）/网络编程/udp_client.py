#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: udp_client.py
@time: 2020/12/26 15:28
@desc: udp客户端
"""

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(bytes(data, encoding="utf-8"), ADDR)
    data, _ = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(str(data, encoding="utf-8"))

udpCliSock.close()