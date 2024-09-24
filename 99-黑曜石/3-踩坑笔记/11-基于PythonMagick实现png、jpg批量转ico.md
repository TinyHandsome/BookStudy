# 基于PythonMagick实现png、jpg批量转ico

## 写在前面

- 做这件事的原因：
  1. 下了一堆png图标
  2. 想批量转为ico格式的，然后给文件夹用

- 使用方式：

  ```python
  if __name__ == '__main__':
      pi = PNG2ICO(r'E:\resources\ico', r'E:\resources\ico_output_by_python')
      pi.walk_files()
  
      '''单个文件测试'''
      # PNG2ICO.png2ico(r'E:\resources\ico\基础多色\chenggong.png', '13.ico')
  ```

  1. 生成类对象，传入的参数由两个：
     1. 有png或其他格式图片的文件夹路径（该路径下的子文件夹中的图片也能识别）
     2. 输出路径
  2. 调用类对象的`walk_files()`函数实现
  3. 如果想单独对一个文件进行测试的话，可以参考下面的 **单个文件测试**

## 代码实战

```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: png2ico.py
@time: 2021/6/2 10:21
@desc: png转ico工具
"""

from dataclasses import dataclass
import PythonMagick
import os


@dataclass
class PNG2ICO:
    root_path: str
    output_path: str

    def __post_init__(self):
        # output路径检测，没有就创建
        self.check_path_exists(self.output_path)

    @staticmethod
    def check_path_exists(path):
        if not os.path.exists(path):
            os.makedirs(path)

    @staticmethod
    def png2ico(file_path, output_path, default_size='256x256'):
        """
        :param file_path: 目标文件夹路径
        :param output_path: 输出文件夹路径
        :param default_size: 默认生成的大小
        :return:
        """
        im = PythonMagick.Image(file_path)
        im.sample(default_size)
        im.write(output_path)

    def walk_files(self):
        for root, dirs, files in os.walk(self.root_path, topdown=True):
            for file in files:
                # print(self.output_path, self.root_path, root, os.path.splitext(file))
                file_path = os.path.join(root, file)
                output_path = os.path.join(root.replace(self.root_path, self.output_path))
                # 检查子路径是否存在
                self.check_path_exists(output_path)

                output_file_path = os.path.join(output_path, os.path.splitext(file)[0] + '.ico')
                self.png2ico(file_path, output_file_path)


if __name__ == '__main__':
    pi = PNG2ICO(r'E:\resources\ico', r'E:\resources\ico_output_by_python')
    pi.walk_files()

    '''单个文件测试'''
    # PNG2ICO.png2ico(r'E:\resources\ico\基础多色\chenggong.png', '13.ico')
```

------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
