"""
对vscode插件：ReadNovel提供内容查找和页码定位的操作
"""

# -----------------【可以删除】---------------------
# 这里是获取vscode配置文件json，读取成dict的过程
import sys
sys.path.append("E:/1-Work/3-Code/tools/tools_py")
from constants import get_vscode_json_dict
vscode_json_dict = get_vscode_json_dict()
# --------------------------------------------------


import os
from dataclasses import dataclass

# 可以直接把文件路径粘到这里就行，不需要像我这样从vscode的配置文件中
book_path = vscode_json_dict.get("ReadNovel.filePath")
book_name = os.path.split(book_path)[-1]


@dataclass
class LocationReadNovel:

    def __post_init__(self):
        self.lines_without_blank = self.read_aim_file()

    def read_aim_file(self):
        with open(book_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return [x for x in lines if len(x.strip()) > 0]

    def find_page(self, words):
        index = 0
        infos = []
        for l in self.lines_without_blank:
            if words in l:
                infos.append((index, l))
            index += 1

        # 展示
        for i, info in infos:
            print(i, ': ', info)


def main():
    lrn = LocationReadNovel()
    print('当前书名：', book_name)
    while True:
        find_words = input("请输入检索内容：（输入q退出）\n\r")
        if find_words.strip() == 'q':
            break
        lrn.find_page(find_words)


if __name__ == '__main__':
    main()
