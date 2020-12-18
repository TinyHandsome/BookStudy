#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: get_month_schedule.py
@time: 2020/11/13 17:21
@desc: 检查双表增量的全量调度时间是否一致
"""
from dataclasses import dataclass
import pandas as pd
import re
from schedule_time_check import GetTask


@dataclass
class GetMonthSchedule:
    file_path: str

    def __post_init__(self):
        df = pd.read_excel(file_path)
        df.dropna(inplace=True)
        self.aim_df = df.iloc[:, [2, 5]]
        self.aim_df['day'] = self.aim_df['全量更新时间'].apply(lambda x: GetMonthSchedule.get_updateDay(x))

    @staticmethod
    def get_updateDay(pv):
        result = re.findall(r'每月(.*)号', pv)
        if result:
            return result[0]
        else:
            return ''

    def check_date(self):
        """检查全量更新时间是否与设置一致"""
        gt = GetTask("select * from P_PROCESS_DEF where process_name like 'ODS_%' ")
        count = 0
        missed_name_count = 0
        error_count = 0

        for line in self.aim_df.values:
            count += 1
            task_name = line[0]
            task_name = task_name.replace('_incr', '') if '_incr' in task_name else task_name
            day = line[2]

            aim_day = gt.get_task_date(task_name, type_func=1)
            if aim_day:
                if int(day) == int(aim_day):
                    # print(count, ': ', task_name, '-> [√] 全量更新时间一致')
                    pass
                else:
                    print(count, ': ', task_name, '-> [×] 全量更新时间不一致', end='')
                    print(' ->', 'excel中的时间：', day, '任务中的时间：', aim_day)
                    error_count += 1
            else:
                print(count, ': ', task_name, '没找到任务！！！！！！！！！！')
                missed_name_count += 1

        if missed_name_count > 0:
            print('！！！【注意】有', missed_name_count, '个任务名没找到！！！')
        else:
            print('运行完毕...')

        print('报错的任务有：', error_count, '个！')


if __name__ == '__main__':
    # 检查双表增量中全量的调度时间
    file_path = 'E:/【冲鸭】/【工作】1. 工作安排、文件存储/20201113-ODS双表时间修改验证/aim_table.xlsx'
    gs = GetMonthSchedule(file_path)
    gs.check_date()
