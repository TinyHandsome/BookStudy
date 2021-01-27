#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: table_info.py
@time: 2021/1/20 15:28
@desc: 
"""

from dataclasses import dataclass


@dataclass
class TableInfo:
    datasetId: int
    topicId: int
    creator: str
    createdTime: str
    modifiedTime: str
    name: str
    owner: str
    description: str
    path: str
    projectName: str
    lastModifyTime: str
    source: str
    useCount: int
    useProject: str
    type: str
    isDefault: int

    # 特殊，表信息，这里只要业务名称的描述
    bussinessName: str

    def __post_init__(self):
        ...
