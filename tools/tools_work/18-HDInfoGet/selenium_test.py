#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: selenium_test.py
@time: 2021/1/19 16:47
@desc: 获取LeapHD的数据信息，处理数据目录
"""

"""
1. [python3爬虫系列20之反爬需要登录的网站三种处理方式](https://zoutao.blog.csdn.net/article/details/103347093)
2. [Python Selenium库的使用](https://blog.csdn.net/weixin_36279318/article/details/79475388)
"""

from selenium import webdriver
import time
import requests


def get_cookies(url):
    chrome_driver = 'E:/1-工作/1-工作/20210119-数据目录/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chrome_driver)
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_id('username').send_keys('litian')
    driver.find_element_by_id('password').send_keys('tian,1234')
    driver.find_element_by_id('FormLoginBtn').click()
    time.sleep(1)
    cookie = driver.get_cookies()
    driver.quit()
    return cookie


def add_cookies(cookie):
    c = requests.cookies.RequestsCookieJar()
    for i in cookie:
        c.set(i['name'], i['value'])
    s.cookies.update(c)


def get_response(url):
    return requests.post(url)


if __name__ == "__main__":
    s = requests.session()
    url = 'http://dmp.whchem.com/metadata/topic/listTree?t=1611042943489'
    cookie = get_cookies(url)
    add_cookies(cookie)
    print(get_response(url).json())

    url = 'http://dmp.whchem.com/metadata/topic/listTree?t=1611046438759'
    cookies = {
        'Cookie': '_anaf_uid=3fda64b4-c20a-461c-9b33-889ec0d323c7; UM_distinctid=174b97d78867c5-081055ee29fab5-333376b-1fa400-174b97d78878b4; Hm_lvt_ef1360f1163a78cfe7c5c8a905ea7b89=1608357334; lang=zh; _anaf_uid_visit=623; _anaf_uid_save=3fda64b4-c20a-461c-9b33-889ec0d323c7.1596778779.201.1611024343.1611021019.1b863d90-fc73-4fbf-ba84-eb0602669171; _anaf_hc_traceId=8daccd3d-8cb5-4e4d-9bbb-b56524c95b16; codeKey=1611046175; _sid_=ac553f3e63d64c7495bd13ea29902cdd; _lpt_=ac553f3e63d64c7495bd13ea29902cdd; username=litian; roles=leapid.pm%2Csql%2Cproc%2Cdhub; id=163; created=1609896831451; domain=http://dmp.whchem.com; timestamp=1611046173106; currentProjectId=65; sysid=p65_g63'
    }

    result = requests.post(url, headers=cookies)
    print(result.json())
