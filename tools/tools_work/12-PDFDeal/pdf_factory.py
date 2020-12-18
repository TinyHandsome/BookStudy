#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: pdf_factory.py
@time: 2020/12/1 10:59
@desc: 测试
"""

from pdf_deal import PDFTool
import re
import os
import pandas as pd
from dataclasses import dataclass
from properties import properties


@dataclass
class PDFFactory:

    def __post_init__(self):
        pass

    def walk_files(self, root_path, pattern):

        result = []
        for home, _, files in os.walk(root_path):
            for file_name in files:
                # 过滤pdf的文件
                if file_name.lower().endswith('.pdf', ):
                    aim_path = os.path.join(home, file_name)

                    try:
                        info = self.get_info(aim_path, pattern)
                        error_info = 0
                    except:
                        print(aim_path)
                        info = '！！！报错，请检查关键字！！！'
                        error_info = 1

                    result.append([file_name, aim_path, info, error_info])

        df = pd.DataFrame(result, columns=['文件名', '文件路径', '目标信息', '报错信息'])
        df.index.name = '编号'
        df.to_excel(os.path.join(root_path, 'result.xlsx'))

    def get_info(self, file_path, pattern):
        pdf_tool = PDFTool()
        answer = pdf_tool.parse_dpfplumber(file_path)

        result = re.search(pattern, answer, re.DOTALL)
        return result.group(2)


def get_root_path_and_pattern():
    root_path = properties.get('root_path')
    filter_starts = properties.get('filter_start')
    filter_ends = properties.get('filter_end')

    start = '(' + '|'.join(filter_starts) + ')'
    end = '(' + '|'.join(filter_ends) + ')'
    pattern = start + '(.*)' + end

    return root_path, pattern


if __name__ == '__main__':
    root_path, pattern = get_root_path_and_pattern()
    PDFFactory().walk_files(root_path, pattern)
