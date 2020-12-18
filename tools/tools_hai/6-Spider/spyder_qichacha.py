#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: spyder_qichacha.py
@time: 2020/10/17 23:17
@desc: 对企查查爬虫
"""

# -*- coding-8 -*-
import requests
import lxml
import sys
from bs4 import BeautifulSoup
import xlwt
import time
import urllib

import requests
from lxml import etree

url = "https://www.qcc.com/search?key=爱奇艺#index:14&"

hed = {
    "host": "www.qcc.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
    "upgrade-insecure-requests": "1",
    "cookie": "QCCSESSID=vpk1mpc45ci95eu83etg528881; zg_did=%7B%22did%22%3A%20%221732cdcac86bf-0039dd6baef69a-4353761-100200-1732cdcac8844f%22%7D; UM_distinctid=1732cdcb0a713b-01b058b949aa5a-4353761-100200-1732cdcb0ab44e; hasShow=1; _uab_collina=159418552807339394444789; acw_tc=7d27c71c15941953776602556e6b8442bc8001e4e1270e8fead4b79557; CNZZDATA1254842228=1092104090-1594185078-https%253A%252F%252Fwww.baidu.com%252F%7C1594195878; Hm_lvt_78f134d5a9ac3f92524914d0247e70cb=1594194111,1594195892,1594195918,1594196042; Hm_lpvt_78f134d5a9ac3f92524914d0247e70cb=1594196294; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201594185526424%2C%22updated%22%3A%201594196294349%2C%22info%22%3A%201594185526455%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%5C%22%24utm_source%5C%22%3A%20%5C%22baidu1%5C%22%2C%5C%22%24utm_medium%5C%22%3A%20%5C%22cpc%5C%22%2C%5C%22%24utm_term%5C%22%3A%20%5C%22pzsy%5C%22%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%22fd05f1ac2b561244aaa6b27b3bb617a4%22%7D",
}

resq = requests.get(url=url, headers=hed).content
response = etree.HTML(resq)

title_list = []
title = response.xpath('//*[@id="search-result"]//tr/td[3]/a//text()')

for tit in title:
    tit = tit.replace(',', '').strip()
    title_list.append(tit)

addr_list = []
addrs = response.xpath('//*[@id="search-result"]//tr/td[3]/p[4]//text()')
for addr in addrs:
    addr = addr.replace(',', '').strip()
    addr_list.append(addr)

print(title_list)
print(addr_list)
