#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: schedule_time_check.py
@time: 2020/11/13 9:28
@desc: 检查各种调度时间，并实现任务调度时间的校验
"""

from task_schedule_info import MysqlInfo
from dataclasses import dataclass
import re


@dataclass
class GetTask:
    db = MysqlInfo()
    sql: str

    def __post_init__(self):

        self.data = self.db.select_sql(self.sql)

        # 【双表增量全量表调度时间】获取双表增量中全量表的运行时间，并用正则表达式提取出来
        self.date = self.data.loc[:, ['process_name', 'process_variables']]
        self.date['date'] = self.date['process_variables'].apply(lambda x: GetTask.get_initDay(x))
        # 【任务调度时间】
        self.schdule_date = self.data.loc[:, ['process_name', 'schedule_time']]
        # 原来的输出是[(1,2,3), (4,5,6)]，zip(*)之后为：[(1,4), (2,5), (3,6)]
        self.schdule_date['h'], self.schdule_date['m'], self.schdule_date['s'] = zip(*self.schdule_date['schedule_time'].apply(lambda x: GetTask.getTimedelta(x)))

    @staticmethod
    def get_initDay(pv):
        result = re.findall(r'\$\{initDay\}=(.*)', pv)
        if result:
            return result[0]
        else:
            return ''

    @staticmethod
    def getTimedelta(time):
        """处理 Timedelta 格式的数据，返回时,分"""
        minutes = time.total_seconds() / 60
        h = int(minutes / 60)
        m = int(minutes % 60)
        s = int(time.total_seconds() - h * 3600 - m * 60)
        return h, m, s

    def get_task_date(self, task_name, type_func):
        """获取任务的变量值"""

        if type_func == 1:
            # 获取双表增量的变量信息
            aim_df = self.date.values
        elif type_func == 2:
            aim_df = self.schdule_date.values

        # 保存任务名和对应的日期
        name_length = 999
        aim_day = None

        for row in aim_df:

            # 遍历数据库中任务名字
            name = row[0]
            day = row[2:]

            if name.lower().endswith(task_name.lower()):
                if name_length > len(task_name) and day != '':
                    # 这里要找到最短的对应的任务，同时不能是删掉任务（删掉的任务day为''）
                    name_length = len(task_name)
                    aim_day = day

        return aim_day

    def get_schedule_date(self, task_pro):
        """这里是遍历所有项目，然后检查每个项目的时间是否满足要求"""
        pass
