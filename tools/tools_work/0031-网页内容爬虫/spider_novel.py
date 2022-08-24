#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: spider_novel.py
@time: 2022/8/24 9:19
@desc: 小说网页爬虫
        核心：当前页数据获取完毕后，获取当前页中，下一页的链接，进行爬虫
"""
import random
import time

from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass
from functools import wraps
import urllib3

urllib3.disable_warnings()


def random_wait(start_t=0, max_t=2):
    """随机等待"""
    time.sleep(random.randint(start_t, max_t))


def retry_anayse(time_limit=3):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            time_count = 0
            while True:
                time_count += 1
                if time_count <= time_limit:
                    try:
                        return function(*args, **kwargs)
                    except Exception as e:
                        continue
                else:
                    raise Exception('重试超过最大次数...')

        return wrapper

    return decorator


@dataclass
class MyNovel:
    current_href: str

    def __post_init__(self):
        ...

    def analyse_url(self, url):
        """分析url获取内容"""
        resp = requests.get(url, verify=False)
        resp.encoding = 'gbk'
        soup = BeautifulSoup(resp.text, "html5lib")

        # 获取正文信息
        aim_content = soup.find(id="content")
        count = 0
        content = ''
        for s in aim_content.strings:
            count += 1

            # 跳过前三行
            if count > 3:
                content += s.strip() + '\n'

        # 获取下一页url
        next_page = soup.find(id="link-next")
        next_page_href = next_page.get('href')

        if next_page_href.endswith('.html'):
            # 找到的是下一章的链接
            return content, next_page_href
        else:
            # 否则结束了，返回的是目录页面
            return content, None

    def analyse(self, time_limit=3):
        """开始遍历"""

        f = open('output.txt', 'w', encoding='utf-8')
        chapter = 1
        while True:

            if self.current_href is None:
                break

            print('正在处理第{}章...'.format(chapter))
            time_count = 0
            while True:
                time_count += 1
                if time_count <= time_limit:
                    try:
                        content, self.current_href = self.analyse_url(self.current_href)
                        break
                    except Exception as e:
                        print('正在重试...')
                        continue
                else:
                    raise Exception('重试超过最大次数...')

            chapter += 1

            f.write(content + '\n')
            # 暂停1-2s
            random_wait(1, 3)

        f.close()


if __name__ == '__main__':
    chapter1_url = 'https://www.zw50.com/book/118193/45642889.html'
    x = MyNovel(chapter1_url)
    x.analyse()
