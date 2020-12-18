#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: MyMatplotlib.py
@time: 2020/5/3 9:31
@desc: 绘图工具
        [plt字体和负号处理](https://blog.csdn.net/u010916338/article/details/96430916?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1)
        [plt.ticks字体大小设置参考](https://www.delftstack.com/zh/howto/matplotlib/how-to-set-tick-labels-font-size-in-matplotlib/)
        [sns.heatmap参数详解1](https://blog.csdn.net/m0_38103546/article/details/79935671)
        [sns.heatmap参数详解2](https://www.pianshen.com/article/975899613/)
        [sns.heatmap刻度异常问题(旋转解决)](https://blog.csdn.net/chenhaouestc/article/details/79132602)
        [sns.pairplot参数详解](https://www.jianshu.com/|p/6e18d21a4cad)
        [sns.pairplot参数详解2](https://www.jianshu.com/p/c50cb4f1029f)
        [sns.pairplot控制图例位置](https://stackoverflow.com/questions/37815774/seaborn-pairplot-legend-how-to-control-position)
        [pl.legend图例参数详解](https://blog.csdn.net/helunqu2017/article/details/78641290?utm_source=blogxgwz6)
"""

import matplotlib.pyplot as plt
import seaborn as sns; sns.set(style="ticks", color_codes=True)
import os
from TimeTool import TimeTool


class MyMatplotlib:
    def __init__(self, save_path):
        # 新建时，需要传入保存路径
        self.save_path = save_path
        # 默认图片大小
        self.figsize = (16, 9)
        # 热力图大小
        self.figsize_heatmap = (12, 9)
        # 默认图片分辨率
        self.dpi = 150

        # 坐标刻度字体和标签字体
        # 1. word一行放三张
        self.font_ticks3, self.font_labels3 = 40, 46
        # 2. word一行放两张
        self.font_ticks2, self.font_labels2 = 30, 36
        # 3. word一行放一张
        self.font_ticks1, self.font_labels1 = 20, 26
        # 4. 热力图
        self.font_ticks_heatmap = 13
        self.labelsize_heatmap = 13
        # 5. 图例字体大小
        self.legend_size = 'large'

        # 设置字体和负号显示正常
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

    def plot_barh(self, ):
        pass

    def plot_plot(self, theme, X_list, y_list, X_label, y_label, best_X=None, is_save=False):
        """
        plt.plot绘图
        :param best_X: 最佳值
        """
        fig = plt.figure(figsize=self.figsize, dpi=self.dpi)
        plt.plot(X_list, y_list, '-o')
        plt.xlabel(X_label, fontsize=self.font_labels1)
        plt.ylabel(y_label, fontsize=self.font_labels1)
        plt.xticks(fontsize=self.font_ticks1)
        plt.yticks(fontsize=self.font_ticks1)
        if is_save:
            save_path = self.save_path + theme + '.jpg'
            plt.tight_layout()
            plt.savefig(save_path)

    def get_ax(self):
        f, ax = plt.subplots(figsize=self.figsize_heatmap, dpi=self.dpi)
        return f, ax

    def get_fg(self):
        fig = plt.figure(figsize=self.figsize_heatmap, dpi=self.dpi)
        return fig

    def savefig(self, figname=None):
        if figname is None:
            figname = TimeTool().getCurrentTime() + '.jpg'
        plt.tight_layout()
        f = os.path.join(self.save_path, figname)
        plt.savefig(f, bbox_inches='tight')
        return f

    def plot_heatmap(self, mat, annot=False, cmap=None, change_ticks_fontsize=False, rotation_ticks=False, vmax=None, vmin=None, center=None):
        # 获取fig和ax
        f, ax = self.get_ax()
        sns.heatmap(mat, square=True, cmap=None, center=center, vmax=vmax, vmin=vmin, ax=ax, robust=True, linewidths=.5, annot=annot, annot_kws={'size': self.labelsize_heatmap})

        if change_ticks_fontsize:
            # 设置ticks的刻度字体大小
            plt.xticks(fontsize=self.font_ticks_heatmap)
            plt.yticks(fontsize=self.font_ticks_heatmap)

            # 设置colorbar的刻度字体大小
            cax = plt.gcf().axes[-1]
            cax.tick_params(labelsize=self.labelsize_heatmap)

            # 设置colorbar的label文本和字体大小
            # cbar = ax.collections[0].colorbar
            # cbar.set_label(r'$NMI$', fontdict = font)

        # 如果ticks太长，可以考虑旋转，增加X轴和y轴ticks的长度
        if rotation_ticks:
            label_y = ax.get_yticklabels()
            plt.setp(label_y, rotation=360)
            label_x = ax.get_xticklabels()
            plt.setp(label_x, rotation=90)

        return self.savefig()

    def plot_pair(self, mat, hue, reg=False, vars=None):
        """
        绘制矩阵图
        :param mat: X, y
        :param hue: 是否分类显示
        :param reg: 是否线性
        :param keep_legend: 是否保留图例
        :param vars: 是否指定属性
        :return:
        """

        params = {}
        column_names = list(mat.columns)

        params['data'] = mat
        # params['aspect'] = 12/9

        if hue:
            params['hue'] = column_names[-1]
        if reg:
            params['kind'] = 'reg'
        if vars is not None:
            params['vars'] = vars

        g = sns.pairplot(**params)

        # 有hue并不要legend，才有不显示图例的可能
        if hue:
            g._legend.remove()
        # plt.legend(fontsize=self.legend_size, shadow=False, loc='upper', ncol=3)

        return self.savefig()
