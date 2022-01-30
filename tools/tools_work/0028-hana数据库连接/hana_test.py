#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: hana_test.py
@time: 2022/1/24 13:30
@desc: hana数据库链接测试
"""

import pyhdb


def get_connection():
    connection = pyhdb.connect(
        host='10.4.16.13',
        port=31015,
        user='leaphd',
        password='Yantai002',
    )
    return connection


class MyHana:

    def __init__(self):
        self.connection = get_connection()

    def cursor_execute(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result


if __name__ == '__main__':
    mh = MyHana()
    print(mh.cursor_execute("SELECT TABLE_NAME FROM USER_TABLES ORDER BY TABLE_NAME;"))
