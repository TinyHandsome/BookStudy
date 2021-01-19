#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: get_content_info.py
@time: 2021/1/19 17:01
@desc: 获取数据目录的内容
"""

import requests
from my_cookies import headers
from dataclasses import dataclass


@dataclass
class GetContentInfo:
    url: str

    def get_listTree(self):
        """获取json数据"""
        response = requests.post(self.url, headers=headers)

        # 字典
        response_dict = response.json()
        message = response_dict.get('message')
        return message

    def analyze_dict(self):
        """对字典进行解析"""
        message = self.get_listTree()




if __name__ == '__main__':
    url = 'http://dmp.whchem.com/metadata/topic/listTree?t=1611046438759'
    data = GetContentInfo(url).get_listTree()
