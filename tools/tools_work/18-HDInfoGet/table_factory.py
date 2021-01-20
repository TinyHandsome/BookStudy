#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: table_factory.py
@time: 2021/1/20 15:33
@desc: 
"""

from dataclasses import dataclass

from selenium_cookie import UrlAnalyze
from table_info import TableInfo


@dataclass
class TableFactory:
    # 一页放多少行
    ua: UrlAnalyze
    default_pageSize = 1000

    def __post_init__(self):
        ...

    def get_response(self, id):
        """根据层级id获取返回值"""
        url = 'http://dmp.whchem.com/metadata/topicDataset/getDatasetInfo?t=1611122689152'
        body = {
            "id": id,
            "sort": "name",
            "order": "desc",
            "page": 1,
            "rows": self.default_pageSize,
            "keyword": ""
        }
        resp = self.ua.get_response(
            url,
            body=body
        )
        return resp

    def get_message_records(self, resp):
        """解析resp"""
        records = resp['message']['records']
        tables = []
        for res in records:
            # 获取bussinessman信息
            res['bussinessName'] = self.get_bussinessName(res['datasetId'])

            t = TableInfo(**res)
            tables.append(t)
        return tables

    def get_common_info(self, datasetId):
        """根据datasetid获取message中的datasetCommoninfo中的businessName（业务名称）"""
        url = 'http://dmp.whchem.com/metadata/datasets/' + str(datasetId) + '/commoninfo?t=1611129382377'
        resp = self.ua.get_response(url, method='get')
        return resp

    def get_message_datasetCommonInfo_businessName(self, resp):
        """获取bussinessName"""
        return resp['message']['datasetCommonInfo']['businessName']

    def get_tables(self, id):
        """总结上面两个函数"""
        return self.get_message_records(self.get_response(id))

    def get_bussinessName(self, datasetId):
        """总结上面两个函数"""
        return self.get_message_datasetCommonInfo_businessName(self.get_common_info(datasetId))


if __name__ == '__main__':
    ua = UrlAnalyze()
    tf = TableFactory(ua)
    print(tf.get_tables(77))
