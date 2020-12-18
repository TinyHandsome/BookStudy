# GridSearchCV.grid_scores_和mean_validation_score报错

[TOC]

## 0. 写在前面

**参考书**

《Python数据科学手册》

**工具**

python3.5.1，Jupyter Notebook

## 1. 问题描述和解决过程

在P438页，**5.13.4 示例：不是很朴素的贝叶斯**中的**2. 使用自定义评估器**小节中有这样一行代码

`scores = [val.mean_validation_score for val in grid.grid_scores_]`

运行之后报错：

> AttributeError: 'GridSearchCV' object has no attribute 'grid_scores_'

![img](https://img-blog.csdnimg.cn/20190611142821931.png)

经过百度了之后，可以知道`grid_scores_`在最新的sklearn中已经被弃用了，换成了`cv_results_`，参考链接：<https://blog.csdn.net/weixin_40283816/article/details/83346098>

那么，更改这个参数后，依然报错：

> AttributeError: 'str' object has no attribute 'mean_validation_score'

![img](https://img-blog.csdnimg.cn/20190611143203126.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

这个问题就再也没有搜到好的解决方案了，所以我去查了GridSearchCV的文档：<https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html>

然后发现，关于`cv_results_`的内容如下：

![img](https://img-blog.csdnimg.cn/20190611143427228.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

这就很尴尬了，所以没有一个参数是包含**validation**关键字的，我的理解是，验证集和测试集在某种情况下可以认为是等价的。所以我猜测**mean_validation_score**对应的应该就是**mean_test_score**。

这样，原来的代码就改成了

`scores = grid.cv_results_['mean_test_score']`

为了证明我的猜想是正确的，所以，按照得到的scores结果，顺着其他的代码，知道最后绘图：

![img](https://img-blog.csdnimg.cn/20190611143734822.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

事实证明，跟书上得到图一毛一样，所以证明我对源代码修改的猜想是正确的。

**即证明了**：

旧版本代码：`scores = [val.mean_validation_score for val in grid.grid_scores_]`

与新版本代码：`scores = grid.cv_results_['mean_test_score']`

**等价！**

## 2. 不想比比直接看结果部分

将代码：`scores = [val.mean_validation_score for val in grid.grid_scores_]`

改成：`scores = grid.cv_results_['mean_test_score']`



------

我的CSDN：https://blog.csdn.net/qq_21579045

我的博客园：https://www.cnblogs.com/lyjun/

我的Github：https://github.com/TinyHandsome

纸上得来终觉浅，绝知此事要躬行~

欢迎大家过来OB~

by 李英俊小朋友