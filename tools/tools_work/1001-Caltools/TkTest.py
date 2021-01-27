#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: TkTest.py
@time: 2020/1/15 14:27
@desc: 小学生作业专用小程序
        【version 1.2】   增加防重功能，结果不超过limits  20200117
        01. 防止出现重复的计算题
        02. 加法的结果不能超过limits
        03. 增加每道题结果的编号
        04. 修改tkinter默认羽毛图标为53
        05. 增加作者联系方式
        06. 增加使用说明
        07. 设置窗口不可拉伸
        08. 100分设置高亮
        09. 设置字体大小和颜色，参考链接：https://blog.csdn.net/foneone/article/details/100915340
        10. 更改response字体大小为30
        11. 修改各个字体的样式，增加居中，（主要是修改tag_config方法）
            参考链接：https://www.cnblogs.com/pinpin/p/9960779.html
        12. 更新颜色设置，对了是绿色，错了是红色
        13. 标题增加版本号
        14. 禁止用户修改Text内容

        【version 1.1】   新增界面功能  20200115
        01. 增加交互界面
        02. 统计最后正确率并输出得分
        03. 修正滚轮问题
        04. 增加设置题目数目控制
        05. 增加设置多少以内加减法控制
        06. 增加回车submit并刷新界面控制
        07. 将py文件用pyinstaller打包，打包代码：pyinstaller -w -F -i 53.ico TkTest.py
           其中
           -w是指win模式，使用Windows子系统执行.当程序启动的时候不会打开命令行
           -F是最后产生一个文件，与之相对应的是-D
           -i是添加ico图标
           参考链接：https://blog.csdn.net/zy1007531447/article/details/103296725

        【version 1.0】   实现基本功能  20200115
        01. 输入数字a，计算a以内的加减法
"""
import tkinter as tk
import tkinter.font as tf
from Caltool import Caltool
from Ico_repair import ico_repair
import os


class TkTest:

    def __init__(self):
        # 界面
        root = tk.Tk()
        root.title('小朋友加减法刷题工具[v1.2]【作者: 李英俊小朋友，litian_cup@163.com】')
        # 修改图标 | 这里在导出成exe的时候会报错，改成下面的函数时，则不会了
        # root.iconbitmap('53.ico')
        temp_name = ico_repair(root)
        # 设置窗口不可变
        root.resizable(0, 0)
        self.font_title = ("Microsoft YaHei", 12)
        self.font_write = ("Microsoft YaHei", 22)
        self.font_button = ("Microsoft YaHei", 12)
        self.font_text = ("Microsoft YaHei", 12)
        self.font_times = ("Microsoft YaHei", 16)
        self.font_response = tf.Font(family="微软雅黑", size=30)

        # 计算方法
        self.tt = Caltool()

        # 参数区
        self.answer = None
        self.result = None
        self.flag = None
        self.info = None
        self.strings = ''
        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
        self.var3 = tk.StringVar()
        self.var3.set(5)
        self.var4 = tk.StringVar()
        self.var4.set(20)

        def clear_text():
            """清除Text内容"""
            # 0.0代表0行的第0个元素
            self.t1.config(state=tk.NORMAL)
            self.t1.delete(0.0, tk.END)
            self.t1.config(state=tk.DISABLED)

        def clear_entry():
            """清除entry"""
            self.var1.set('')
            self.var2.set('')

        def write(xx, loc="end", c='black'):
            """写入Text内容"""
            self.t1.config(state=tk.NORMAL)
            self.t1.insert(loc, xx, c)
            self.t1.config(state=tk.DISABLED)

        def start():
            clear_text()
            clear_entry()
            ti, self.result, self.info = self.tt.next_ti()
            self.var1.set(ti)
            self.var2.set('')
            self.tt.reset()
            self.tt.count = int(self.var3.get())
            self.tt.number_limit = int(self.var4.get())

        def submit_(event):
            submit()

        def submit():
            clear_text()
            if self.var1.get() == '':
                xx = '还没有召唤题目哦！\n'
                write(xx, c='big_red')
                return
            try:
                self.answer = int(self.var2.get())
            except:
                xx = '只许输入数字哦，小朋友！\n'
                write(xx, c='big_red')
                return
            if self.answer == self.result:
                xx = '题' + str(self.tt.xuhao + 1) + ': (√)恭喜你答对啦！\n'
                write(xx, c='big_green')
                self.tt.sum += 1
                self.flag = True

            else:
                xx = '题' + str(self.tt.xuhao + 1) + ': (×)答错了哦！\n'
                write(xx, c='big_red')
                self.flag = False

            self.tt.strings += self.info + '\t\t你的答案：' + str(self.answer) + '\t\t正确答案：' + str(self.result) + '\t\t' + (
                '√' if self.flag else '×') + '\n'
            self.tt.xuhao += 1

            # 如果计算的个数达到预计了，则输出结果
            if self.tt.check():
                clear_text()
                write(self.tt.strings + '*' * 100 + '\n' + '小朋友你的得分是：')
                write(str(int((self.tt.sum / self.tt.count) * 100)) + '分', c='red')
                write('\n')
                clear_entry()
                self.tt.reset()

            else:
                ti, self.result, self.info = self.tt.next_ti()
                self.var1.set(ti)
                self.var2.set('')

        f1 = tk.Frame(root)
        l1 = tk.Label(f1, text='Question', font=self.font_title, width=10).grid(row=0, column=3, sticky='wens')
        l2 = tk.Label(f1, text='Answer', font=self.font_title).grid(row=0, column=4, sticky='wens')

        e1 = tk.Entry(f1, textvariable=self.var1, font=self.font_write, state='readonly', width=15,
                      justify=tk.CENTER).grid(row=1, column=3, sticky='wens')
        e2 = tk.Entry(f1, font=self.font_write, textvariable=self.var2, width=5, justify=tk.CENTER)
        e2.grid(row=1, column=4, sticky='wens')
        e2.bind("<Return>", submit_)

        b1 = tk.Button(f1, text='Submit', font=self.font_button, command=submit, width=10).grid(row=0, column=5,
                                                                                                sticky='wens',
                                                                                                rowspan=2)
        b2 = tk.Button(f1, text='Start', font=self.font_button, command=start, width=6, height=1).grid(row=0, column=2,
                                                                                                       sticky='wens',
                                                                                                       rowspan=2)
        l3 = tk.Label(f1, text='Set Times', font=self.font_title, width=10).grid(row=0, column=0, sticky='wens')
        e3 = tk.Entry(f1, font=self.font_times, textvariable=self.var3, width=6, justify=tk.CENTER).grid(row=1,
                                                                                                         column=0,
                                                                                                         sticky='wens')
        l4 = tk.Label(f1, text='Set Limits', font=self.font_title, width=10).grid(row=0, column=1, sticky='wens')
        e4 = tk.Entry(f1, font=self.font_times, textvariable=self.var4, width=6, justify=tk.CENTER).grid(row=1,
                                                                                                         column=1,
                                                                                                         sticky='wens')

        f1.grid(row=0, column=0, sticky='wens')

        # 填充滚动条
        f2 = tk.Frame(root)

        self.t1 = tk.Text(f2, font=self.font_text)

        # Text颜色设置
        self.t1.tag_config('red', foreground='red', backgroun='yellow')
        self.t1.tag_config('black', foreground='black')
        self.t1.tag_config('big_black', foreground='black', font=self.font_response)
        self.t1.tag_config('big_red', foreground='red', font=self.font_response)
        self.t1.tag_config('big_green', foreground='green', font=self.font_response)
        self.t1.tag_config('write_black', foreground='black', justify=tk.CENTER)

        self.t1.grid(row=3, column=0, columnspan=3, sticky='wens')
        scroll = tk.Scrollbar(f2)
        scroll.grid(row=3, column=3, sticky='wens')
        self.t1.config(yscrollcommand=scroll.set)
        scroll.config(command=self.t1.yview)
        f2.grid(row=1, column=0, sticky='wens')

        # 增加使用说明
        write('本作品用于小朋友【学习加减法】刷题所用，愿每一个小朋友都有做不完的作业（坏笑）', "end", 'red')
        write('\n使用说明：\n'
              '1. Set Times：\t\t输入题目数量\n'
              '2. Set Limits：\t\t输入加减运算上限（20以内的加减法则输入20）\n'
              '3. Start：\t\t点击开始，生成题目！\n'
              '4. Submit：\t\t点击提交并进行下一题（快捷键：回车）\n'
              '作者: 李英俊小朋友，若有任何疑问或发现任何bug，请联系：litian_cup@163.com\n'
              '免责声明：本软件由作者原创，仅供个人用于学习、研究，未经许可不可用于任何商业用途\n'
              '                若有任何疑问请联系作者，版权归原作者所有，侵权必究！', "end", 'black')

        root.mainloop()
        try:
            os.remove(temp_name)
        except:
            print('并没有文件可以删除哦！')


if __name__ == '__main__':
    x = TkTest()
