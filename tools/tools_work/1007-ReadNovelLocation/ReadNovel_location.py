"""
对vscode插件：ReadNovel提供内容查找和页码定位的操作
"""

import sys
sys.path.append("E:/1-Work/3-Code/tools/tools_py")
from constants import get_vscode_json_dict

from dataclasses import dataclass

vscode_json_dict = get_vscode_json_dict()
book_path = vscode_json_dict.get("ReadNovel.filePath")


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
    lrn.find_page('生命涅槃')


if __name__ == '__main__':
    main()
