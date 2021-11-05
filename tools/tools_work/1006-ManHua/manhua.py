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
        2. [OSError: encoder error -2 when writing image file](https://blog.csdn.net/kasagawa/article/details/7841935)
"""
import os
import random
import time
from functools import reduce
from io import BytesIO
from system_hotkey import SystemHotkey

import requests
from PIL import Image
from dataclasses import dataclass

# 可能存在数据丢失的情况，报错：【OSError: image file is truncated】，这里设置加载截断的图片
from PIL import ImageFile, UnidentifiedImageError

ImageFile.LOAD_TRUNCATED_IMAGES = True

BASE_PAUSE_TIME = 1

root_url = 'http://img.wwmh.xyz/bookimages/1498/'
save_path = 'E:/img_temp/'


@dataclass
class ManHua:
    start_chapter: int
    end_chapter: int
    page: int = 1

    def __post_init__(self):
        self.hk = SystemHotkey()
        self.current_save_path = save_path
        self.hk.register(('control', 'e'), callback=lambda e: self.next_page())

        self.current_chapter_long_imgs = []

    def reset_long_img(self):
        self.current_chapter_long_imgs.clear()

    def update_long_img(self, img):
        self.current_chapter_long_imgs.append(img)

    def generate_long_img(self):
        """垂直拼接图片，宽为所有图片最宽，长为所有图片长的和"""
        y = sum([img.size[1] for img in self.current_chapter_long_imgs])
        x = max([img.size[0] for img in self.current_chapter_long_imgs])
        long_img = Image.new('RGB', (x, y))

        current_loc = (0, 0)
        for img in self.current_chapter_long_imgs:
            long_img.paste(img, current_loc)
            current_loc = (current_loc[0], current_loc[1] + img.size[1])

        return long_img

    def update_save_path(self):
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
        url = root_url + str(self.start_chapter) + '/' + str(self.page) + '.jpg'

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
        """
        切换下一章节，重置页数为0，默认章节加1
        :return:
        """
        self.page = 1
        self.start_chapter += 1

        # 合成大图列表置空
        self.reset_long_img()
        return self.start_chapter > self.end_chapter

    def save_img(self, img, name=None):
        """
        保存图片
        :param img: 图片
        :param name: 保存的图片名称，没有的话，默认为章节名称
        """
        if not os.path.exists(self.current_save_path):
            os.makedirs(self.current_save_path)

        if name is None:
            name = str(self.start_chapter)

        # 保存图片时，需要考虑设置MAXBLOCK，因为大图容易报错
        img.save(self.current_save_path + name + '.png', optimize=True)

    def get_chapters(self):
        """
        获取对应的章节
        """
        while True:
            print('current location:', mh.start_chapter, mh.page)
            img = mh.get_img()

            if img != 404:
                mh.update_long_img(img)
                mh.next_page()
            else:
                if mh.current_chapter_long_imgs:
                    # 一张图都没有，这一章直接跳过；否则才保存图片
                    # 合成长图，并保存
                    long_img = mh.generate_long_img()
                    mh.save_img(long_img)
                else:
                    print("current chapter {} is null".format(self.start_chapter))

                if mh.next_chapter():
                    break
            time.sleep(random.random() + BASE_PAUSE_TIME)

        print("the latest save path: ", mh.current_save_path)


if __name__ == '__main__':
    single = 233380
    mh = ManHua(single, single, 1) #20 233323
    mh.get_chapters()
