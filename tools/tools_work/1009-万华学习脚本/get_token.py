#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: get_token.py
@time: 2022/1/17 8:34
@desc: 获取万华学习登录的token

        参考链接：
            1. (史上最全！Selenium元素定位的30种方式)[https://blog.csdn.net/qq_32897143/article/details/80383502]
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from password import *

LOGIN_URL = 'https://learning.whchem.com:4443/?action=loginout'

# 配置设置
chrome_options = webdriver.ChromeOptions()
# 设置无界面模式
# chrome_options.add_argument('--headless')
# 设置忽略警告提示语
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation', 'load-extension'])
# 不保存密码
prefs = {
    'credentials_enable_service': False,
    'profile.password_manager_enabled': False
}
chrome_options.add_experimental_option('prefs', prefs)

# 设置显式等待的时间
EXPLICIT_WAIT_TIME = 20


# 显示获取属性
def get_element(my_browser, target_name, my_type='class'):

    type_dict = {
        'class': By.CLASS_NAME,
    }

    result = WebDriverWait(my_browser, EXPLICIT_WAIT_TIME).until(
        EC.presence_of_all_elements_located((type_dict.get(my_type), target_name))
    )
    if len(result) == 1:
        return result[0]
    else:
        return result


browser = webdriver.Chrome('E:/1-Work/3-Code/tools/tools_work/0018-HDInfoGet/driver/chromedriver.exe',
                           options=chrome_options)
browser.get(LOGIN_URL)
# 设置浏览器大小
browser.set_window_size(400, 1000)

# 登录
get_element(browser, 'login_username', 'class').send_keys(username)
get_element(browser, 'login_password', 'class').send_keys(password)
get_element(browser, 'login_button', 'class').click()
# 感谢下载，同意
get_element(browser, 'agreement-btn-yes', 'class').click()
# 点击去完成
get_element(browser, 'task-no-status', 'class').click()

# 每日登录，必修课程，选学课程，每周一练，闯关答题，调查问卷，同学PK
my_tasks = get_element(browser, 'task-list-item', 'class')
print(my_tasks)


