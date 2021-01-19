#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: content.py
@time: 2021/1/19 17:24
@desc: 数据目录的各个类，三级类
"""

from dataclasses import dataclass


@dataclass
class Base:
    id: int
    creator: str
    create_time: str
    userName: str
    isSystemAdmin: int
    status: str
    level: int
    title: str
    path: str
    description: str
    createdTime: int
    modifiedTime: int
    parentId: int
    childTopicCount: int
    datasetCount: int
    datasetIds: str
    distinctDatasetIds: list
    childTopic: list


@dataclass
class One(Base):
    ...


@dataclass
class Two(Base):
    ...


@dataclass
class Three(Base):
    ...
