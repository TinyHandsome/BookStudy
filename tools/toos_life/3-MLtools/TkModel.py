#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: TkModel.py
@time: 2020/5/6 21:50
@desc: 可视化专用
        [各个组件介绍](https://blog.csdn.net/ahilll/article/details/81531587)
        [布局详解](https://www.cnblogs.com/jerryspace/p/9836034.html)
            我的理解：pack中
                expand是该组件是否扩充额外的空间，但是内容不一定扩充，只说明了组件的占位
                fill是该组件是否扩充占位的空间

        [通过像素为单位来指定布局大小](https://blog.csdn.net/qq_41556318/article/details/85080617)
            1. 首先要设置pack_propagate(0)，来保证基础frame不变动
            2. 设置fram中的每个组件，label也好，button也好，固定在一个frame中，组件不用设置大小，frame要设置像素
               同时设置组件为pack(fill="both", expand=True)
               其中：
                    expand指定是否填充父组件的额外空间
                    fill指定填充 pack分配的空间
            3. 以14号字体的配置来看，4个字是100合适，2个字是70合适
               那么1个字是15，宽度计算公式为40 + len * 15

        [配色方案](https://www.cnblogs.com/kongzhagen/p/6154826.html)
        [relief样式参考](https://cloud.tencent.com/developer/ask/184643)

        [Text详解](https://blog.csdn.net/qq_41556318/article/details/85112829)
            \n不能带颜色！
        [Text 插入图片详解](https://blog.csdn.net/FunkyPants/article/details/78163021?utm_source=blogxgwz1)
        [图片PIL.resize保持信息缩放详解](https://blog.csdn.net/sunshinefcx/article/details/85623227)
            只能插入gif，其他格式需要用ImageTk方法进行转换

        [路径分解，文件名全名，文件名，后缀](https://blog.csdn.net/lilongsy/article/details/99853925)

        [如何高效的判断一个字符是中文还是英文](https://www.jianshu.com/p/4d2335ea6982)

        报错编码：
            code_1：创建线程出错
            code_2：读取文件类型出错
            code_3：pandas读取文件出错
            code_4：未传入数据就点击了功能区
            code_5：未选择保存路径就点击了功能区

"""
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory
import os
import re
import threading
import pandas as pd
from PIL import Image, ImageTk

from PreAnalysis import MyPCA, DataTransfer
from MLTools import MLTools
from PreAnalysis import PreAnalysis
from TimeTool import TimeTool


class TkModel():

    def __init__(self):
        """字体设置"""
        # label标题字体
        self.font_title = ("Microsoft YaHei", 14)
        # button字体
        self.button_font = ("Microsoft YaHei", 14)
        # ratio字体
        self.ratio_font = ("Microsoft YaHei", 14)

        # 设置默认字体
        self.default_fg = 'black'
        self.default_bg = 'white'
        self.default_padx = 5
        self.default_pady = 5
        self.default_font = ("Microsoft YaHei", 14)

        """Root 元素"""
        self.root = tk.Tk()
        self.root.title('机器学习工具v1.0【作者：李英俊小朋友】')
        self.root_width = 1200
        self.root_height = 765

        # 计算居中的位置，默认分辨率为1920*1080
        left_pad = int(1920 / 2 - self.root_width / 2)
        up_pad = int(1080 / 2 - self.root_height / 2)

        self.root.geometry(
            str(self.root_width) + "x" + str(self.root_height) + "+" + str(left_pad) + "+" + str(up_pad))
        self.root.resizable(width=False, height=False)

        """Frame 颜色和大小"""
        f1_color = None
        f2_color = 'white'
        ratio = 7 / (5 + 7)
        self.f1_height = self.root_height
        self.f1_width = int(ratio * self.root_width)
        self.f2_height = self.root_height
        self.f2_width = int((1 - ratio) * self.root_width)
        # 功能区
        self.f_func = tk.Frame(self.root, height=self.f1_height, width=self.f1_width, bg=f1_color)
        # 输出区
        self.f_print = tk.Frame(self.root, height=self.f2_height, width=self.f2_width, bg=f2_color)

        """Text 功能区默认放置信息，以及滚动条"""
        # state:
        #   1. 默认情况下 Text 组件响应键盘和鼠标事件（"normal"）
        #   2. 如果将该选项的值设置为 "disabled"，那么上述响应就不会发生，并且你无法修改里边的内容
        # wrap:
        #   1. 设置当一行文本的长度超过 width 选项设置的宽度时，是否自动换行
        #   2. 该选项的值可以是："none"（不自动换行），"char"（按字符自动换行）和 "word"（按单词自动换行）
        # takefocus:
        #   1. 指定使用 Tab 键可以将焦点移动到 Text 组件中
        #   2. 默认是开启的，可以将该选项设置为 False 避免焦点在此 Text 组件中
        # spacing2:
        #   1. 指定 Text 组件的文本块中自动换行的各行间的空白间隔
        #   2. 注意：换行符（'\n'）不算
        #   3. 默认值是 0
        # font:
        #   1. 设置 Text 组件中文本的默认字体
        #   2. 注意：通过使用 Tags 可以使 Text 组件中的文本支持多种字体显示
        self.t_print = tk.Text(self.f_print, wrap="char", takefocus=False, spacing2=1,
                               font=('Microsoft YaHei', 14))

        # 设置滚动条
        self.scroll = tk.Scrollbar()
        # 放到窗口的右侧, 填充Y竖直方向
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # 两个控件关联
        self.scroll.config(command=self.t_print.yview)
        self.t_print.config(yscrollcommand=self.scroll.set)
        self.t_print.pack(fill=tk.BOTH, expand=tk.YES)

        """相关全局变量的数据"""
        # 数据路径
        self.file_path = tk.StringVar()
        # 保存路径，默认为数据路径对应的目录
        self.save_path = tk.StringVar()
        # 缺失值处理方法选择
        self.missing_data = tk.IntVar()
        # 数据标准化选择
        self.data_stand = tk.IntVar()
        # pca降维选择
        self.pca_select = tk.IntVar()
        # 多选框的取值，是一维数组，需要初始化
        self.check_values = None

        # 数据集的column_names
        self.column_names = None
        # 数据本身，包含了列名
        self.data = None
        # X：监督学习去掉y，非监督学习X，为DataFrame，有列名
        self.X = None
        # y：同上，y为list，无列名，默认为label
        self.y = None
        # 显示列名内容
        self.column_show = tk.StringVar()
        # 根据是否有 label|Label 分辨是否是监督学习
        self.has_label = None

        """调用外界类的应用，单例模式"""
        # 使用什么功能，1：数据预处理，2：分类
        self.func_state = 0
        # 使用该功能的什么方法
        self.which_f = 0

        # 工具类的引用，在使用的时候创建，只创建一次
        self.tool = None

        """工具区的变量"""
        # 全局变量
        self.path_dict = {}
        self.path_list = []
        # 文件名
        root_name = '点我点我我是结果'

        def path_list_generate(pa_path, pa_path_in):
            # 初始化list和dict
            for p in pa_path_in:
                pp = root_name + '/' + pa_path + '/' + p
                self.path_list.append(pp)

        # 数据预处理文件名
        pa_path = '数据预处理'
        pa_path_in = ['特征矩阵图', '相关性分析', '缺失值分析', '异常值分析']
        path_list_generate(pa_path, pa_path_in)

        # 降维
        pa_path = '降维'
        pa_path_in = ['主成分分析']
        path_list_generate(pa_path, pa_path_in)

        # 数据转换
        pa_path = '数据转换'
        pa_path_in = ['最大最小值标准化']
        path_list_generate(pa_path, pa_path_in)

        # 分类
        pa_path = '分类'
        pa_path_in = ['全部实现']
        path_list_generate(pa_path, pa_path_in)

        # 机器学习建模文件名

        """一些辅助变量"""
        # 保存上一个tag，在下一个tag生成时删除上一次生成的多个tag
        self.old_tags = []
        # 保存上一个时间记录，同时的操作不显示时间
        self.old_time = None
        # 保存临时图片显示
        self.photos = []

        # 统计数据分割的次数和路径建立的次数
        self.xy_sep_time = 0
        self.path_build_time = 0

        # 左右预留间隔大小
        self.lp = None

    def init_checkValues(self, check_names):
        """根据选框名初始化全局变量"""
        self.check_values = []
        for c in check_names:
            temp = tk.IntVar()
            self.check_values.append(temp)

    def finish(self):
        """布局root和frame"""
        # 禁止frame自动调整
        self.f_func.pack_propagate(0)
        self.f_print.pack_propagate(0)

        self.f_func.pack(side=tk.LEFT, fill='y', expand=True, pady=0)
        self.f_print.pack(side=tk.RIGHT, fill='y', expand=True)
        self.root.mainloop()

    def data_seperate(self):
        """
        用于分离data中的X和y
        可以重复更新X，y
        :return:
        """
        if self.data is None:
            self.info('-x->【警告】你还没有传入数据！错误代码：【code_4】', focus_words='auto')
        else:
            self.y = self.data[self.column_names[-1]].tolist()
            self.X = self.data.drop(columns=self.column_names[-1])

    def build_path(self):
        """根据保存路径建立文件系统"""
        if self.path_build_time == 0:
            sp = self.save_path.get()
            if not os.path.exists(sp):
                self.info('-x->【警告】你还没有选择保存路径！错误代码：【code_5】', focus_words='auto')
            else:
                # 生成目录 生成字典
                filePathList = []
                for i in self.path_list:
                    name = i.split('/')[-1]
                    abs_path = os.path.join(sp, i)
                    filePathList.append(abs_path)
                    self.path_dict[name] = abs_path

                # 检查路径是否都存在，存在就算了，不存在就创建
                for p in filePathList:
                    if not os.path.exists(p):
                        os.makedirs(p)

                self.path_build_time += 1

    def check_data_path(self):
        """检查数据问题，路径问题，等"""
        self.data_seperate()
        self.build_path()

    def show_pic(self, path):
        """插入图片到text中"""

        def resize_img(image):
            # 因为滚动条有宽度，默认16像素，所以这里要减去一部分
            target_width = int(self.f2_width - 20)
            width, height = image.size
            # h / w = h2 / w2
            h2 = int(height / width * target_width)
            new_image = image.resize((target_width, h2), Image.ANTIALIAS)
            return new_image

        image = Image.open(path)
        self.photos.append(ImageTk.PhotoImage(resize_img(image)))
        self.t_print.image_create('end', image=self.photos[-1])

        # 两个图片之间留白
        self.info(' ', False, print_time=False)
        self.t_print.see(tk.END)

    def info(self, inf, is_update=True, focus_words=None, fg_color=None, bg_color=None, font_type=None,
             font_size=None, print_time=True):
        """
        写入右边信息，报错啊，运行到哪里了呀，等等
        支持多个重点内容，但不能重复，重点内容的传入为list
        :param inf: 写入的信息
        :param is_update: 是否清空原来的信息
        :param focus_words: 需要强调的内容，最好用【】表示，类型是list，一个值也要用list
        :param fg_color:
        :param bg_color:
        :param font_type:
        :param font_size:
        :param print_time: 是否输出时间，默认是输出的
        :return:
        """
        # 如果添加新的内容需要删除之前的内容，并删除之前内容保留下来的tags
        if is_update:
            self.t_print.delete('1.0', 'end')

            # tags用完之后删除，清空内存
            if self.old_tags:
                for tag in self.old_tags:
                    self.t_print.tag_delete(tag)
                # 删完后充值old_tags
                self.old_tags = []

        if focus_words == 'auto':
            # 自动识别带【】的内容，并将其转换为list
            fws = []

            # 如果inf中带-x->内容，也标红
            if '-x->' in inf:
                fws.append('-x->')

            kaiguan = False
            temp_str = ''
            for word in inf:
                if word == '【':
                    kaiguan = True
                if kaiguan:
                    temp_str += word
                if word == '】':
                    kaiguan = False
                    fws.append(temp_str)
                    temp_str = ''
            focus_words = fws

        params = {
            'fg_color': self.default_fg,
            'bg_color': self.default_bg,
            'font_type': self.default_font[0],
            'font_size': self.default_font[1]
        }

        if fg_color is not None:
            params['fg_color'] = fg_color
        if bg_color is not None:
            params['bg_color'] = bg_color
        if font_type is not None:
            params['font_type'] = font_type
        if font_size is not None:
            params['font_size'] = font_size

        # 获取随机tag名
        tag_name = TimeTool().getct()
        self.t_print.tag_config(tag_name, background=params['bg_color'], foreground=params['fg_color'],
                                font=(params['font_type'], params['font_size']))
        # 保存该tag名
        self.old_tags.append(tag_name)

        # 设置加强字体
        self.t_print.tag_config("tag_temp_imp", background=params['bg_color'], foreground='red',
                                font=(params['font_type'], params['font_size']))

        # 设置时间tag
        self.t_print.tag_config(
            "tag_time", background=self.default_bg, foreground='LightGrey', font=self.default_font,
            # justify=tk.CENTER
        )
        tag_info = TimeTool().getTimeTag()
        if tag_info != self.old_time and print_time:
            self.t_print.insert("end", tag_info, "tag_time")
            self.t_print.insert("end", '\n')
            self.old_time = tag_info

        """这里开始正式写入内容"""
        # 若没有需要重点标明的内容
        if focus_words is None or len(focus_words) == 0:
            self.t_print.insert("end", inf, tag_name)
            self.t_print.insert("end", '\n')
        else:
            # 正则表达式分割重点内容，很明显，非重点语句的数量比重点内容多1
            regx_focus = "|".join(focus_words)
            words_list = re.split(regx_focus, inf)
            # 用空值补充重点内容
            fw = focus_words + ['']

            # 开始写出内容，重点内容默认字体大小不变，但颜色为红色
            for inf1, inf_imp in zip(words_list, fw):
                self.t_print.insert("end", inf1, tag_name)
                self.t_print.insert("end", inf_imp, "tag_temp_imp")
            self.t_print.insert("end", '\n')

        # text显示最新内容
        self.t_print.see(tk.END)

    def temp_frame(self, base_frame, width, height, bd=0):
        f = tk.Frame(base_frame, height=height, width=width, bd=bd)
        f.pack_propagate(0)
        return f

    def count_str(self, inf):
        ignore = ['[', ']']
        for i in ignore:
            inf = inf.replace(i, '')
        length = 0
        for x in inf:
            judge_chinese = u'\u4e00' <= x <= u'\u9fa5'
            if not judge_chinese:
                length += 0.65
            else:
                length += 1
        return length

    def count_info_width(self, inf):
        """计算字符串长度，中文为1，英文为0.5, 4->100, 2->60"""
        length = self.count_str(inf)
        width = 18 * length + 28
        return width

    def getLabel(self, frame, label_info, row, column, fg='black', bg='gainsboro', width=None, height=40):
        if width is None:
            width = self.count_info_width(label_info)
        f = self.temp_frame(frame, width, height)
        l1 = tk.Label(f, text=label_info, font=self.font_title, fg=fg, bg=bg, relief='ridge', bd=1)
        l1.pack(fill="both", expand=True)
        f.grid(row=row, column=column, sticky='wesn')
        return l1, width

    def getEntry(self, frame, var, row, column, width=200, height=40, entry_info=None, entry_color=None):
        f = tk.Frame(frame, height=height, width=width)
        f.pack_propagate(0)
        e = tk.Entry(f, textvariable=var, font=self.font_title)
        e.insert(tk.END, ' ' + entry_info)
        e.configure(fg=entry_color)
        e.pack(fill="both", expand=True)
        f.grid(row=row, column=column, sticky='wesn')
        return e, width

    def getButton(self, frame, button_info, command_func, row, column, width=None, height=40, bg=None, rowspan=None):
        if width is None:
            width = self.count_info_width(button_info)
        f = tk.Frame(frame, height=height, width=width)
        f.pack_propagate(0)
        b = tk.Button(f, text=button_info, font=self.button_font, command=command_func, bg=bg)
        b.pack(fill="both", expand=True)
        f.grid(row=row, column=column, sticky='wesn', rowspan=rowspan)
        return b, width

    def getRatio(self, frame, ratio_info, value, row, column, variable, width=None, height=40, bg='lightgray',
                 activeforeground=None, rowspan=None):
        """

        :param frame:
        :param ratio_info:
        :param value: 选了之后的取值
        :param row:
        :param column:
        :param variable: value存放的变量，值为value
        :param width:
        :param height:
        :param bg:
        :param activeforeground:
        :param rowspan:
        :return:
        """

        def check_command():
            """选择按钮后，显示选择的信息"""
            self.info('-->【' + ratio_info + '】已被选择...', False, focus_words='auto')

        if width is None:
            width = self.count_info_width(ratio_info)
        f = tk.Frame(frame, height=height, width=width)
        f.pack_propagate(0)
        r = tk.Radiobutton(f, text=ratio_info, font=self.ratio_font, variable=variable, value=value, bg=bg,
                           activeforeground=activeforeground, command=check_command)
        r.pack(fill="both", expand=True)
        f.grid(row=row, column=column, sticky='wesn', rowspan=rowspan)
        return r, width

    def getCheck(self, frame, check_info, row, column, c, width=None, height=40, bg='lightgray',
                 activeforeground=None, rowspan=None):

        variable = self.check_values[c]

        def check_command():
            """选择按钮后，显示选择的信息"""
            if variable.get() == 1:
                self.info('-->【' + check_info + '】已被选择...', False, focus_words='auto')
            else:
                self.info('-->【' + check_info + '】已被取消...', False, focus_words='auto')

        if width is None:
            width = self.count_info_width(check_info)
        f = tk.Frame(frame, height=height, width=width)
        f.pack_propagate(0)
        r = tk.Checkbutton(f, text=check_info, font=self.ratio_font, variable=variable, bg=bg,
                           activeforeground=activeforeground, command=check_command, onvalue=1, offvalue=0)
        r.pack(fill="both", expand=True)
        f.grid(row=row, column=column, sticky='wesn', rowspan=rowspan)
        return r, width

    def decorate_frame(self, father_frame):
        separator = tk.Frame(father_frame, height=2, width=500, bd=1, relief="sunken")
        separator.pack(padx=5, pady=5)

    def base_frame(self, text, is_label=True, frame=None, bg=None):
        """一个功能的基础Frame"""
        padx = self.default_padx
        pady = self.default_pady
        leave_xp = 2 * padx
        h, w = 0, self.f1_width
        # 细节组件Frame的边框宽度
        frame_boderWidth = 2
        frame_relief = None
        frame_bg = bg
        font = self.default_font
        labelanchor = "n"

        if frame is None:
            frame = self.f_func

        if is_label:
            f1 = tk.LabelFrame(frame, text=text, height=h, width=w, borderwidth=frame_boderWidth, relief=frame_relief,
                               bg=frame_bg, padx=padx, pady=pady, font=font, labelanchor=labelanchor)
        else:
            f1 = tk.Frame(frame, height=h, width=w, borderwidth=frame_boderWidth, relief=frame_relief, bg=frame_bg,
                          padx=0, pady=0)
        return f1, leave_xp * 3.5

    def baseFrame_end_pack(self, f1, padx=8):
        f1.pack(expand=False, fill='x', padx=padx, pady=0)

    def baseFrame_end_grid(self, f1, row, column, rowspan=1):
        f1.grid(row=row, column=column, rowspan=rowspan, sticky='wesn')

    def set_pathSelect(self, var: tk.StringVar or None, is_file: int, recall_info: str, label_info: str,
                       entry_info: str, base_frame=None, start_row=0, button_info: str = '选择',
                       auto_generateSavePath: tk.StringVar = None):
        """
        路径选择模块：用于生成标题 + 输入框 + 按钮
        :param var: 需要填充的StringVar变量
        :param is_file: 获取文件，还是路径，或者其他
        :param recall_info: 点击按钮实现后，输出的信息
        :param label_info: label的文字
        :param entry_info: entry的默认提示文字，颜色默认为灰色
        :param button_info: button的默认文字
        :param auto_generateSavePath: 是否自动关联某个entry的StringVar，None：不关联；否则，指定需要关联的StringVar，获取文件路径
        :return: 标题Label，输入框Entry，按钮Button
        """

        def select_file():
            # 获取路径的信息不再是灰色，而是黑色
            e1.configure(fg='black')

            if is_file == 1:
                # 获取文件路径
                var.set(askopenfilename())

                if auto_generateSavePath is not None:
                    # 是否自动填充默认保存路径
                    data_path = os.path.dirname(var.get())
                    auto_generateSavePath.set(data_path)

                self.info('---> ' + recall_info, fg_color='green')
                # 处理路径，检测是否合法，自动识别列名，获取数据
                self.thread_it(self.deal_data, [])

            elif is_file == 2:
                # 获取文件夹路径
                var.set(askdirectory())
                self.info('---> ' + recall_info, fg_color='green')
            else:
                # 不获取什么，但是点击了会有提示信息
                self.info('---> ' + recall_info, focus_words='auto', fg_color='black')

        if base_frame is None:
            f1, self.lp = self.base_frame('数据获取和检查')
        else:
            f1 = base_frame

        l1, l_w = self.getLabel(f1, label_info, start_row, 0)
        b1, b_w = self.getButton(f1, button_info, select_file, start_row, 2)
        e_w = self.f1_width - l_w - b_w - self.lp / 3.5 * 3.35
        e1, _ = self.getEntry(f1, var, start_row, 1, entry_info=entry_info, entry_color='gray', width=e_w)

        return f1, start_row + 1

    def component_cal(self, base_frame, label_name, labels, func0, start_row, rowspan, right_button=False):
        """
        获取生成组件集的基本配置，计算组件的每个长度
        :param base_frame: 基础组件，有的话是为了集成，None的话则是新建
        :param label_name: 集成的总名字
        :param labels: 所有组件的label
        :param right_button: True则固定右边第一个button的长度跟它的字符长度有关
        :return: 右边的集成基础frame，base_frame，右边每个组件的宽度，左边的宽度
        """

        if base_frame is None:
            f1, self.lp = self.base_frame(label_name)
        else:
            f1 = base_frame

        # 组件总长度
        sum_len = self.f1_width
        # 左边一概以120的宽度计算
        b0_w = 100
        rest_len = sum_len - b0_w - self.lp
        if not right_button:
            # 计算其他的长度
            other_labels = labels[1:]
            other_words = [self.count_str(i) for i in other_labels]
            other_len = [int(i / sum(other_words) * rest_len) for i in other_words]
            # 为了防止int导致最后加起来不是总长，因此设最后一个为总长减其他的
            len_list = other_len[:-1] + [int(rest_len - sum(other_len[:-1]))]
        else:
            lb_width = self.count_info_width(labels[1])
            rest_len2 = rest_len - lb_width
            other_labels = labels[2:]
            other_words = [self.count_str(i) for i in other_labels]
            other_len = [int(i / sum(other_words) * rest_len2) for i in other_words]
            len_list = [lb_width] + other_len[:-1] + [int(rest_len2 - sum(other_len[:-1]))]

        # 内层，把右边的做在一起
        f_2, _ = self.base_frame(None, False, f1)

        # 左边的不用集成，自己就是一个frame，直接放置
        if labels[0] is not None:
            b0, _ = self.getButton(f1, labels[0], func0, start_row, 0, bg='gainsboro', width=b0_w,
                                   rowspan=rowspan)

        return f_2, f1, len_list, b0_w

    def set_buttons(self, labels: list, all_func: list, label_name: str, base_frame=None, start_row=0, rowspan=1):
        """
        功能按钮模块：用于生成一行多列的button
            1：nb模式，多个button
        :return:
        """
        f_2, f1, len_list, b0_w = self.component_cal(base_frame, label_name, labels, all_func[0], start_row, rowspan)

        col = 0
        for head_name, func, w in zip(labels[1:], all_func[1:], len_list):
            bb, _ = self.getButton(f_2, head_name, func, start_row, col, width=w)
            col += 1

        self.baseFrame_end_grid(f_2, start_row, 1, rowspan=1)

        return f1, start_row + 1

    def set_ratios(self, labels: list, all_func: list, label_name: str, variable, base_frame=None, start_row=0,
                   rowspan=1):
        """
            2：bbr模式，button+button+多个ratio
        """
        f_2, f1, len_list, b0_w = self.component_cal(base_frame, label_name, labels, all_func[0], start_row, rowspan,
                                                     right_button=True)
        rest_funcs = all_func[1:]
        rest_labels = labels[1:]

        b1, _ = self.getButton(f_2, rest_labels[0], rest_funcs[0], start_row, 0, width=len_list[0])

        # 绘制右边第二个组件ratio的集合
        col = 1
        for head_name, func, w in zip(rest_labels[1:], rest_funcs[1:], len_list[1:]):
            bb, _ = self.getRatio(f_2, head_name, func, start_row, col, variable, width=w)
            col += 1

        self.baseFrame_end_grid(f_2, start_row, 1, rowspan=1)

        return f1, start_row + 1

    def set_check(self, labels: list, all_func: list, label_name: str, base_frame=None, start_row=0,
                  rowspan=1):
        """
        3：bbo模式，button+button+多个check
        :param labels:
        :param all_func:
        :param label_name:
        :param base_frame:
        :param start_row:
        :param rowspan:
        :return:
        """
        f_2, f1, len_list, b0_w = self.component_cal(base_frame, label_name, labels, all_func[0], start_row, rowspan,
                                                     right_button=True)
        rest_funcs = all_func[1:]
        rest_labels = labels[1:]

        b1, _ = self.getButton(f_2, rest_labels[0], rest_funcs[0], start_row, 0, width=len_list[0])

        # 绘制右边第二个组件ratio的集合
        col = 1
        for head_name, c, w in zip(rest_labels[1:], list(range(len(rest_funcs[1:]))), len_list[1:]):
            bb, _ = self.getCheck(f_2, head_name, start_row, col, c=c, width=w)
            col += 1

        self.baseFrame_end_grid(f_2, start_row, 1, rowspan=1)

        return f1, start_row + 1

    def run_func(self):
        """数据处理工具"""

        def inner_info(n1, n2):
            if n1 is not None and n2 is not None:
                self.info('--> 2. 正在运行【' + n1 + '】功能中的【' + n2 + '】方法...', False, focus_words='auto')

            # 工具类的数据只赋值一次
            if self.tool.X is None:
                self.tool.set_X(self.X)
            if self.tool.y is None:
                self.tool.set_y(self.y)

            # 在运行工具的时候，需要设置工具类的保存路径，这里不能只赋值一次，因为每个方法的保存路径不同
            self.tool.set_savepath(self.path_dict[n2])

            # 设置好参数后开始运行
            self.tool.aim(self.which_f)

            # 检查该方法是否有返回的信息，若有的化，则输出到屏幕
            if self.tool.return_inf is not None:
                self.info(self.tool.return_inf, False, focus_words='auto', fg_color='black')

            # 运行结束后绘图
            if self.tool.fig_path is not None:
                self.show_pic(self.tool.fig_path)

        def extra_inner_info(n, name):
            self.info('--> 2.' + str(n) + ' 由于您输入的数据自动检测到是【分类】问题，因此自动生成了【' + name + '】的图...', False, focus_words='auto')
            self.tool.aim(self.which_f)
            if self.tool.return_inf is not None:
                self.info(self.tool.return_inf, False, focus_words='auto', fg_color='black')
            if self.tool.fig_path is not None:
                self.show_pic(self.tool.fig_path)

        def inner_run():
            # 检查数据和路径
            self.info('--> 1. 正在检查数据和路径是否合法...', False)
            self.check_data_path()

            if self.func_state == 1:
                # 选择了功能区中的数据预处理
                n1 = '数据预处理'
                self.tool = PreAnalysis(None)
                if self.which_f == 1:
                    # 使用特征矩阵图
                    n2 = '特征矩阵图'
                    inner_info(n1, n2)

                    # 检查是否是分类，分类多一个图
                    if self.has_label:
                        self.which_f = 1.1
                        extra_inner_info(1, '按类标记')
                        self.which_f = 1.2
                        extra_inner_info(2, '分类线性回归')

                elif self.which_f == 2:
                    # 使用相关性分析
                    n2 = '相关性分析'
                    inner_info(n1, n2)

                elif self.which_f == 3:
                    # 使用缺失值分析
                    n2 = '缺失值分析'
                    inner_info(n1, n2)

            elif self.func_state == 2:
                # 选择了功能区的标准化
                n1 = '数据转换'
                self.tool = DataTransfer(None)
                if self.which_f == 1:
                    n2 = '最大最小值标准化'
                    inner_info(n1, n2)

            elif self.func_state == 3:
                # 选择了功能区的降维
                n1 = '降维'
                if self.which_f == 1.1:
                    n2 = '主成分分析'
                    self.tool = MyPCA(None)
                    inner_info(n1, n2)

            elif self.func_state == 4:
                # 选择了功能区的分类
                n1 = '分类'
                if self.which_f == 0:
                    n2 = '全部实现'
                    self.tool = MLTools(None)
                    inner_info(n1, n2)

            self.info('--> 3. 计算完毕...', False)

        self.thread_it(inner_run, [])

    def set_state(self, state, which):
        """调用什么功能的什么方法"""
        self.func_state = state
        self.which_f = which
        self.run_func()

    def thread_it(self, func, args):
        """创建多线程任务"""
        try:
            t = threading.Thread(target=func, args=args)
            t.start()
            # t.join()

        except Exception as e:
            self.info("-x->【错误】创建线程报错，错误代码：【code_1】", False, focus_words='auto')

    def test(self):
        """测试用例"""
        # self.set_label('【数据获取】')
        f1, new_row = self.set_pathSelect(self.file_path, 1, '写入数据成功！（默认保存路径获取！）', '数据路径',
                                          '点击选择文件', auto_generateSavePath=self.save_path)
        f1, new_row = self.set_pathSelect(self.save_path, 2, '写入保存路径成功！', '保存路径', '点击选择保存文件夹',
                                          base_frame=f1, start_row=new_row)
        # 文件类型介绍
        intro = ['根据不同的文件类型获取列名',
                 ' ' * 5 + '1. 以xls或xlsx为后缀的excel文件，默认第1行为列名，请保证第1列是列名【推荐】',
                 ' ' * 5 + '2. 其他后缀或无后缀的文件，会被认为是pikle保存的文件进行读取',
                 ' ' * 5 + '2.1 以字典dict保存的文件格式要求：{"column_names": 一维数组的列名[*, *], "data": 二维数组的数据[[*, *], [*, *]]}',
                 ' ' * 5 + '2.2 以列表list保存的文件格式为[[*, *], [*, *]]，不用加列名，列名最后以数字格式自动填充【不推荐】',
                 ' ' * 5 + '注意：上述数据中：需要包含标签列（监督学习），【标签列为最后一列，且列名为label】；非监督学习不能进行分类和回归！']
        self.set_pathSelect(self.column_show, 0, '\n'.join(intro), '数据列名', '点击查看了解文件处理方式', button_info='查看',
                            base_frame=f1, start_row=new_row)
        self.baseFrame_end_pack(f1)

        # self.set_label('【数据预处理】')
        name = '数据分析和预处理'
        labels = ['数据分析', '特征矩阵图', '相关性分析', '缺失值分析', '异常值分析']
        all_func = [None, lambda: self.set_state(1, 1), lambda: self.set_state(1, 2),
                    lambda: self.set_state(1, 3)] + list(range(len(labels) - 2))
        f1, new_row = self.set_buttons(labels, all_func, name)

        labels = ['数据清洗', '缺失值处理', '删除记录', '均值填充', '常数填充', '最近邻插补']
        all_func = [None] * 2 + list(range(len(labels) - 2))
        f1, new_row = self.set_ratios(labels, all_func, name, self.missing_data, base_frame=f1, start_row=new_row)

        labels = ['数据转换', '数据标准化', '离差标准化', '标准差标准化', '小数定标标准化']
        all_func = [None, lambda: self.set_state(2, 1)] + list(range(len(labels) - 2))
        f1, new_row = self.set_ratios(labels, all_func, name, self.data_stand, base_frame=f1, start_row=new_row)

        labels = ['数据降维', '主成分分析', 'PCA', 'IPCA', 'RPCA', 'KPCA']
        all_func = [None, lambda: self.set_state(3, 1.1)] + list(range(len(labels) - 2))
        f1, new_row = self.set_ratios(labels, all_func, name, self.pca_select, base_frame=f1, start_row=new_row,
                                      rowspan=4)

        labels = [None, '因子分析[FA]', '线性判别分析[LDA]', '局部线性嵌入[LLE]']
        all_func = [None] * len(labels)
        f1, new_row = self.set_buttons(labels, all_func, name, base_frame=f1, start_row=new_row)

        labels = [None, '等距特征映射[Isomap]', '多维标定[MDS]', 't-SNE']
        all_func = [None] * len(labels)
        self.set_buttons(labels, all_func, name, base_frame=f1, start_row=new_row)
        self.baseFrame_end_pack(f1)

        name = '机器学习：聚类'
        labels = ['常用聚类', 'KMeans', 'DBSCAN', 'OPTICS', '谱聚类[SC]']
        all_func = [None] * len(labels)
        f1, new_row = self.set_buttons(labels, all_func, name, rowspan=2)

        labels = [None, '均值漂移', 'BIRCH', 'GMM', '层次聚类[HC]']
        all_func = [None] * len(labels)
        self.set_buttons(labels, all_func, name, base_frame=f1, start_row=new_row)
        self.baseFrame_end_pack(f1)

        """创建分类学习"""
        name = '机器学习：分类'  # ' | 评价指标：f1_macro | 抽样方式：分层抽样'
        mt = MLTools('')
        model_names = mt.model_names
        check_names = ['简单建模', '分步调参', '网格调参']
        self.init_checkValues(check_names)

        labels = ['常用分类', '查看参数默认配置和说明'] + check_names
        all_func = [lambda: self.set_state(4, 0), None] + [None] * (len(labels) - 2)
        f1, new_row = self.set_check(labels, all_func, name, rowspan=len(model_names) + 1)

        start = 0
        labels = [None] + model_names[start: start + 4]
        all_func = [None] * len(labels)
        f1, new_row = self.set_buttons(labels, all_func, name, base_frame=f1, start_row=new_row)
        start += 4

        labels = [None] + model_names[start:]
        all_func = [None] * len(labels)
        self.set_buttons(labels, all_func, name, base_frame=f1, start_row=new_row)

        self.baseFrame_end_pack(f1)

        self.finish()

    def deal_data(self):
        """
        处理数据，将数据转为DataFrame
        与文件选择事件绑定
        使用多线程
        :return:
        """

        # 检查文件是否存在
        self.info('--> 1. 检测到您输入的路径为：', False)
        fp = self.file_path.get()
        self.info(fp, False, bg_color='yellow')
        if not os.path.exists(fp):
            self.info('-x->【警告】该文件路径不合法！', False, 'auto')
        else:
            file, ext = os.path.splitext(fp)
            if ext == '.xls' or ext == '.xlsx':
                self.info('检测到该文件为【' + ext + '】数据，是合法数据！', False, 'auto')
                self.info('--> 2. 正在进行分析...', False)
                # 开始读取文件
                try:
                    self.data = pd.read_excel(fp)
                    self.column_names = self.data.columns.tolist()
                    self.info('---> 读取文件成功！正在识别列名....', False, fg_color='green')
                    col_str = '| ' + ' | '.join(self.column_names) + ' |'
                    self.info(col_str, False, bg_color='yellow')
                    self.column_show.set(col_str)

                    # 检查是否有label，有label就是监督学习否则就是无监督
                    last_column = self.column_names[-1]
                    if last_column.lower() == 'label':
                        self.has_label = True
                    else:
                        self.has_label = False
                    aim = '监督' if self.has_label else '无监督'
                    self.info('根据输入的数据可知，目标为：【' + aim + '学习】...', False, 'auto')

                except:
                    self.info('-x->【错误】文件内容获取错误！错误代码：【code_3】')
            else:
                self.info('-x-> 检测到该文件为【非法数据】，暂不支持其他格式的数据，请重新选择！错误代码：【code_2】', False, 'auto')
                return


if __name__ == '__main__':
    t = TkModel()
    t.test()
