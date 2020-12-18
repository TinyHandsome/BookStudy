#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: test_url.py
@time: 2020/9/2 9:41
@desc: 研究python爬虫
"""

import requests

url = 'http://dmpqas.whchem.com/TaskScheduler/process/copyProcess.do'
response = requests.get(url)
fromdata = {
    'processId': 48
}
headers = {
    ""
}
