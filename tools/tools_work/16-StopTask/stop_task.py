#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: stop_task.py
@time: 2020/12/29 14:24
@desc: 禁用目标任务
        process_state（流程状态）: N正常, D禁止'
"""

from dataclasses import dataclass
from task_schedule_info import MysqlInfo
import pandas as pd
from collections import OrderedDict


@dataclass
class StopTask:
    db = MysqlInfo()

    def __post_init__(self):
        # 记录修改之前的状态
        self.dict_data = OrderedDict()
        # 记录失败的数量
        self.count = 0

    def get_aim_task(self, task_name, col_name):
        sql = "select * from P_PROCESS_DEF where process_name = '" + task_name + "';"
        data = self.db.select_sql(sql)
        return data[col_name].values[0]

    def update_aim_task(self, task_name, aim_column, aim_value):
        """设置目标表的目标列的值为目标数值"""
        sql = "update P_PROCESS_DEF set " + aim_column + "='" + aim_value + "' where process_name = '" + task_name + "';"
        flag = self.db.update_sql(sql)
        if flag:
            print('修改成功...')
        else:
            self.count += 1
            print('修改失败...')


def read_excel():
    st = StopTask()
    path = r'E:\1-工作\1-工作\20201229-上线预演\禁用任务列表.xlsx'
    df = pd.read_excel(path)
    tasks = df.iloc[:, 1].values.tolist()
    for task in tasks:
        st.dict_data[task] = st.get_aim_task(task, 'process_state')
        print(task, "：", end='')
        st.update_aim_task(task, 'process_state', 'D')
    print('*'*100)
    print('失败的数量为：', st.count, '\n')
    print('修改前的结果：\n', st.dict_data)
    st.db.close_all()


if __name__ == '__main__':
    read_excel()
    # StopTask().update_aim_task('ODS_MM_RKPF', 'process_state', 'D')
