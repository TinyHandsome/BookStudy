#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: content_factory.py
@time: 2021/1/19 19:39
@desc:
        1. 表 -> 系统：根据表名检查是否有三级目录，是否有中文名
"""

from dataclasses import dataclass

from selenium_cookie import UrlAnalyze
from table_factory import TableFactory
from content import *
import json
import pandas as pd
import os


@dataclass
class ContentFactory:

    def __post_init__(self):
        self.ua = UrlAnalyze()
        self.tf = TableFactory(self.ua)
        self.A_list = []
        self.B_list = []
        self.C_list = []

    def get_listTree(self):
        """获取listtree，并取出message的内容"""
        resp = self.ua.get_response('http://dmp.whchem.com/metadata/topic/listTree?t=1611108227854')
        return resp['message']

    def deal_json(self, json):
        """处理json"""
        for a in json:
            self.deal_element(a)

    def get_table_info(self):
        """获取表信息"""
        ...

    def deal_element(self, element):
        """处理json数据中的每一个element，保存到A_list中"""
        if element['level'] == 1:
            # 如果是1级则实例化A，并迭代获取B
            childTopic = element.pop('childTopic')
            element['childTopic'] = None

            tmp_a = A(**element)

            if len(childTopic) != 0:
                tmp_a.childTopic = [self.deal_element(x) for x in childTopic]

            # 写入关联表信息
            tmp_a.table_info_list = self.tf.get_tables(tmp_a.id)

            self.A_list.append(tmp_a)
            return tmp_a

        elif element['level'] == 2:
            # 如果是2级则实例化B，并迭代获取C
            childTopic = element.pop('childTopic')
            element['childTopic'] = None

            tmp_b = B(**element)

            # 也要考虑，可能B之后没有C的情况
            if len(childTopic) != 0:
                tmp_b.childTopic = [self.deal_element(x) for x in childTopic]
            self.B_list.append(tmp_b)

            # 写入关联表信息
            tmp_b.table_info_list = self.tf.get_tables(tmp_b.id)
            return tmp_b

        elif element['level'] == 3:
            # 如果是3级则实例化C
            childTopic = element.pop('childTopic')
            element['childTopic'] = None

            tmp_c = C(**element)
            self.C_list.append(tmp_c)

            # 写入关联表信息
            tmp_c.table_info_list = self.tf.get_tables(tmp_c.id)
            return tmp_c

        else:
            raise Exception('报错啦！')

    def get_info_from_content_list(self, content_list, save_path):
        """无论是abc list，将结果输出"""
        result_list = []
        for content in content_list:
            path = content.path
            # 根据path获取路径列表
            if content.level == 1:
                temp_list = [path]
            else:
                temp_list = path.split('/')

            for table in content.table_info_list:
                main_list = [table.projectName] + temp_list + [table.name, table.bussinessName]
                result_list.append(main_list)

        aim_columns = ['系统', '一级目录', '二级目录', '三级目录']
        df = pd.DataFrame(result_list, columns=aim_columns[:len(temp_list) + 1] + ['表名', '表中文名'])
        df.to_excel(save_path, index=False)


if __name__ == '__main__':
    cf = ContentFactory()
    message = cf.get_listTree()
    cf.deal_json(message)

    save_dict = {
        '一级目录': cf.A_list,
        '二级目录': cf.B_list,
        '三级目录': cf.C_list,
    }
    for k, v in save_dict.items():
        root_path = r'E:\1-工作\1-工作\20210120-数据目录新'
        save_path = os.path.join(root_path, k + '.xlsx')
        cf.get_info_from_content_list(v, save_path)
