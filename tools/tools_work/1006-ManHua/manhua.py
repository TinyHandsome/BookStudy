#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: manhua.py
@time: 2021/10/25 13:30
@desc: 《杀戮都市》漫画获取所写脚本 end chapter 2766138
        https://res99.shut123.com/image/view/2766078/9.webp
        1. [Max retries exceeded with url (Caused by NewConnectionError(urllib3.connection...)](https://blog.csdn.net/wangziyang777/article/details/106670320/)
"""
import os
import random
import time
from io import BytesIO
from system_hotkey import SystemHotkey

import requests
from PIL import Image
from dataclasses import dataclass

# 可能存在数据丢失的情况，报错：【OSError: image file is truncated】，这里设置加载截断的图片
from PIL import ImageFile, UnidentifiedImageError

ImageFile.LOAD_TRUNCATED_IMAGES = True

root_url = 'https://res99.shut123.com/image/view/'
save_path = 'E:/img_temp/'


@dataclass
class ManHua:
    start_chapter = 2766062
    end_chapter = 2766062
    page = 0

    def __post_init__(self):
        self.hk = SystemHotkey()
        self.current_save_path = save_path + str(self.start_chapter) + '/'
        self.hk.register(('control', 'e'), callback=lambda e: self.next_page())

    def update_save_path(self):
        self.current_save_path = save_path + str(self.start_chapter) + '/'

        # 检查文件夹是否存在，不存在就创建吧
        if not os.path.exists(self.current_save_path):
            os.makedirs(self.current_save_path)

    def get_img(self):
        # 这里修复连接次数太多导致的达到最大重试次数，以至于无法连接的问题
        # 1. 请求头上加 headers = {'Connection':'close'}
        # 2. s = requests.session() s.keep_alive = False
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
            'Connection': 'close',
        }
        url = root_url + str(self.start_chapter) + '/' + str(self.page) + '.webp'

        # 这里需要加上请求头哦
        a = requests.get(
            url, headers=headers,
            # verify=False
        )
        s = requests.session()
        s.keep_alive = False

        # 404说明没有下一页啦
        if a.status_code == 404:
            return 404

        f = BytesIO(a.content)

        # 如果检测到图片无法识别，直接给一个空白页好了
        try:
            img = Image.open(f)
        except UnidentifiedImageError as e:
            img = Image.new('1', (256, 256), 1)

        if img.mode == 'P' or img.mode == 'RGBA':
            img = img.convert('RGB')
        a.close()
        return img

    def show_img(self, img):
        img.show()

    def next_page(self):
        self.page += 1

    def next_chapter(self):
        self.page = 0
        self.start_chapter += 1
        self.update_save_path()
        return self.start_chapter > self.end_chapter

    def save_img(self, img):
        if not os.path.exists(self.current_save_path):
            os.makedirs(self.current_save_path)

        img.save(self.current_save_path + str(self.page) + '.jpg')


if __name__ == '__main__':
    mh = ManHua()
    while True:
        print('current location:', mh.start_chapter, mh.page)
        img = mh.get_img()

        if img != 404:
            mh.save_img(img)
            mh.next_page()
        else:
            if mh.next_chapter():
                break
            print("the latest save path: ", mh.current_save_path)
        time.sleep(random.random() + 1)
