#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: selenium_cookie.py
@time: 2021/1/20 9:09
@desc: 通过selenium模拟登录后，获取cookie，然后根据目标网页获取返回值
        1. [python3爬虫系列20之反爬需要登录的网站三种处理方式](https://zoutao.blog.csdn.net/article/details/103347093)
        2. [Python Selenium库的使用](https://blog.csdn.net/weixin_36279318/article/details/79475388)
        3. [显示等待WebDriverWait](https://www.cnblogs.com/fireporsche/p/9517009.html)
"""
import json

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dataclasses import dataclass
import time
import requests
from info_py_ini import info


@dataclass
class UrlAnalyze:

    def __post_init__(self):
        self.cookie = None
        self.driver_path = 'driver/chromedriver.exe'

    def login(self, login_path, info_py=True):
        self.browser = webdriver.Chrome(executable_path=self.driver_path)

        if info_py:
            username = info['username']
            password = info['password']
        else:
            username = input('请输入用户名：')
            password = input("请输入密码：")

        self.browser.get(login_path)
        # 页面最大化
        self.browser.maximize_window()

        # 显示等待
        WebDriverWait(self.browser, 20, 0.5).until(EC.presence_of_element_located((By.ID, 'username')))
        # time.sleep(1)

        # 填写用户名和密码
        self.browser.find_element_by_id('username').send_keys(username)
        self.browser.find_element_by_id('password').send_keys(password)
        self.browser.find_element_by_id('FormLoginBtn').click()
        time.sleep(2)

    def get_cookie(self, save_cookie=True):
        cookie = self.browser.get_cookies()
        result_cookie = ''
        for i in cookie:
            name = i['name']
            value = i['value']

            result_cookie += name + '=' + value + '; '

        self.cookie = result_cookie[:-2]
        if save_cookie:
            with open('cookie/cookie.plk', 'w') as f:
                f.write(self.cookie)
        self.browser.quit()

    def login_and_set_cookie(self, login_path):
        """模拟登录，并设置cookie"""
        self.login(login_path)
        self.get_cookie()

    def get_response(self, url, method='post', login_path='', body=None):
        if login_path == '':
            with open('cookie/cookie.plk', 'r') as f:
                self.cookie = f.readline()
        else:
            self.login_and_set_cookie(login_path)
        headers = {
            'Cookie': self.cookie
        }

        if method == 'post':
            return requests.post(url, headers=headers, json=body).json()
        elif method == 'get':
            return requests.get(url, headers=headers, json=body).json()
        else:
            print('错误！获取方式不正确！')
            return None


if __name__ == '__main__':
    ua = UrlAnalyze()
    # ua.login_and_set_cookie('http://dmp.whchem.com/leapid-admin/view/login.html')
    # resp = ua.get_response('http://dmp.whchem.com/metadata/topic/listTree?t=1611108227854')

    # 获取列表信息
    resp = ua.get_response('http://dmp.whchem.com/metadata/topicDataset/getDatasetInfo?t=1611122689152', body={"id": 2, "sort": "name", "order": "desc", "page": 1, "rows": 1000, "keyword": ""})
    print(resp)
