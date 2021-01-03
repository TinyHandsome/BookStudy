#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: tsTservTW.py
@time: 2020/12/29 16:57
@desc: 时间戳TCP服务器
"""

from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567


class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...连接自：', clnt)

    def dataReceived(self, data):
        self.transport.write(bytes('[%s] %s' % (ctime(), str(data, encoding='utf-8')), encoding='utf-8'))


factory = protocol.Factory()
factory.protocol = TSServProtocol
print('等待连接...')
reactor.listenTCP(PORT, factory)
reactor.run()
