#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: task_schedule_info.py
@time: 2020/11/11 9:41
@desc: 获取最新环境taskschedule的信息
        1. 查询结果，返回dataframe
        2. 修改sql，成功则返回True，失败则返回False和错误信息并回滚
"""

import pymysql
import pandas as pd
from password import ts_mysql_info


class MysqlInfo:

    def __init__(self):
        ts_mysql_info = ts_mysql_info
        self.db = pymysql.connect(ts_mysql_info.get('host'), ts_mysql_info.get('user'), ts_mysql_info.get('password'),
                                  ts_mysql_info.get('database'))
        # 检查连接是否断开，如果断开就进行重连
        self.db.ping(reconnect=True)
        self.tcursor = self.db.cursor()

    def select_sql(self, sql):
        """查询语句，返回dataframe"""
        self.tcursor.execute(sql)
        data = self.tcursor.fetchall()
        columns_temp = self.tcursor.description
        columns = [i[0] for i in columns_temp]
        return pd.DataFrame(data, columns=columns)

    def update_sql(self, sql):
        """修改语句，update"""
        try:
            self.tcursor.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print('出错啦！报错内容：', e)
            return False

    def close_all(self):
        self.tcursor.close()
        self.db.close()


if __name__ == '__main__':
    pass
