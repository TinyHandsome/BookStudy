#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: word_check.py
@time: 2020/11/12 13:59
@desc: 读取详设word文件，检查部分内容
        [Python3.7 dataclass使用指南](https://www.cnblogs.com/apocelipes/p/10284346.html#using-define)
        1. 标题名是不是与createtable中的表名一致
        2. 抽取策略为增量的，是否有partitioned by，否则应该没有partioned by
"""

from docx import Document
import pandas as pd
from typing import List
from dataclasses import dataclass, field
import re
import win32com.client as wc
import os


@dataclass
class Doc2Docx:
    """将doc转换为docx"""
    word = wc.Dispatch("Word.Application")

    def transfer(self, fpath: str) -> str:
        """转换"""
        doc = self.word.Documents.Open(fpath)

        # 路径处理
        root_path, file_name = os.path.split(fpath)
        new_file_name = "{}x".format(file_name)
        new_path = os.path.join(root_path, new_file_name)

        doc.SaveAs(new_path, 12)
        doc.Close()

        return new_path

    def close(self):
        self.word.Quit()


@dataclass
class Procedure:
    """word中的每一个任务"""
    # 任务名
    raw_head: str = ''
    head: str = ''

    # 是否有分区
    raw_is_partioned: bool = None
    is_partioned: bool = None

    # 目标sql
    sql: str = ''

    def set_head(self):
        """设置任务标题字段"""
        self.head = re.findall(r'抽取(.*)', self.raw_head)[0].strip()

    def set_is_partioned(self):
        """设置分区字段"""
        if '否' in self.raw_is_partioned:
            self.is_partioned = False
        else:
            self.is_partioned = True

    def check_table_name(self):
        """检查表名是否与sql中的表名一致"""
        try:
            sql_table_name = re.findall(r'create\s*table\s*if\s*not\s*exists\s*.*\.`(.*)`', self.sql)[0].strip()
            return sql_table_name.lower() == self.head.lower()
        except:
            return -10

    def check_partioned(self):
        """检查是否有分区字段"""
        flag_sql = 'partitioned by' in self.sql
        return flag_sql == self.is_partioned

    def check_all_func(self):
        """检查分区和表名两种情况，如果出现其中一种则输出报错"""
        result = ''
        flag1 = self.check_table_name()
        if not flag1:
            result += '表名与任务中涉及的表不一致！'
        else:
            if flag1 == -10:
                result += '目标表没有`字符！'

        if not self.check_partioned():
            result += '分区情况（partitioned by）有问题！'

        if result == '':
            return False
        else:
            return self.head + ': ' + result

    def check_all(self):
        """try check_all_func"""
        try:
            return self.check_all_func()
        except Exception as e:
            return self.head + ': ' + '缺少对应的字段，需要补全！（该任务详设与标准详设格式不一致！）'


@dataclass
class WordDeal:
    """处理word文件"""
    fpath: str
    dc = None
    type_4th = '中通文档标题4'

    flag = False
    hang = -999
    temp_procedule = None

    pros: List[Procedure] = field(default_factory=list)

    def __post_init__(self):
        self.dc = Document(self.fpath)

    def deal_word(self):
        for paragraph in self.dc.paragraphs:
            if paragraph.style.name == self.type_4th:
                # 忽略第一次的空值
                if self.temp_procedule is not None:
                    self.pros.append(self.temp_procedule)

                self.temp_procedule = Procedure(raw_head=paragraph.text)
                self.temp_procedule.set_head()

                self.hang = -9999

            if '是否有分区' in paragraph.text:
                self.temp_procedule.raw_is_partioned = re.findall(r'是否有分区[：:][\s]*(.*)', paragraph.text)[0]
                self.temp_procedule.set_is_partioned()

            if '建表语句' in paragraph.text:
                # 0是因为要跳过这一句
                self.hang = 0

            if self.hang > 0:
                self.temp_procedule.sql += paragraph.text + '\n'

            self.hang += 1

        # 最后一个流程
        self.pros.append(self.temp_procedule)


@dataclass
class WordsDeal:
    file_path: str
    path_files: List[str] = None
    final_result: List = field(default_factory=list)
    generate_files: List = field(default_factory=list)

    def __post_init__(self):
        self.get_files()

    def get_files(self):
        """获取路径下的每个文件的绝对路径"""
        files = os.listdir(self.file_path)
        self.path_files = [os.path.join(self.file_path, f) for f in files if
                           (f.endswith('doc') or f.endswith('docx')) and not f.startswith('~$')]

    def delete_generate_files(self):
        """删掉生成的docx"""
        for ff in self.generate_files:
            os.remove(ff)

    def deal_all_files(self):
        """处理所有的文件"""
        d2d = Doc2Docx()

        for f_path in self.path_files:
            print('正在处理', os.path.split(f_path)[-1], '...')
            if f_path.endswith('.doc'):
                # 先看文件是否是doc，是的话生成docx
                path = d2d.transfer(f_path)
                self.generate_files.append(path)
            else:
                path = f_path

            wd = WordDeal(path)
            wd.deal_word()
            count = 1
            for pro in wd.pros:
                result = pro.check_all()
                if result:
                    self.final_result.append([os.path.split(f_path)[-1], count] + result.split(': '))
                    count += 1

        print('正在生成结果，并删除生成的中间doc...')
        df = pd.DataFrame(self.final_result, columns=['文件名', '编号', '表名', '问题'])
        df.to_excel(os.path.join(self.file_path, '检查结果.xlsx'), index=False)

        # 关闭d2d
        d2d.close()
        # 删除所有新生成的文件
        self.delete_generate_files()
        print('运行完毕...')


if __name__ == '__main__':
    root_path = 'E:\\【冲鸭】\\【工作】1. 工作安排、文件存储\\20201120-合同报表施工类详设\\ODS\\'

    WordsDeal(root_path).deal_all_files()
