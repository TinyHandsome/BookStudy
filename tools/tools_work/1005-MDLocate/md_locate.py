#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: md_locate.py
@time: 2021/5/25 10:13
@desc: 根据小标题的序号获取整个内容，并输出统计字数
"""

from dataclasses import dataclass
import re
from queue import LifoQueue


@dataclass
class Content:
    level = 0

    def __post_init__(self):
        self.lines = []

    def __repr__(self):
        for line in self.lines:
            if line != '':
                return line + '...'


@dataclass
class MultiWell:
    title: str
    index: str
    level: int
    contents: list
    pattern = re.compile(r'(?P<level>#+)\s*(?:(?P<index>\d*)(?:\.\s*))?(?P<title>.*)')

    def __repr__(self):
        return '#' * self.level + ' ' + self.get_index_info() + self.title + '(' + self.get_contents_info() + ')'

    def get_index_info(self):
        if self.index:
            return self.index + '. '
        else:
            return ''

    def get_contents_info(self):
        infos = []
        for c in self.contents:
            if isinstance(c, Content):
                infos.append('内容')
            else:
                infos.append(str(c))
        return '，'.join(infos)


@dataclass
class MDLocate:
    path: str

    def __post_init__(self):
        self.stack = LifoQueue()
        # 初始化，放一个头进去
        self.stack.put('head')

    def well_check(self, line):
        """检查这一行是不是 #开头 """
        if MultiWell.pattern.match(line):
            # 该行为井号开头
            pattern_match_result = MultiWell.pattern.match(line).groupdict()
            level = len(pattern_match_result.get('level'))
            index = pattern_match_result.get('index')
            title = pattern_match_result.get('title')
            well = MultiWell(title, index, level, [])
            return well
        else:
            return False

    def get_all_info(self):
        """获取MD小说中所有的内容"""
        with open(self.path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()
            if lines != '':
                current_line = self.well_check(line)
                output = self.stack.get()
                if current_line:
                    # 该行为标题 [lastoutput output] current_line
                    if output == 'head':
                        # 为空的话直接写入标题
                        ...
                    else:
                        # 检查output是不是content，是的话，就放入lastoutput中，再检查当前和上上个是否有关系，否则就无事发生
                        if isinstance(output, Content):
                            last_output = self.stack.get()
                            last_output.contents.append(output)
                            # output是Content的话，就给last_output了，然后output变成了last_output
                            output = last_output

                        # output是标题
                        # 检查上一个和这一个的level，如果上一个level大则内容要包含这个，否贼上一个就不入栈了
                        if current_line.level > output.level:
                            output.contents.append(current_line)
                        self.stack.put(output)

                    self.stack.put(current_line)
                else:
                    # 该行为内容
                    if not isinstance(output, Content):
                        # 是不是第一行内容，即栈里面存的是标题
                        # 新建内容，存入line，入栈
                        new_content = Content()
                        new_content.lines.append(line)

                        # 放回标题，再放回新的Content
                        self.stack.put(output)
                        self.stack.put(new_content)
                    else:
                        # 不是第一行内容，则直接把改行存入内容，直接追加内容，并放回Content
                        output.lines.append(line)
                        self.stack.put(output)

        # 操作完了之后，看看最后一个是不是Content，是的话，并且stack不为空的话，放入到前一个well里面
        last_one = self.stack.get()
        if isinstance(last_one, Content) and not self.stack.empty():
            last_well = self.stack.get()
            last_well.contents.append(last_one)
            self.stack.put(last_well)

        print(self.stack.queue)


if __name__ == '__main__':
    sample_path = 'E:/1-工作/3-代码/writting/暗黑童话.md'
    mdl = MDLocate(sample_path)
    mdl.get_all_info()
