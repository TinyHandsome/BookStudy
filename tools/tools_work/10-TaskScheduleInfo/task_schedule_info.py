#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: task_schedule_info.py
@time: 2020/11/11 9:41
@desc: 获取taskschedule的信息
"""

import pymysql
import pandas as pd


class MysqlInfo:

    def __init__(self):
        ts_mysql_info = {
            'host': '10.4.16.31',
            'user': 'root',
            'password': 'bigdata',
            'database': 'priest_db'
        }

        self.db = pymysql.connect(ts_mysql_info.get('host'), ts_mysql_info.get('user'), ts_mysql_info.get('password'),
                                  ts_mysql_info.get('database'))
        self.tcursor = self.db.cursor()

    def select_sql(self, sql):
        self.tcursor.execute(sql)
        data = self.tcursor.fetchall()
        columns_temp = self.tcursor.description
        columns = [i[0] for i in columns_temp]
        self.close_all()
        return pd.DataFrame(data, columns=columns)

    def close_all(self):
        self.tcursor.close()
        self.db.close()


if __name__ == '__main__':
    pass