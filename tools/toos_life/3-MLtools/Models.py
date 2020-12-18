#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: Models.py
@time: 2020/4/29 15:22
@desc:
        [正则化的理解](https://www.zhihu.com/question/20924039)
        [惩罚参数C的理解](https://blog.csdn.net/csdn_lzw/article/details/80185529)
        我的理解：
            惩罚参数C越大 --> 越不允许出错 --> 偏向过拟合 --> 需要求解的系数越多 --> 正则化系数lamda越小

        [多项式朴素贝叶斯参数详解](https://www.jianshu.com/p/17b04a5b6410)
        [朴素贝叶斯三种方法的使用区别](https://blog.csdn.net/brucewong0516/article/details/78798359)
        [KNN参数详解](https://www.jianshu.com/p/871884bb4a75)
        [LR参数详解](https://www.jianshu.com/p/99ceb640efc5)
        [LR调参](https://www.cnblogs.com/webRobot/p/11781078.html)
        [SVM参数详解](https://blog.csdn.net/sun_shengyun/article/details/55669160)
        [SVM调参](https://www.cnblogs.com/yuehouse/p/9742697.html)
        [决策树参数详解](https://www.cnblogs.com/lyxML/p/9575820.html)
        [AdaBoost参数详解](https://www.cnblogs.com/mdevelopment/p/9445090.html)

"""
from xgboost import XGBClassifier
from MyModel import MyModel
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from collections import OrderedDict


# 1. Multinomial Naive Bayes Classifier / 多项式朴素贝叶斯
class MyMNB(MyModel):
    def __init__(self):
        super().__init__()
        self.name = "多项式朴素贝叶斯"
        self.is_ensemble = False
        self.chinese_name = "多项式朴素贝叶斯"
        self.english_name = "Multinomial Naive Bayes Classifier"
        self.parameters = OrderedDict([
            # alpha：拉普拉修/Lidstone平滑参数,浮点型,可选项,默认1.0
            ('alpha', [0, 0.25, 0.5, 0.75, 1])
        ])

    def init_model(self):
        self.model = MultinomialNB()


# 2. Gaussian Naive Bayes Classifier / 高斯朴素贝叶斯
class MyGNB(MyModel):
    def __init__(self):
        super().__init__()
        self.name = "高斯朴素贝叶斯"
        self.is_ensemble = False
        self.chinese_name = "高斯朴素贝叶斯"
        self.english_name = "Gaussian Naive Bayes Classifier"

        # 几乎没有参数可调
        self.parameters = None

    def init_model(self):
        self.model = GaussianNB()


# 3. KNN Classifier / K最近邻
class MyKNN(MyModel):
    def __init__(self):
        super().__init__()
        self.name = "K最近邻"
        self.is_ensemble = False
        self.chinese_name = "K最近邻"
        self.english_name = "KNN Classifier"

        self.parameters = OrderedDict([
            # n_neighbors: int, 可选参数(默认为 5)，每个点与周围多少个点进行比较
            ('n_neighbors', range(1, 10, 1))
        ])

    def init_model(self):
        self.model = KNeighborsClassifier()


# 4. Logistic Regression Classifier / 逻辑回归
class MyLR(MyModel):
    def __init__(self):
        super().__init__()
        self.name = "逻辑回归"
        self.is_ensemble = False
        self.chinese_name = "逻辑回归"
        self.english_name = "Logistic Regression Classifier"

        self.parameters = OrderedDict([
            # 正则化一般选择l2就ok了
            # 参数solver的选择，如果是L2正则化，那么4种可选的算法{'newton-cg', 'lbfgs', 'liblinear', 'sag'}都可以选择
            # 但是如果penalty是L1正则化的话，就只能选择'liblinear'了
            ('solver', ['newton-cg', 'lbfgs', 'liblinear', 'sag']),
            # 惩罚因子的调参与支持向量机一致
            ('C', [0.1, 1, 10])
        ])

    def init_model(self):
        self.model = LogisticRegression()


# 5. SVM Classifier / 支持向量机
class MySVM(MyModel):
    def __init__(self):
        super().__init__()
        self.name = "支持向量机"
        self.is_ensemble = False
        self.chinese_name = "支持向量机"
        self.english_name = "Support Vector Machine"

        self.parameters = OrderedDict([
            # C表示模型对误差的惩罚系数，C越大，模型越容易过拟合；C越小，模型越容易欠拟合
            ('C', [0.1, 1, 10]),
            # gamma反映了数据映射到高维特征空间后的分布，gamma越大，支持向量越多，gamma值越小，支持向量越少
            # gamma越小，模型的泛化性变好，但过小，模型实际上会退化为线性模型；gamma越大，理论上SVM可以拟合任何非线性数据
            ('gamma', [1, 0.1, 0.01])
        ])

    def init_model(self):
        self.model = SVC()


# 6. Decision Tree Classifier / 决策树
class MyDT(MyModel):
    def __init__(self):
        super().__init__()
        self.name = "决策树"
        self.is_ensemble = False
        self.chinese_name = "决策树"
        self.english_name = "Decision Tree Classifier"

        self.parameters = OrderedDict([
            # 特征选择标准，可以使用"gini"或者"entropy"，前者代表基尼系数，后者代表信息增益
            ('criterion', ['gini', 'entropy']),
            # 最大树深度越小越简单
            ('max_depth', range(1, 10, 1)),
            # 最小样本分割数越大越简单
            ('min_samples_split', list(range(2, 10, 1))[::-1])
        ])

    def init_model(self):
        self.model = DecisionTreeClassifier()


# 7. Random Forest Classifier / 随机森林
class MyRF(MyModel):
    def __init__(self):
        super().__init__()
        self.name = "随机森林"
        self.is_ensemble = True
        self.chinese_name = "随机森林"
        self.english_name = "Random Forest Classifier"

        self.parameters = OrderedDict([
            # 集成模型数量越小越简单
            ('n_estimators', range(10, 200, 20)),
            # 最大树深度越小越简单，集成学习的树不能太深
            ('max_depth', range(1, 5, 1)),
            # 最小样本分割数越大越简单
            ('min_samples_split', list(range(2, 10, 1))[::-1])
        ])

    def init_model(self):
        self.model = RandomForestClassifier()


# 8. GBDT(Gradient Boosting Decision Tree) Classifier / 梯度提升决策树
class MyGBDT(MyModel):
    def __init__(self):
        super().__init__()
        self.name = "GBDT"
        self.is_ensemble = True
        self.chinese_name = "梯度提升决策树"
        self.english_name = "Gradient Boosting Decision Tree Classifier"

        self.parameters = OrderedDict([
            # 集成模型数量越小越简单
            ('n_estimators', range(10, 200, 20)),
            # 最大树深度越小越简单，集成学习的树不能太深
            ('max_depth', range(1, 5, 1)),
            # 最小样本分割数越大越简单
            ('min_samples_split', list(range(2, 10, 1))[::-1])
        ])

    def init_model(self):
        self.model = GradientBoostingClassifier()


# 9. XGBoost / 极端梯度提升
class MyXGBoost(MyModel):
    def __init__(self):
        super().__init__()
        self.name = "XGBoost"
        self.is_ensemble = True
        self.chinese_name = "极端梯度提升树"
        self.english_name = "XGBoost"

        self.parameters = OrderedDict([
            # 集成模型数量越小越简单
            ('n_estimators', range(10, 200, 20)),
            # 最大树深度越小越简单，集成学习的树不能太深
            ('max_depth', range(1, 5, 1)),
            # 最小样本分割数越大越简单
            ('min_samples_split', list(range(2, 10, 1))[::-1])
        ])

    def init_model(self):
        self.model = XGBClassifier()


# 10. AdaBoost Classifier / 自适应提升法
class MyAdaboost(MyModel):

    def __init__(self):
        super().__init__()
        self.name = "Adaboost"
        self.is_ensemble = True
        self.chinese_name = "自适应提升算法"
        self.english_name = "Adaptive Boosting"

        self.parameters = OrderedDict([
            # 集成模型数量越小越简单
            ('n_estimators', range(10, 200, 20)),
            # 最大树深度越小越简单，集成学习的树不能太深
            ('base_estimator__max_depth', range(1, 5, 1)),
            # 最小样本分割数越大越简单
            ('base_estimator__min_samples_split', list(range(2, 10, 1))[::-1])
        ])

    def init_model(self):
        self.model = AdaBoostClassifier(base_estimator=DecisionTreeClassifier(class_weight='balanced', max_depth=2), n_estimators=200)
