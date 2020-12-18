#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: test1.py
@time: 2020/10/17 23:40
@desc:
参考连接：
    1. [学习连接](https://www.cnblogs.com/zhangxinqi/p/9210211.html#_label4)
    2. [api](https://lxml.de/api/lxml.etree._Element-class.html)

"""

import requests
from lxml import etree
import pandas as pd
import time, random


class AimTable:
    def __init__(self, value_list):
        self.value_list = value_list
        self.chigu_index = self.count_index()
        self.num = value_list[0]
        self.gudong = value_list[1]
        self.end_list = value_list[self.chigu_index:]
        self.middle_list = value_list[2:self.chigu_index]
        self.middle = self.deal_middle()

    def deal_middle(self):
        return "_".join(self.middle_list)

    def get_list(self):
        return [self.num, self.gudong, self.middle] + self.end_list

    def count_index(self):
        count = 0
        for value in self.value_list:
            if '%' in value:
                return count
            count += 1


def get_link(firm_links):
    for link in firm_links:
        if 'partnerslist' in link:
            return ('https://www.qcc.com/' + link)


def get_response(url):
    hed2 = {
        'cookie': 'zg_did=%7B%22did%22%3A%20%22175371477da24f-0e36bf4e81feae-333376b-1fa400-175371477db2d5%22%7D; UM_distinctid=17537147a5b47-0bc55d6c2b5fca-333376b-1fa400-17537147a5c76c; _uab_collina=160294689296135835264877; QCCSESSID=h6bbldi2hujlj8r92mt66ons21; hasShow=1; acw_tc=73df119b16030795287916696ebd833f6007f6853f943ea7a11ff92278; CNZZDATA1254842228=489385317-1602942637-https%253A%252F%252Fwww.baidu.com%252F%7C1603077652; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201603079529268%2C%22updated%22%3A%201603079534813%2C%22info%22%3A%201602946889699%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%5C%22%24utm_source%5C%22%3A%20%5C%22baidu1%5C%22%2C%5C%22%24utm_medium%5C%22%3A%20%5C%22cpc%5C%22%2C%5C%22%24utm_term%5C%22%3A%20%5C%22pzsy%5C%22%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%22366d7751c1560d080e3b2f3a9e5e1d21%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%7D',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }

    resq = requests.get(url=url, headers=hed2).content.decode('utf-8')
    return resq


def get_dataframe(key):
    resq = get_response('https://www.qcc.com/search?key=' + key)
    html = etree.HTML(resq)
    # //代表获取子孙节点，*代表获取所有，这里获取了所有的连接，所以要把partnerslist记录取出来
    firm_links = html.xpath('//tr/td/p[@class="m-t-xs m-b-n-xs"]/a/@href')
    partn = get_link(firm_links)

    # 获取公司的信息
    resq_partn = get_response(partn)
    html2 = etree.HTML(resq_partn)
    aa = html2.xpath('//table[@class="ntable ntable-odd npth nptd"]/tr')

    # 表头
    cols = []
    table_columns = aa[0]
    for r in table_columns.itertext():
        if r.strip() != '':
            cols.append(r.strip())

    # 内容
    infos = aa[1:]
    data = []

    for r in infos:
        line = []
        for v in r.itertext():
            sv = v.strip()
            if sv != '' and '>' not in sv:
                line.append(sv)

        temp = AimTable(line)
        # print(temp.get_list())
        data.append(temp.get_list())

    result = pd.DataFrame(data, columns=cols)

    save_path = 'E:/【冲鸭】/【我海】1. 选我就完事儿了/20201019-投资事件/公司信息/' + key + '.xlsx'
    result.to_excel(save_path, index=False)


if __name__ == '__main__':
    root_path = 'E:/【冲鸭】/【我海】1. 选我就完事儿了/20201019-投资事件/'
    path = root_path + '投资事件.xlsx'
    df = pd.read_excel(path)
    names = df['投资方全称']
    indexs = df.index

    # 报错记录
    error_info = []

    # 测试数据
    # indexs = [1]
    # names = ['上海国有资产经营有限公司']

    for index, name in zip(indexs, names):
        print(index, ':', name)

        # 测试
        # get_dataframe(name)

        if name != '不公开的投资者':
            try:
                get_dataframe(name)
            except Exception as e:
                error_info.append([name, e])
                print(e)
                pass

        # 暂停下，给服务器一个机会
        time.sleep(random.random())

    # 保存错误文件
    errors = pd.DataFrame(error_info, columns=['投资方全称', '报错信息'])
    errors.to_excel(root_path + 'errors.xlsx', index=False)
    print('失败的数量：', errors.shape[0])

    # get_dataframe('君联资本管理股份有限公司')
