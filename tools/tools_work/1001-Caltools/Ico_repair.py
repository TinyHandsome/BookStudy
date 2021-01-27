#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: Ico_repair.py
@time: 2020/1/17 15:16
@desc: 在导出exe文件的时候，图标会报错，这里进行修改
       参考链接：https://blog.csdn.net/weixin_30907523/article/details/98814707
"""
import base64
from icon import Icon


def ico_generate():
    with open("icon.py", "a") as f:
        f.write('class Icon(object):\n')
        f.write('\tdef __init__(self):\n')
        f.write("\t\tself.img='")
    with open("53.ico", "rb") as i:
        b64str = base64.b64encode(i.read())
        with open("icon.py", "ab+") as f:
            f.write(b64str)
    with open("icon.py", "a") as f:
        f.write("'")


def ico_repair(root):
    with open('tmp.ico', 'wb') as tmp:
        tmp.write(base64.b64decode(Icon().img))
        root.iconbitmap('tmp.ico')
        return 'tmp.ico'


if __name__ == '__main__':
    ico_generate()
