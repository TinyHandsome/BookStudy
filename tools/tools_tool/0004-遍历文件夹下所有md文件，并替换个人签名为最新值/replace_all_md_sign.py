"""
    遍历md文件，替换签名，每个文件都需要确认，输出替换前的内容
"""

import os

root_path = 'E:/1-Work/3-Code/'
replace_info = '''
- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
'''
replace_find = '---'
aim_suffix = '.md'


class File:
    def __init__(self, path):
        self.path = path
        with open(path, 'r', encoding='utf-8') as ff:
            self.content: list = ff.readlines()
        self.content: list = [x.replace('\n', '') for x in self.content]
        self.len_con = len(self.content)

        self.find, self.aim_signal = self.see_file()

    def see_file(self):
        for cc in self.content[::-1]:
            if replace_find in cc:
                return True, cc

        return False, ''

    def get_info(self):
        ii = self.len_con - self.content[::-1].index(self.aim_signal)
        self.original = "\n".join(self.content[ii+1:])
        self.before = "\n".join(self.content[:ii+1])

    def replace_end(self, replace_content):
        result = self.before + '\n' + replace_content

        with open(self.path, 'w+', encoding='utf-8') as f:
            f.write(result)

    def check_consistent(self, replace_content):
        
        # print(self.original)
        # print(replace_content)
        # print(self.original == replace_content)
        # print(len(self.original), len(replace_content))
        # print(self.original[-1], replace_content[-1])
        # print(self.original[-2], replace_content[-2])


        if -5 < len(self.original) - len(replace_content) < 5:
            return True

        return False


def main():
    for (root, dirs, files) in os.walk(root_path):
        for f in files:
            if f.endswith(aim_suffix):
                # 找到以.md为结尾的文件
                file_path = os.path.join(root, f)
                F = File(file_path)
                F.get_info()

                if F.find:

                    # 如果替换过或者一致就不换咯
                    if F.check_consistent(replace_info):
                        continue

                    print(f)
                    print(F.original)
                    x = input('是否替换?（q退出）\n')
                    print('\n')
                    if x == 'y':
                        F.replace_end(replace_info)
                    elif x == 'q':
                        exit()
                    else:
                        continue

                os.system('cls')


if __name__ == '__main__':
    # f = File(root_path + 'README.md')
    # f.get_info()
    # f.replace_end(replace_info)

    main()
