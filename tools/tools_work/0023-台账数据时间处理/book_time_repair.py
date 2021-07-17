#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: book_time_repair.py
@time: 2021/7/16 16:06
@desc: 台账中跟时间相关的数据全部修复
        【20210717】初始化版本 v0.1
            1. pyinstaller -D -n 台账日期处理工具[v0.1] -i rili.ico book_time_repair.py
"""

import pandas as pd
import re
import os
import datetime
import time
from dataclasses import dataclass
from collections import defaultdict
from tkinter import Tk
from tkinter.filedialog import askopenfilename


@dataclass
class BookTimeRepair:
    excel_path: str

    def __post_init__(self):

        # 更新日志和写在前面
        self.info_before = '【注意】\n' \
                           '    1. 使用时，需要保证excel中的日期格式为【常规】或【文本】，而不是【日期】或其他格式\n' \
                           '       否则将会导致处理后的日期输出为 形如 [2022-06-18 00:00:00] 的格式\n' \
                           '    2. 程序运行完毕后会自动打开 【日志文件】，关闭后，会自动打开处理后的【处理后的excel】\n' \
                           '    3. 如果需要不自动打开，或需要其他功能和优化功能也请联系开发人员【litian@whchem.com】\n' \
                           '    4. 日志文件和处理后的excel保存路径与 输入excel 的路径相同' \
                           + '\n'
        print(self.info_before)

        # 获取excel的根目录
        self.root_path, self.file_name = os.path.split(self.excel_path)
        # 生成一个日志文件
        self.current_time_str = datetime.datetime.strftime(datetime.datetime.now(), '[%Y-%m-%d-%H-%M-%S]')
        # 生成输出文件名
        self.output_path = os.path.join(self.root_path, self.current_time_str + self.file_name)
        self.log_file_name = os.path.join(self.root_path, 'log-' + self.current_time_str + '.txt')
        self.log = open(self.log_file_name, 'w', encoding='utf-8')

        # 定义特殊问题的字典
        self.problem_dict = defaultdict(int)
        self.problem_dict_keys = {
            1: '空和空值',
            2: '/',
            3: '..',
            4: 'nan',
            9: '其他不识别的日期数据'
        }
        self.problemlist_9 = []

    def close(self):
        """退出函数"""
        self.log.close()
        print(self.current_time_str + ' 程序运行完毕，将自动打开日志文件和输出文件，请稍等...')
        os.system(r'notepad ' + self.log_file_name)
        os.system(self.output_path)

    def deal_date(self, date):
        """处理时间字段"""
        date = str(date).strip()
        # 统计空和空值
        if pd.isna(date) or date == '':
            self.problem_dict[1] += 1
            return date
        # 统计/
        if date == '/':
            self.problem_dict[2] += 1
            return date
        # nan
        if date == 'nan':
            self.problem_dict[4] += 1
            return date
        # 统计..的情况
        while '..' in date:
            self.problem_dict[3] += 1
            date = date.replace('..', '.')

        try:
            pattern = re.compile(r'\d{4}(?P<connect>[、./-])\d{1,2}(?:[、./-](?P<day>\d{1,2}))?')
            connect, day = pattern.match(date).groups()
            if day is None:
                return date + connect + '01'
            else:
                return date
        except:
            # 统计无法识别的日期
            self.problem_dict[9] += 1
            self.problemlist_9.append(date)
            return date

    def deal_table(self):
        """处理数据"""
        # 读取，空值不做处理直接为''而不是nan，以str的格式读取
        tables = pd.read_excel(self.excel_path, sheet_name=None, keep_default_na=False, dtype=str)
        # 保存
        writer = pd.ExcelWriter(self.output_path)
        for sheet_name, sheet in tables.items():
            # 时间相关的列名
            aim_column_names = [x for x in sheet.columns if '有效日期' in x]
            for aim_column_name in aim_column_names:
                sheet[aim_column_name] = sheet[aim_column_name].apply(self.deal_date)

            sheet.to_excel(writer, sheet_name=sheet_name, index=False)
        writer.save()
        self.write_log()

    def write_log(self):
        """写入log文件中"""
        # 先检查是否没有异常数据
        if sum(self.problem_dict.values()) == 0:
            self.log.write('恭喜你，没有异常日期数据，所有日期已完成年月到年月日的转换！')
        else:
            self.log.write('处理时发现的异常日期数据\n' + self.current_time_str + '\n\n')
            for key, value in sorted(self.problem_dict.items()):
                self.log.write(str(key) + '. 日期为【' + self.problem_dict_keys.get(key) + '】的数量：' + str(value) + '\n')

            self.log.write('9中没有识别的日期有（去重后）：' + ', '.join(list(set(self.problemlist_9))))

        self.close()


def get_path(formats: list = None):
    """获取文件路径"""
    root = Tk()
    root.withdraw()
    if formats is None:
        return askopenfilename()
    else:
        path = askopenfilename()
        for f in formats:
            if path.endswith(f):
                return path, 1
        return path, -1


if __name__ == '__main__':
    excel_path, status_code = get_path(formats=['xls', 'xlsx'])

    # excel文件检测
    if status_code == -1:
        print('【警告】输入的文件不是excel文件！程序即将退出...')
        limit_time = 3
        for i in range(limit_time):
            print('倒计时：', limit_time - i)
            time.sleep(1)
    else:
        test = BookTimeRepair(excel_path)
        test.deal_table()
