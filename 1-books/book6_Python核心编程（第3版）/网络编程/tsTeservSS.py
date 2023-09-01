#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: tsTeservSS.py
@time: 2020/12/26 16:13
@desc: 创建SocketServer TCP服务器
"""

from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):
    def handle(self):
        print('...连自：', self.client_address)
        self.wfile.write(bytes('[%s] %s' % (ctime(), str(self.rfile.readline(), encoding='utf-8')), encoding='utf-8'))


tcpServ = TCP(ADDR, MyRequestHandler)
print('等待连接...')
tcpServ.serve_forever()
