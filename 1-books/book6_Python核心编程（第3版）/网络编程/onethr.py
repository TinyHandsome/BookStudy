#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: onethr.py
@time: 2021/1/8 17:19
@desc: 使用单线程执行循环
"""

from time import sleep, ctime


def loop0():
    print('start loop 0 at: ', ctime())
    sleep(4)
    print('loop 0 done at: ', ctime())


def loop1():
    print('start loop 1 at: ', ctime())
    sleep(2)
    print('loop 1 done at:', ctime())


def main():
    print('starting at: ', ctime())
    loop0()
    loop1()
    print('all Done at: ', ctime())


if __name__ == '__main__':
    main()
