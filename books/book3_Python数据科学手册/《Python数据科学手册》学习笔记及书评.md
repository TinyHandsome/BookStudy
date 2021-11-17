# 《Python数据科学手册》学习笔记

[TOC]

## 写在前面

- 封面

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/941e2c1cb6c140d6971e92ece4ccd8cf.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

- 读后感

  - 只能说挺不错的，前面数据分析部分挺好，后面机器学习部分差点东西

## 1. 食谱数据库数据找不到的问题

- 问题：

  - 在P163页，3.11.3 案例：食谱数据库中，涉及到的食谱数据无法下载，在网上也找不到资源。**是不是很揪心！！！是不是很绝望！！！**
  - 我也是。。。然后我在网上搜了大概半个小时把，放弃了，然后慢慢看书上给的连接：[食谱数据库](https://github.com/fictivekin/openrecipes)
  - 我想，肯定有很多跟我看同一本书的歪果仁，在评论区吐槽没有数据。
  - 果然让我找到了解决办法。。。时隔多年，作者之一总算过来提供最新数据连接了。。。[参考链接](https://github.com/fictivekin/openrecipes/issues/218)

- 结论：

  - 数据连接：https://s3.amazonaws.com/openrecipes/20170107-061401-recipeitems.json.gz

  - 下载方法：右键另存为就完事儿了。。。（链接都有了，再不会我就没辙了。。。）下完了然后右键解压缩。。。如图。。。

    ![img](https://img-blog.csdnimg.cn/20190521110201589.png)

## 2.Seaborn马拉松可视化里时分秒转化为秒数的问题

- [抄作业](https://www.jianshu.com/p/6ab7afa059d1)

  > 在做Python Data Science Handbook的实例学习，4.16.3 案例：探索马拉松比赛成绩里，有提示将时分秒的时间化为秒的总数，以方便画图。书里给出的指令是：
  >
  > **data['split_sec']=data['split'].astype(int)/1E9**
  >
  > **data['final_sec']=data['final'].astype(int)/1E9**
  >
  > 我用这种方式会出现以下错误：
  >
  > **TypeError: cannot astype a timedelta from [timedelta64[ns]] to [int32]**

- 结论

  - 描述的连接里面给出了一种解决办法，可是这种解决办法太复杂了，我想了一个更简单的

  - 先写一个将Timedelta格式的时间数据转化为总秒数的函数：

    ```python
    data['split_sec'] = data['split'].apply(transfor_time)
    data['final_sec'] = data['final'].apply(transfor_time)
    ```

  - 然后对我们需要的列广播这个函数：

    ```python
    data['split_sec'] = data['split'].apply(transfor_time)
    data['final_sec'] = data['final'].apply(transfor_time)
    ```

  - 查看结果：

    ```python
    data.head()
    ```

    ![img](https://img-blog.csdnimg.cn/20190530100318792.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

  - OK！完美解决。。。

## 3. scikit-learn使用fetch_mldata无法下载MNIST数据集的问题

- 问题：

  - 显示下载超时，链接不上，不能下载等

- 结论：

  - [直接下载MNIST数据集](https://github.com/amplab/datascience-sp14/raw/master/lab7/mldata/mnist-original.mat)

  - 把数据集保存到mldata文件夹中：

    ![img](https://img-blog.csdnimg.cn/20190608201943584.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

- 参考链接：[Error Downloading MNIST #143](<https://github.com/ageron/handson-ml/issues/143>)

## 4. GridSearchCV.grid_scores_和mean_validation_score报错

- 问题：

  - 在P438页，**5.13.4 示例：不是很朴素的贝叶斯**中的**2. 使用自定义评估器**小节中有这样一行代码：`scores = [val.mean_validation_score for val in grid.grid_scores_]`

  - 运行之后报错：`AttributeError: 'GridSearchCV' object has no attribute 'grid_scores_'`

    ![img](https://img-blog.csdnimg.cn/20190611142821931.png)

  - 经过百度了之后，可以知道`grid_scores_`在最新的sklearn中已经被弃用了，换成了`cv_results_`，[参考链接](https://blog.csdn.net/weixin_40283816/article/details/83346098)

  - 那么，更改这个参数后，依然报错：`AttributeError: 'str' object has no attribute 'mean_validation_score'`

    ![img](https://img-blog.csdnimg.cn/20190611143203126.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

  - 这个问题就再也没有搜到好的解决方案了，所以我去查了[GridSearchCV的文档](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)

  - 然后发现，关于`cv_results_`的内容如下：

    ![img](https://img-blog.csdnimg.cn/20190611143427228.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

  - 这就很尴尬了，所以没有一个参数是包含**validation**关键字的，我的理解是，验证集和测试集在某种情况下可以认为是等价的。所以我猜测**mean_validation_score**对应的应该就是**mean_test_score**

  - 这样，原来的代码就改成了`scores = grid.cv_results_['mean_test_score']`

  - 为了证明我的猜想是正确的，所以，按照得到的scores结果，顺着其他的代码，知道最后绘图：

    ![img](https://img-blog.csdnimg.cn/20190611143734822.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

  - 事实证明，跟书上得到图一毛一样，所以证明我对源代码修改的猜想是正确的

  - **即证明了**：

    - 旧版本代码：`scores = [val.mean_validation_score for val in grid.grid_scores_]`
    - 与新版本代码：`scores = grid.cv_results_['mean_test_score']`
    - **等价！**

## 5. Jupyter导出PDF从入门到绝望

- 问题：

  - 我在使用jupyter lab的时候，想要把我的代码和结果导出成pdf格式的（由于里面有图片，所以不想导出成html）。然后报错：

    ![img](https://img-blog.csdnimg.cn/20190522140525488.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

  - 然后我用pip安装了pandoc，发现并没有什么luan用。并且好像跟报错所指的pandoc不一样。反正就是绝望就完事儿了

- 方案：

    1. 下载安装windows开发环境包的管理器，Chocolatey。参考官网了连接，用cmd粘代码就能装：[官网](https://chocolatey.org/)

       `@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"`

    2. 然后呢，就可以用这个管理工具安装pandoc了，参考[pandoc官网](https://pandoc.org/installing.html)

       `choco install pandoc`

       ![img](https://img-blog.csdnimg.cn/20190522140347835.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

    3. 安装完事儿！

       ![img](https://img-blog.csdnimg.cn/20190522141137671.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

    4. 然后导出pdf的时候发现，竟然对pandoc的版本有要求，也是佛了，那就重新搞一下把。。。

       ![img](https://img-blog.csdnimg.cn/20190522141725475.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

       安装固定版本的pandoc，根据[官网发布的版本list](<https://pandoc.org/releases.html#pandoc-1.19.2.4-10-sep-2017>)，我选择安装1.19版本的。`choco install pandoc --version 1.19`

       ![img](https://img-blog.csdnimg.cn/20190522145630612.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

       安装时安装完毕了，不知道为啥，一副好像报错了的样子，下的我赶紧去看一下到底是安装好了没。。。

       ![img](https://img-blog.csdnimg.cn/2019052214583633.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

       应该是完事儿了，然后试试导出pdf。

    5. pandoc好像是没有问题了，可是另一个包好像又除了问题：

       ![img](https://img-blog.csdnimg.cn/20190522145613941.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

       所以现在又要安装这个：

       `choco install miktex`

       ![img](https://img-blog.csdnimg.cn/20190522150040633.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

    6. 完。。。做完这一步，电脑自动重启了，然后jupyter lab打不开了，报错：

       `ImportError: cannot import name 'constants' from 'zmq.backend.cython’`

       然后没办法，用pip升级了一下pyzmq包，总算是能打开了。。。

       ![img](https://img-blog.csdnimg.cn/20190522151612816.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

       然后，告诉我，我下载的插件不能用了，要重新“build”，所以就重新安装了插件。。。（像显示目录啊之类的插件。。。）

       ![img](https://img-blog.csdnimg.cn/2019052215174854.png)

       我真的很绝望。。。

       ![img](https://img-blog.csdnimg.cn/20190522153316641.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

    7. 然后依然报同样的错误。。。于是我怀疑，是不是MikTex有错，于是在官网上下了一个exe安装的那种，一路确认下去。。。[参考链接](<https://blog.csdn.net/csdnsevenn/article/details/81091523>)、[下载链接](https://miktex.org/)

       果然，在点了导出pdf的时候，报错缺少的文件就弹出来安装程序了。。。

       ![img](https://img-blog.csdnimg.cn/20190522161935621.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

    8. 然后就成功保存pdf啦！

       ![img](https://img-blog.csdnimg.cn/20190522162225837.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

- 另辟蹊径

  说实话，这样导出来的pdf并不好看，还有一种方法，直接导出html，里面保留了插入的图片的那种，更能还原jupyter原来的排版。[参考链接](https://www.jianshu.com/p/49a0c9f74d59)

## 6. 机器学习部分笔记

### 6.1 判定系数

1. 定义

   判定系数（coefficient of determination），也叫可决系数或决定系数，是指在线性回归中，回归平方和与总离差平方和之比值，其数值等于相关系数的平方。它是对估计的回归方程拟合优度的度量。（参考：[百度百科](https://baike.baidu.com/item/%E5%88%A4%E5%AE%9A%E7%B3%BB%E6%95%B0/2393145?fr=aladdin)）

   判定系数（记为R$^2$）在统计学中用于度量因变量的变异中可由自变量解释部分所占的比例，以此来判断统计模型的解释力。对于简单线性回归而言，判定系数为样本相关系数的平方。

   假设一数据集包括$y_1, y_2, ..., y_n$共n个观察值，相对应的模型预测值分别为$f_1, f_2, ..., f_n$。定义残差$e_i = y_i - f_i$，

   平均观察值为：$\bar{y} = \cfrac{1}{n} \sum\limits_{i=1}^n y_i$

   于是可以得到总平方和：$SS_{tot} = \sum\limits_{i=1} (y_i - \bar{y})^2$

   回归平方和：$SS_{reg} = \sum\limits_{i=1} (f_i - \bar{y})^2$

   残差平方和：$SS_{res} = \sum\limits_{i=1} (y_i - f_i)^2 = \sum\limits_{i=1} e_i^2$

   由此，判定系数可定义为：$R^2 = 1 - \cfrac{SS_{res}}{SS_{tot}}$

2. 总结

   R$^2$ = 1：表示模型与数据完全吻合。

   R$^2$ = 0：表示模型不比简单取均值好。

   R$^2$ < 0：表示模型性能很差。

3. 系数标准

   判定系数只是说明列入模型的所有解释变量对因变量的联合的影响程度，不说明模型中单个解释变量的影响程度。
   判定系数达到多少为宜？没有一个统一的明确界限值；若建模的目的是预测因变量值，一般需考虑有较高的判定系数。若建模的目的是结构分析，就不能只追求高的判定系数，而是要得到总体回归系数的可信任的估计量。**判定系数高并不一定说明每个回归系数都可信任。**

### 6.2 朴素贝叶斯

1. 贝叶斯定理

   我们在生活中经常遇到这种情况：我们可以很容易直接得出P(A|B)，P(B|A)则很难直接得出，但我们更关心P(B|A)，贝叶斯定理就为我们打通从P(A|B)求得P(B|A)的道路。

   $P(B|A) = \cfrac{P(A|B)P(B)}{P(A)}$

   推导：$P(A, B) = P(B|A) * P(A) = P(A|B) * P(B)$

   参考：[机器学习之贝叶斯（贝叶斯定理、贝叶斯网络、朴素贝叶斯）](<https://blog.csdn.net/weixin_42180810/article/details/81278326>)

   朴素贝叶斯分类是一种十分简单的分类算法，叫它朴素贝叶斯分类是因为这种方法的思想真的很朴素。

   朴素贝叶斯的思想基础是这样的：**对于给出的待分类项，求解在此项出现的条件下各个类别出现的概率，哪个最大，就认为此待分类项属于哪个类别。**通俗来说，就好比这么个道理，你在街上看到一个黑人，我问你你猜这哥们哪里来的，你十有八九猜非洲。为什么呢？因为黑人中非洲人的比率最高，当然人家也可能是美洲人或亚洲人，但在没有其它可用信息下，我们会选择条件概率最大的类别，这就是朴素贝叶斯的思想基础。

   - 假设每个标签的数据都服从简单的高斯分布，最容易理解的朴素贝叶斯分类器：**高斯朴素贝叶斯**，参考：[透彻理解高斯分布](https://baijiahao.baidu.com/s?id=1621087027738177317&wfr=spider&for=pc)。
   - 假设特征是由一个简单的多项式分布生成，适合用于描述出现次数或者出现次数比列的特征：**多项式朴素贝叶斯**，参考：[朴素贝叶斯的三个常用模型：高斯、多项式、伯努利](<https://blog.csdn.net/qq_27009517/article/details/80044431>)

2. 朴素贝叶斯的应用场景

   由于朴素贝叶斯分类器对数据有严格的假设，因此它的训练效果通常比复杂模型的差。其优点主要体现在以下四个方面。

   - 训练和预测的速度非常快
   - 直接使用概率预测
   - 通常很容易理解
   - 可调参数（如果有的话）非常少。

   朴素贝叶斯分类器非常适合用于以下应用场景：

   - 假设分布函数与数据匹配（实际中很少见）。
   - 各种类型的区分度很高，模型复杂度不重要。
   - 非常高维度的数据，模型复杂度不重要。

### 6.3 自举重采样方法

- 模式识别中每个方法的实现都是基于一个特定的数据样本集的，但是这个样本集只是所有可能的样本中的一次随机抽样，毕竟在我们的生活实际中存在着万物众生，多到我们数也数不清，甚至计算机都无法统计的清，而我们搜集到的充其量只是其中很小很小的一部分，这也是为什么机器学习中缺少的只是数据，只要有足够多的学习数据，就一定能取得惊人的结果，因此模式识别和机器学习中的很多方法的实现结果都无疑会受到这种随机性的影响，我们训练得到的分类器也因此具有偶然性，尤其是样本不足够多时更为明显。
- 对于**决策树**而言，其树的生长是采用的**贪心算法**，只考虑**当前局部的最优**，因此其受这种随机性影响会更加严重，这也是为什么有的**决策树泛化能力那么差**的原因。
- 针对这种随机性的影响，最早在统计学中有人提出了一种叫做”自举（Bootstrap）“的策略，基本思想是对现有样本进行重复采样而产生多个样本子集，通过这种多次重复采样来模拟数据的随机性，然后在最后的输出结果中加进去这种随机性的影响。随后有人把这种自举的思想运用到了模式识别中，衍生出了一系列的解决方法，像随机森林、Bagging、Adaboost等。

### 6.4 白化

- 白化的目的是去除输入数据的冗余信息。假设训练数据是图像，由于图像中相邻像素之间具有很强的相关性，所以用于训练时输入是冗余的；白化的目的就是降低输入的冗余性。

- 输入数据集X，经过白化处理后，新的数据X'满足两个性质：

  (1) 特征之间相关性较低；
  (2) 所有特征具有相同的方差。

- 其实我们之前学的PCA算法中，可能PCA给我们的印象是一般用于降维操作。然而其实PCA如果不降维，而是仅仅使用PCA求出特征向量，然后把数据X映射到新的特征空间，这样的一个映射过程，其实就是满足了我们白化的第一个性质：除去特征之间的相关性。因此白化算法的实现过程，第一步操作就是PCA，求出新特征空间中X的新坐标，然后再对新的坐标进行方差归一化操作。

- 参考链接：[机器学习（七）白化whitening](<https://blog.csdn.net/hjimce/article/details/50864602>)，[PCA 和 白化区别](https://blog.csdn.net/u010681136/article/details/41746349)

### 6.5 机器学习章节总结

1. 有监督学习
   - **高斯朴素贝叶斯（Gaussian naive Bayes）**：速度快，不需要选择超参数，所以通常很适合作为初步分类手段，在借助更复杂的模型进行优化之前使用。<u>这个方法假设每个特征中属于一类的观测值都符合高斯分布，且变量无协方差（即线性无关）。</u>椭圆曲线表示每个标签的**高斯生成模型**，越靠近椭圆中心的可能性越大。通过这种类似的生成模型，可以计算出任意数据点的似然估计（likelihood）P（特征|$L_1$），然后根据贝叶斯定理计算出后验概率比值，从而确定每个数据点可能性最大的标签。**贝叶斯主义**（Bayesian formalism）的一个优质特性是它天生支持概率分类，我们可以用`predict_proba`方法计算样本属于某个标签的概率。**缺点**：由于分类结果只能依赖于一开始的模型假设，因此高斯朴素贝叶斯经常得不到非常好的结果。
   - **多项式朴素贝叶斯（multinomial naive Bayes）**：<u>它假设特征是由一个简单多项式分布生成的。</u>**优点**：多项分布可以描述各种类型样本出现次数的概率，因此多项式朴素贝叶斯非常适用于描述出现次数或者出现次数比例的特征。
   - **简单线性回归（Linear Regression）**：将数据拟合成一条直线。除了简单的线性拟合，它还可以处理多维度的线性回归模型。
   - **基函数回归（basis function regression）**：通过基函数对原始数据进行变换，从而将变量间的线性回归模型转换为非线性回归模型。有**多项式基函数**、**高斯基函数**等。
   - **正则化（regularization）**：虽然在线性回归模型中引入基函数会让模型变得更加灵活，但是也很容易造成过拟合。当基函数重叠的时候，通常就表明出现了过拟合：相邻基函数的系数想相互抵消。<u>对较大的模型参数进行惩罚（penalize）</u>，从而抑制模型的剧烈波动，这个惩罚机制被称为正则化。有**岭回归（ridge regression，$L_2$范数正则化）**：$P = \alpha \sum_{n=1}^N \theta_n^2$、**Lasso正则化（$L_1$范数）**：$P = \alpha \sum_{n=1}^N |\theta|$。Lasso正则化倾向于构建稀疏矩阵，即它更喜欢将模型系数设置为0。
   - **支持向量机（support vector machine, SVM）**：不同于贝叶斯分类器，首先对每个类进行了随机分布的假设，然后用生成的模型估计新数据点的标签。——**生成分类**方法；支持向量机是**判别分类**方法：不再为每类数据建模、而是用一条分割线（二维空间中的直线或曲线）或者流体形（多维空间中的曲线、曲面等概念的推广）将各种类型分割开。**边界最大化**评估器。**核变换**和**核函数技巧**处理非线性问题。SVM实现了一些修正因子来**软化边界**。
   - **决策树**：采用非常直观的方式对事物进行分类或打标签，**二叉树分支方法**。**缺点**：决策树非常容易陷得很深（过拟合）。
   - **随机森林**：通过组合多个过拟合评估器来降低过拟合程度的想法，其实是一种集成学习方法，称为**装袋算法**。**优点**：无参数的随机森林模型非常适合处理多周期数据，不需要我们配置多周期模型！训练和预测速度都非常快。多任务可以直接并行计算。多棵树可以进行概率分类。无参数模型很灵活，在其他评估器都欠拟合的任务中表现突出。**缺点**：结果不太容易解释。
2. 无监督学习
   - **主成分分析技术（principal component analysis, PCA）**：这是一种快速线性降维技术。<u>沿着最不重要的主轴的信息都被去除了，仅留下含有最高方差值的数据成分。</u>**降维原理**：发现一组比原始的像素基向量更能有效表示输入数据的基函数。**用PCA作噪音过滤**：建模->逆变换重构。**缺点**：经常受数据集的异常点影响。`RandomizedPCA`：使用了一个非确定算法，快速地近似计算出一个维度非常高的数据的前几个主成分。`SparsePCA`：引入了一个正则项来保证成分的稀疏性。
   - **流形学习**：<u>它试图将一个低维度流形嵌入到一个高维度空间来描述数据集。</u>**多维度标度法（multidimensional scaling，MDS）**：它可以将一个数据集的距离矩阵还原成一个D维坐标来表示数据集。**缺点**：无法展示数据非线性嵌入的特征。当MDS失败时，**局部线性嵌入法（locally linear embedding，LLE）**：该方法不保留所有的距离，而是只保留邻节点间的距离。通常情况下，modified LLE的效果比用其他算法还原实现定义好的流形数据的效果好。**保距映射法（isometric mapping，Isomap）**：虽然LLE通常对现实世界的高维数据源的学习效果比较差，但是Isomap算法往往会获得比较好的嵌入效果。**t-分布邻域嵌入算法（t-distributed stochastic neighbor embedding, t-SNE）**：将它用于高度聚类的数据效果比较好，但是该方法比其他方法学习速度慢。
   - **k-means聚类**：在不带标签的多维数据集中寻找确定数量的簇，最优的聚类结果需要符合以下两个假设：a. “簇中心点”是属于该簇的所有数据点坐标的算术平均值。b. 一个簇的每个点到该簇中心点的距离比其他簇中心点的距离短。<u>k-means方法使用了一种容易理解、便于重复的期望最大化算法（E-M算法）取代了穷举搜索。</u>**使用E-M算法时的注意事项**：a. 可能不会达到全局最优结果；b. 簇数量必须事先定好；c. k-means算法只能确定线性聚类边界。但是我们可以通过一个**核变换**将数据投影到更高维的空间，投影后的数据使线性分离称为可能。（这种核k-means算法可以在`sklearn.cluster.SpectralClustering`评估器中实现，它使用最邻近来计算数据的高维表示，然后用k-means算法分配标签）； d. 当数据量较大时，k-means会很慢。这时就需要将“每次迭代都必须使用所有数据点”这个条件放宽，<u>例如每一步仅使用数据集的一个子集来更新簇中心点。</u>这恰恰就是**批处理（batch-based）k-means**算法的核心思想，该算法在`sklearn.cluster.MiniBatchKMeans`中实现。还可以使用k-means用于**色彩压缩**。**缺点**：在实际应用中，k-means的非概率性和它仅根据到簇中心点的距离来指派簇的特点将导致性能低下。由于k-means本身没有度量簇的分配概率或不确定性的方法，k-means可以理解为在每个簇的中心放置了一个圆，在这个圆圈之外的任何点都不是该簇的成员。所有k-means的这两个缺点——**类的形状缺少灵活性**、**缺少簇分配的概率**——使得它对许多数据集（特别是低维数据集）的拟合效果不尽人意。
   - **高斯混合模型（Gaussian mixture model, GMM）**：该模型可以被看作是k-means思想的一个扩展，一个聚类和密度评估器的混合体。<u>GMM模型试图将数据构造成若干服从高斯分布的概率密度函数簇，即用不同高斯分布的加权汇总来表示概率分布估计。</u>高斯混合模型本质上与k-means模型非常类似，它们都是用了**期望最大化（E-M）**方法。但高斯混合模型的每个簇的结果并不与硬边缘的空间有关，而是通过高斯平滑模型实现。GMM算法的本质是一个密度估计算法，即GMM拟合的结果并不是一个聚类模型，而是描述数据分布的生成概率模型。GMM可以利用改模型来评估数据的似然估计，并利用交叉验证来防止过拟合，还有一些纠正过拟合的标准分析方法，例如**赤池信息准则（Akaike information criterion，AIC）**、**贝叶斯信息准则（Bayesian information criterion，BIC）**调整模型的似然估计。<u>类的最优数量出现在AIC或BIC曲线最小值的位置。</u>**生成模型是贝叶斯生成分类器的一个非常有用的成分。**
   - **核密度估计（kernel density estimation，KDE）**：该算法将高斯混合理念扩展到了逻辑极限（logical extreme）。<u>它通过对每个点生成高斯分布的混合成分，获得本质上是无参数的密度估计器。</u>核密度估计的自有参数是：a. 核类型（kernel），它可以指定每个点核密度分布的形状；b. 核带宽（kernel bandwidth），它控制每个点的核的大小。
   
3. 验证模型（根据书上的例子，分为分类和回归，当然部分函数是可以混用的）

   1. 留出集和特征工程
      - `sklearn.model_selection.train_test_split`：**留出集**。`X1, X2, y1, y2 = train_test_split(X, y, random_state, train_size)`
      - `sklearn.feature_extraction.DictVectorizer`：**独热编码**。解决常见的非数值类型的分类特征。`vec = DictVectorizer(sparse, dtype)`
      - `sklearn.feature_extraction.text.CountVectorizer`：**单词统计**。将文字编码成数字的技术手段。`vec = CountVectorizer()`
      - `sklearn.feature_extraction.text.TfidVectorizer`：**TF-IDF**（term frequency-inverse document frequency，词频逆文档频率）。通过单词在文档中出现的频率来衡量其权重，IDF的大小与一个词的常见程度成反比。`vec = TfidVectorizer()`
      - `sklearn.preprocessing.PolynomialFeatures`：**多项式特征**，输入特征经过数学变换衍生出来的新特征，这种特征叫做**衍生特征**，这种处理方式被称为**基函数回归**（basis function regression）。`poly = PolynomialFeatures(degree, include_bias)`
      - `sklearn.preprocessing.Imputer`：**缺失值补充**。用均值、中位数、众数等填充方法补充缺失值。`imp = Imputer(strategy)`
      - `sklearn.pipeline.make_pipeline`：**特征管道**。将多个步骤串起来。`model = make_pipeline(*steps)`
      - `skimage.feature.hog`：**HOG特征（方向梯度直方图，Histogram of Oriented Gradients）**。它可以将图像像素转换为向量形式，与图像具体内容有关，与图像合成因素无关。它是一个简单的特征提取程序，专门用来识别行人（pedestrians）的图像内容。
      
   2. 分类（Classification）
      - `sklearn.metrics.accuracy_score`：验证模型越策结果的**准确率**（预测的所有结果中，正确结果占总预测样本数的比例）。`accuracy_score(y_true, y_pred)`
      - `sklearn.metrics.confusion_matrix`：**混淆矩阵**，分类结果和原始标签的一个表。`confusion_matrix(y_true, y_pred)`
      - `sklearn.model_selection.cross_val_score`：**交叉验证**。`cross_val_score(model, X, y, cv)`
      - `sklearn.model_selection.LeaveOneOut`：**留一（LOO）交叉验证**。`cross_val_score(model, X, y, cv=LeaveOneOut())`
   3. 回归（Regression）
      - `sklearn.model_selection.validation_curve`：**验证曲线**。计算验证范围内的训练得分和验证得分。`train_score, val_score = validation_curve(model, X, y, param_name, param_range, cv)`
      - `sklearn.model_selection.learning_curve`：**学习曲线**。反映训练集规模的训练得分 / 验证得分曲线。`learning_curve(model, X, y, cv, training_sizes)`
      - `sklearn.model_selection.GridSearchCV`：**网格搜索**。寻找模型的最优参数。`GridSearchCV(model, param_grid, cv)`

## 7. 高斯过程学习笔记 / Gaussion Process

- 参考链接：[透彻理解高斯过程Gaussian Process (GP)](https://blog.csdn.net/paulfeng20171114/article/details/80276061)

  > 1. 高斯过程模型属于无参数模型，相对解决的问题复杂度及与其它算法比较减少了算法计算量。
  > 2. 高斯模型可以解决高维空间（实际上是无限维）的数学问题，可以面对负杂的数学问题。
  > 3. 结合贝叶斯概率算法，可以实现通过先验概率，推导未知后验输入变量的后验概率。由果推因的概率。
  > 4. 高斯过程观测变量空间是连续域，时间或空间。
  > 5. 高斯过程观测变量空间是实数域的时候，我们就可以进行回归而实现预测。
  > 6. 高斯过程观测变量空间是整数域的时候（观测点是离散的），我们就可以进行分类。结合贝叶斯算法甚至可以实现单类分类学习（训练），面对小样本就可以实现半监督学习而后完成分类。面对异常检测领域很有用，降低打标签成本（小样本且单类即可训练模型）。 
  >    所以说，我们快点进入高斯过程-贝叶斯概率算法模型吧，功能非凡。 


------

- :cloud: 我的CSDN：https://blog.csdn.net/qq_21579045
- :snowflake: 我的博客园：https://www.cnblogs.com/lyjun/
- :sunny: 我的Github：https://github.com/TinyHandsome
- :rainbow: 我的bilibili：https://space.bilibili.com/8182822
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友