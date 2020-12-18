#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: PreAnalysis.py
@time: 2020/5/4 11:23
@desc: 对数据进行各种预分析，比如关联性分析等
        1. 数据分析，预处理
            [特征关联](https://blog.csdn.net/FrankieHello/article/details/81604806)
            [数据预处理流程](https://www.jianshu.com/p/2339b0005405)
            [数据预处理全过程](https://blog.csdn.net/Monk_donot_know/article/details/86479176?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase)

            [缺失值处理方法](https://baijiahao.baidu.com/s?id=1665989715432866346&wfr=spider&for=pc)
                检查缺失值的两种方式：缺失热图/相关图，缺失树状图

        2. 降维
            [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html?highlight=pca#sklearn.decomposition.PCA)
            [isinstance类型检测方法](https://www.runoob.com/python/python-func-isinstance.html)

            [常用降维方法](https://www.jianshu.com/p/ad2ac2bda87b)
            [PCA和FA的区别](https://blog.csdn.net/yujianmin1990/article/details/49247307)

        3. 数据转换

        4. 其他
            [pandas.insert, pop](https://blog.csdn.net/yj1556492839/article/details/79807241?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase)

"""
import os
import pandas as pd
from sklearn.decomposition import PCA
import copy
from MyMatplotlib import MyMatplotlib
from TimeTool import TimeTool
from sklearn.preprocessing import MinMaxScaler


class Tools:
    def __init__(self, save_path):
        self.save_path = save_path
        self.fig_path = None
        self.return_inf = None
        self.X = None
        self.y = None
        self.column_names = None

    def set_X(self, X):
        self.X = X

    def set_y(self, y):
        self.y = y

    def set_savepath(self, sp):
        self.save_path = sp


class DataTransfer(Tools):
    def __init__(self, save_path):
        super().__init__(save_path)

    def aim(self, t=0):
        self.fig_path = None
        self.return_inf = None

        if t == 1:
            # 最大最小值标准化
            self.myMaxMinScaler(self.X, self.y)

    def myMaxMinScaler(self, X, y=None, predict_X=None, is_save=True):
        """
        最大最小值标准化
        !!!!!!!!!!!!!!!!!!!!!!!!!!待修改，如果有预测集则需要放在一起标准化
        :param X:
        :param y:
        :param predict_X: 是否有需要预测的转换X
        :return:
        """
        name = '最大最小值标准化'

        scaler = MinMaxScaler()
        new_X = scaler.fit_transform(X)
        df = pd.DataFrame(new_X, columns=X.columns)

        if predict_X is not None:
            px = scaler.fit(predict_X).transform(predict_X)
            pxx = pd.DataFrame(px, columns=predict_X.columns)
            excel_name2 = '[' + name + ']-预测集' + TimeTool().getCurrentTime() + '.xls'
            p2 = os.path.join(self.save_path, excel_name2)
            pxx.to_excel(p2, index=False)
        else:
            pxx = None

        if y is not None:
            df['label'] = y

        if is_save:
            excel_name = '[' + name + ']-' + TimeTool().getCurrentTime() + '.xls'
            file_savePath = os.path.join(self.save_path, excel_name)

            df.to_excel(file_savePath, index=False)
        return df


class PreAnalysis(Tools):
    def __init__(self, save_path):
        super().__init__(save_path)
        self.hue = None
        # 功能集成：字典
        self.funcs = {
            '特征矩阵图': self.correlationPair,
            '相关性分析': self.correlationHotMap,
            '缺失值分析': self.missingValueAnalysis,
        }

    def aim(self, t=0):
        """
        通过t来控制运行所有程序还是哪一个
        :param t:
            1：返回矩阵分析图的调用和参数，默认两个都生成
               根据是否是监督学习，选择性生成，非监督学习就不能
            2. 返回相关性分析的调用和参数，
        :return:
        """

        self.return_inf = None
        if t == 1:
            self.correlationPair(self.X)
        elif t == 1.1:
            self.correlationPair(self.X, self.y, hue=True)
        elif t == 1.2:
            self.correlationPair(self.X, self.y, hue=True, reg=True)
        elif t == 2:
            self.correlationHotMap(self.X)
        elif t == 3:
            self.missingValueAnalysis(self.X, self.y)

    def correlationHotMap(self, X, column_names=None, annot=False, change_ticks_fontsize=False, rotation_ticks=False):
        """
        关联矩阵分析-->热力图
        热力图没有label，不分因此只要X不要y
        :param X: 二维矩阵
        :param column_names: 属性的列名，如果没有传入列名的话，自动生成列名
        :param annot: 是否在格子里标注数据
        :param change_ticks_fontsize: 是否改变ticks的字体大小
        :param rotation_ticks: 是否旋转ticks（名字太长了就要这样做）
        :return:
        """

        func_name = '相关性分析'

        # 将二维矩阵转化为DataFrame
        if isinstance(X, pd.DataFrame):
            df = X
        else:
            df = pd.DataFrame(X, columns=column_names)
        corr_mat = df.corr()

        # 保存热力图元数据
        excel_name = TimeTool().getCurrentTime() + '.xls'
        file_savePath = os.path.join(self.save_path, excel_name)
        corr_mat.to_excel(file_savePath)

        # 绘制热力图
        self.fig_path = MyMatplotlib(self.save_path).plot_heatmap(corr_mat, annot, change_ticks_fontsize,
                                                                  rotation_ticks)
        return None

    def correlationPair(self, X, y=None, names=None, hue=False, reg=False, vars=None):
        """
        所有变量中任意两个变量之间的图形， 用矩阵图探索多维数据不同维度间的相关性
        这里由于可以，对不同的类进行分析， 所以可以传入y
        实际使用时，可以通过plot_pair函数的传参来设置，仅分析属性，还是连类别也分析
        需要根据y是否存在分为监督学习还是非监督学习
        :param X:
        :param y:
        :param names: 列名，属性名
        :param hue: 是否分类
        :param reg:
        :param vars:
        :return:
        """
        func_name = '特征矩阵图'

        # 将二维矩阵转化为DataFrame
        if isinstance(X, pd.DataFrame):
            df = X
        else:
            df = pd.DataFrame(X, columns=names)

        if hue:
            labels = [str(i) for i in y]
            df['label'] = labels

        # 绘制矩阵图
        self.fig_path = MyMatplotlib(self.save_path).plot_pair(df, hue, reg, vars)
        return None

    def missingValueAnalysis(self, X, y=None, names=None):
        """
        缺失值分析
        :param X:
        :param y:
        :param names: 列名，属性名
        :return:
        """
        # 将二维矩阵转化为DataFrame
        if isinstance(X, pd.DataFrame):
            df = X
        else:
            df = pd.DataFrame(X, columns=names)


class DimensionReduction(Tools):
    def __init__(self, save_path):
        super().__init__(save_path)
        # 降维方法名
        self.name = None
        # 随机种子
        self.random_state = 42
        # 模型类
        self.model = None
        # 若未给出，生成80%，90%，95%三个级别的数据
        self.p_list = [0.8, 0.9, 0.95]

        # 子类初始化
        try:
            # 固定每个模型的随机种子
            self.model.set_params(**{'random_state': self.random_state})
        except:
            pass


class MyPCA(DimensionReduction):
    """对相关系性较高的特征进行降维处理"""

    def __init__(self, path):
        super().__init__(path)
        self.name = 'PCA'
        self.model = PCA()

    def aim(self, t=0):
        """
        通过t来控制运行所有程序还是哪一个
        :return:
        """
        # 获取投射到新空间后每个特征的方差
        ii = self.get_vr(self.X)
        self.get_aim_percent(self.X, self.y)
        self.return_inf = '---> 原始数据投射到新空间后每个特征的方差为：\n' + ii + '\n'
        # 根据不同的信息保留比例获取操作后的数据
        self.return_inf += '---> 已保存阈值设置为【0.8, 0.9, 0.95】降维后的数据...'

    def get_vr(self, X):
        """获取保留的各个特征的方差"""
        model = copy.deepcopy(self.model)
        model.fit(X)
        ii = model.explained_variance_ratio_.tolist()
        ii = ["{:.4f}".format(s) for s in ii]
        return '       | ' + ' | '.join(ii) + ' |'

    def get_aim_percent(self, X, y, p=None):
        """
        获取保留p（1>p>0）以上信息的数据
        随着p的增大，保留的维度越高，数据越多
        """
        model = copy.deepcopy(self.model)
        if p is None:
            # 若未给出，生成80%，90%，95%三个级别的数据
            p = self.p_list
        else:
            if isinstance(p, float):
                p = [p]

        # 保存降维后的数据，并根据是否有y整合为新的数据
        for per in p:
            params = {'n_components': per}
            model.set_params(**params)
            new_data = model.fit_transform(X)
            df = pd.DataFrame(new_data)
            excel_name = '[' + str(per) + ']' + TimeTool().getCurrentTime() + '.xls'

            file_savePath = os.path.join(self.save_path, excel_name)

            if y is not None:
                df['label'] = y

            df.to_excel(file_savePath, index=False)

    def pca_patial(self, X, aim_columns, y=None, n_components=1, predict_X=None):
        """
        对多列分别降维后合并
        :param X:
        :param y:
        :param aim_columns: 多维数组[[], []]，内部[]放置了要进行标准化的列名
        :return:
        """
        # 遍历每一组列名，进行降维，暂时降至保留1个特征的信息
        df = X
        df_pre = predict_X
        n = 1
        keep_ratio = []
        for column in aim_columns:
            df_temp = df[column]
            df = df.drop(columns=column)

            df_pre_temp = df_pre[column]
            df_pre = df_pre.drop(columns=column)

            model = PCA(n_components=n_components)
            new_feature = model.fit_transform(df_temp)
            feature_keep = len(new_feature[0])
            new_column_name = ['新特征_' + str(i) for i in range(n, feature_keep + n, 1)]
            df = pd.concat([df, pd.DataFrame(new_feature, columns=new_column_name)], axis=1)
            keep_ratio.append(str(list(model.explained_variance_ratio_)))

            if predict_X is not None:
                px = model.transform(df_pre_temp)
                df_pre = pd.concat([df_pre, pd.DataFrame(px, columns=new_column_name)], axis=1)

            n += feature_keep

        if y is not None:
            df['label'] = y

        ratio_name = '-'.join(keep_ratio)
        excel_name = '[对多列分别降维后合并]-' + ratio_name + '-' + TimeTool().getCurrentTime() + '.xls'
        excel_name2 = '[对多列分别降维后合并]-预测集-' + ratio_name + '-' + TimeTool().getCurrentTime() + '.xls'
        file_savePath = os.path.join(self.save_path, excel_name)
        file_savePath2 = os.path.join(self.save_path, excel_name2)
        df.to_excel(file_savePath, index=False)
        df_pre.to_excel(file_savePath2, index=False)
