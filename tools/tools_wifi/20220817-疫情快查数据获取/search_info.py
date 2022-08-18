#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: search_info.py
@time: 2022/8/17 9:13
@desc: 获取疫情快查服务中的数据
        1. 学习链接：https://blog.csdn.net/sgld995/article/details/123451146
        2. find_element_by_xpath()使用的几种方法：https://blog.csdn.net/qq_32189701/article/details/100176577
        3. selenium、webdriver打开Chrome浏览器闪退问题（版本号一致）：https://blog.csdn.net/weixin_42603129/article/details/105561926
        4. 学这一篇就够啦：https://blog.csdn.net/qq_43098690/article/details/121341442
        5. selenium的3种等待方式：https://www.cnblogs.com/x00479/p/14254001.html
"""
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def increase_speed():
    """加快网页加载速度"""
    options = webdriver.ChromeOptions()
    prefs = {
        'profile.default_content_setting_values': {
            # 不加载图片
            'images': 2,
            # 禁用css
            # 'permissions.default.stylesheet': 2,
            # 禁用js
            # 'javascript': 2,
        }
    }
    options.add_experimental_option('prefs', prefs)
    return options


class EpidemicPrevention:

    def __init__(self, driver=None):
        if driver is None:
            self.driver = webdriver.Chrome()
        else:
            self.driver = driver

    def implicitly_wait(self, t=10):
        """隐式等待"""
        self.driver.implicitly_wait(t)

    def driver_wait(self, method, info, wait_time=60, check_time=0.5):
        """显示等待"""
        locator = (method, info)
        WebDriverWait(self.driver, wait_time, check_time).until(EC.presence_of_element_located(locator))

    def random_wait(self, start_t=0, max_t=2):
        """随机等待"""
        time.sleep(random.randint(start_t, max_t))

    def maximize_window(self):
        self.driver.maximize_window()

    def get_url(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def send_key_to_input(self, element: WebElement, info: str):
        """将值输入到输入框"""
        self.implicitly_wait()
        element.send_keys(info)

    def click(self, element: WebElement, sleep_time=1):
        """模拟点击"""
        element.click()
        self.random_wait(sleep_time, sleep_time + 1)

    def switch_latest_handle(self):
        """跳转句柄"""
        all_handle = self.driver.window_handles
        self.driver.switch_to.window(all_handle[-1])

    def find_element_by_name(self, name):
        self.driver_wait(By.NAME, name)
        return self.driver.find_element_by_name(name)

    def find_element_by_class_name(self, cls_name):
        self.driver_wait(By.CLASS_NAME, cls_name)
        return self.driver.find_element_by_class_name(cls_name)

    def find_element_by_xpath(self, xpath):
        self.driver_wait(By.XPATH, xpath)
        return self.driver.find_element_by_xpath(xpath)

    def find_elements_by_xpath(self, xpath):
        self.driver_wait(By.XPATH, xpath)
        return self.driver.find_elements_by_xpath(xpath)

    def find_element_by_xpath_contains_text(self, tag, info):
        """【简单直接查找】根据元素内容模糊查找定位元素"""
        return self.driver.find_element_by_xpath("//{}[contains(text(),'{}')]".format(tag, info))

    def get_page_source(self):
        """打印网页的源码"""
        return self.driver.page_source


if __name__ == '__main__':
    ...
