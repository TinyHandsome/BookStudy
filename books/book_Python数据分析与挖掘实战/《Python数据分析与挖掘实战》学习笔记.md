# 《Python数据分析与挖掘实战》学习笔记

[TOC]

## 写在前面

- 封面 | 摘要 | 关键词

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/3b6896c35a724a55b07d1a07b97f16d5.png)

- 读后感

  1. 这？字典变成自编？是我有问题，还是你有问题？都出书了，为什么会有这种低级问题？

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/e59bcf39871f43e2a7c2705fd0f67477.png)

- 摘抄

  1. matplotlib显示中文和负号

     ```python
     plt.rcParams['font.sans-serif'] = ['SimHei']
     plt.rcParams['axes.unicode_minus'] = False
     ```

     

- 传送门

## 1. 数据挖掘基础

1. 数据挖掘建模过程

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/ccd35e0b46ca4e108d390b2ba82c882d.png)

   - 定义挖掘目标
   - 数据采样
   - 数据探索
   - 数据预处理
   - 挖掘建模
   - 模型评价

2. 常用的数据挖掘建模工具

   1. SAS Enterprise Miner
   2. IBM SPSS Modeler
   3. SQL Server
   4. Python
   5. WEKA
   6. KNIME
   7. RapidMiner/YALE
   8. TipDM

## 2. Python数据分析简介

1. 列表list可以修改，元组tuple不可以

2. 其他创建字典dict的方法：
   - `dict([['A', 1], ['B', 2]])`
   - `dict.fromkeys(['A', 'B'], 0)`

3. 集合：set，{}
   - 元素不重复
   - 无序
   - 不支持索引

4. `map`：`map(lambda x, y: x*y, a: list, b: list)`
   - 逐一遍历
   - map效率更高，并且是懒加载

5. `reduce`：
   - 递归计算
   - `reduce(lambda x,y : x*y, range(1, n+1))`

6. `filter`：

   - `filter(lambda x: x > 5 and x < 8, range(10))`
   - 总结：操作上不如**列表表达式**，但是效率上快于列表表达式

7. Python数据挖掘相关扩展库

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/617a5b045820476bb673468e9389d332.png)
   
8. keras使用

   ```python
   from tensorflow.keras import Sequential
   from tensorflow.keras.layers import Dense, Dropout, Activation
   from tensorflow.keras.optimizers import SGD
   
   model = Sequential()
   model.add(Dense(64, input_shape=(20, )))
   model.add(Activation('tanh'))
   model.add(Dropout(0.5))
   model.add(Dense(64))
   model.add(Activation('tanh'))
   model.add(Dropout(0.5))
   model.add(Dense(1))
   model.add(Activation('sigmoid'))
   
   sgd = SGD(learning_rate=0.1, decay=1e-6, momentum=0.9, nesterov=True)
   model.compile(loss='mean_squared_error', optimizer=sgd)
   
   model.fit(X_train, y_train, nb_epoch-20, batch_size=16)
   score = model.evaluate(X_test, y_test, batch_size=16)
   ```


## 3. 数据探索

### 3.1 数据质量分析

脏数据

- 缺失值
- 异常值
- 不一致的值
- 重复数据
- 含有特殊符号的数据，如#、￥、*等

#### ① 缺失值分析

数据的缺失主要包括记录的缺失和记录中某个字段信息的缺失，两者都会造成统计结果不准确。

1. 缺失值产生的原因：
   1. 有些信息暂时无法获取，或者获取信息的代价太大。
   2. 有些信息是被遗漏的（人为因素和非人为原因）。
   3. 属性值不存在（例如未婚者的配偶姓名）。
2. 缺失值的影响：
   1. 数据挖掘建模将丢失大量的有用信息。
   2. 数据挖掘模型所表现出的不确定性更加显著，模型中蕴含的规律更难把握。
   3. 包含空值的数据会使建模过程陷入混乱，导致不可靠的输出。
3. 缺失值的分析：
   1. 使用简单的统计分析，可以得到含有缺失值的属性的个数，以及每个属性的未缺失数、缺失数与缺失率等。
   2. 从总体上来说，缺失值的处理分为
      1. 删除存在缺失值的记录
      2. 对可能值进行插补
      3. 不处理

#### ② 异常值分析

异常值分析是检验数据是否有录入错误以及含有不合常理的数据。异常值是指样本中的个别值，其数据明显偏离其余的观测值。异常值也称为离散点，异常值的分析也称为离群点分析。

1. 简单统计量分析

   对变量做一个描述性统计，进而查看不合理数据。最常用的统计量是最大值和最小值，用来判断这个变量的取值是否超出了合理的范围。

2. 3σ原则

   如果数据服从正态分布，在3σ原则下，异常值被定义为一组测定值中与平均值的偏差超过3倍标准差的值。这种值的出现属于小概率事件。如果数据不服从正态分布，也可以用远离平均值的多少倍标准差来描述。

3. 箱型图分析

   箱型图定义，异常值为小于QL - 1.5IQR 或大于QU + 1.5IQR 的值。

   其中，QL称为下四分位数，表示全部观察值中有四分之一的数据取值比它小；QU称为上四分位数，表示全部观察值中有四分之一的数据取值比它大；IQR称为四分位数间距，是QU与QL之差，其间包含了全部观察值的一半。

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/6b5b9332a62a4826a1e7765792f2e821.png)

#### ③ 一致性分析

数据不一致性是指数据的矛盾性、不相容性。

不一致数据的产生主要发生在数据集成的过程中，可能由于被挖掘数据是来自于从不同的数据源、对于重复存放的数据未能进行一致性更新造成的。

### 3.2 数据特征分析

#### ① 分布分析

分布分析能揭示数据的分布特征和分布类型。

对于定量数据，欲了解其分布形式是对称的还是非对称的，发现某些特大或特小的可疑值，课通过绘制频率分布表、绘制频率分布直方图、绘制茎叶图进行值观地分析；对于定性分析数据，可用饼图和条形图直观地显示分布情况。

1. 定量数据的分布分析

   对定量变量而言，选择“组数”和“组宽”是做频率分布分析时最主要的问题，按以下步骤进行：

   1. 求极差
   2. 决定组距与组数
   3. 决定分点
   4. 列出频率分布表
   5. 绘制频率分布直方图

   遵循的主要原则：

   1. 各组直接必须是相互排斥的
   2. 各组必须将所有的数据包含在内
   3. 各组的组宽最好相等

2. 定性数据的分布分析

   - 对于定性变量，常常根据变量的分类类型来分组，可以采用饼图和条形图来描述定性变量的分布

#### ② 对比分析

1. 绝对数比较
2. 相对数比较
   1. 结构相对数
   2. 比例相对数
   3. 比较相对数
   4. 强度相对数
   5. 计划完成程度相对数
   6. 动态相对数

#### ③ 统计量分析

1. 集中趋势：均值、中位数、众数

2. 离中趋势：极差、标准差、方差、变异系数、四分位间距

   - 变异系数度量 **标准差** 相对于 **均值** 的离中趋势，计算公示为：
     $$
     CV=\frac{s}{\overline{x}}\times100\%
     $$
     变异系数主要用来比较两个或多个具有不同单位或不同波动幅度的数据集的离中趋势

   - 四分位数间距：上四分位数$Q_U$与下四分位数$Q_L$之差，其间包含了全部观察值的一半。其值越大，说明数据的 **变异程度** 越大，反之越小。

#### ④ 周期性分析

#### ⑤ 贡献度分析

- 又：帕累托分析
- 帕累托法则：又称20/80定律。同样的投入放在不同的地方会产生不同的效益。

#### ⑥ 相关性分析

1. 直接绘制散点图

2. 绘制散点图矩阵

3. 计算相关系数

   1. Pearson相关系数

      **是对定距变量的统计**

      - 连续变量

      - 假设条件：

        a) 两个变量分别服从正态分布，通常用t检验检查相关系数的显著性；

        b) 两个变量的标准差不为0。

      - pearson 描述的是线性相关关系，取值[-1, 1]。负数表示负相关，正数表示正相关。在显著性的前提下，绝对值越大，相关性越强。绝对值为0， 无线性关系；绝对值为1表示完全线性相关。

      - 公式：

        ![pearson](https://pic2.zhimg.com/80/v2-0c8e4244ca787cd806c85c2dfa1bdf59_1440w.webp)

   2. [Spearman秩相关系数](https://zhuanlan.zhihu.com/p/339077538)

      **是对定序变量的统计**

      - 连续变量

      - 无参数的等级相关系数，亦即其值与两个相关变量的具体值无关，而仅仅与其值之间的大小关系有关。$d_i$表示两个变量分别排序后成对的变量位置差，$N$表示$N$个样本，减少异常值的影响。

      - 公式：

        ![spearman](https://pic4.zhimg.com/80/v2-fdd4fdb80002ece8d070b828ce900123_1440w.webp)

      - 皮尔逊相关系数适用于线性关系，而斯皮尔曼相关系数适用于单调关系，线性与单调的一个区别是，线性关系的斜率是固定的。如果数据看上去，既有点像线性关系，又有点像单调关系，那么使用斯皮尔曼相关系数；皮尔逊相关系数使用元数据进行计算的，而斯皮尔曼相关系数是基于秩计算的。

   3. *[Kendall相关系数](https://zhuanlan.zhihu.com/p/60059869)*

      - 有序分类变量

      - 属于等级相关系数。排序一致，则为1， 排序完全相反则为-1。

      - [公式：](https://www.jianshu.com/p/9dec47bac5b9)

        ![Tau-a](https://math.jianshu.com/math?formula=T%20a%20u-a%3D%5Cfrac%7BC-D%7D%7B%5Cfrac%7B1%7D%7B2%7D%20N(N-1)%7D)

        ![Tau-b](https://math.jianshu.com/math?formula=T%20a%20u-b%3D%5Cfrac%7BC-D%7D%7B%5Csqrt%7B(N%203-N%201)(N%203-N%202)%7D%7D)

        ![Tau-c](https://math.jianshu.com/math?formula=T%20a%20u-c%3D%5Cfrac%7BC-D%7D%7B%5Cfrac%7B1%7D%7B2%7D%20N%5E%7B2%7D%20%5Cfrac%7BM-1%7D%7BM%7D%7D)

      [小结：](https://guyuecanhui.github.io/2019/08/10/feature-selection-kendall/)

      1. **Kendall** 秩相关系数可以用于度量有序变量间相关性，只要求变量取值之间可比，对变量的分布和数据的距离不作假设；

      2. 能用 **Pearson** 相关系数和 **Spearman** 秩相关系数的地方都能用 **Kendall** 秩相关系数，但是 **Spearman** 和 **Kendall** 秩相关系数要对数据排序，复杂度远高于 **Pearson** 相关系数，因此能用 **Pearson** 相关系数的时候优先考虑 **Pearson** 相关系数；

      3. **Kendall** 秩相关系数依赖一致对和分歧对的计数，这里需要注意数据中是否有重复取值的情况，来选择使用 **Tau-a** 还是 **Tau-b** 进行计算。

      4. [Pearson相关与Spearman和Kendall相关](https://www.jianshu.com/p/9dec47bac5b9)

         非参数相关（指 spearman和kendall）的表达能力相对较弱，因为它们在计算中使用的信息较少。在Pearson的情况下，相关性使用有关均值和均值偏差的信息，而非参数相关性仅使用序数信息和成对分数。

         在非参数相关的情况下，X和Y值可能是连续的或有序的，并且不需要X和Y的近似正态分布。但在皮尔逊相关的情况下，它假定X和Y的分布应该是正态分布，并且也应该是连续的（**因此做pearson之前要做一些对数变换之类的尽量接近正态分布**）。

      5. Spearman相关与Kendall相关

         在正常情况下，Kendall相关性比Spearman相关性更强健和有效。这意味着当样本量较小或存在一些异常值时，首选Kendall相关。

         相关系数是测量**线性**（皮尔逊）或 **单调**（Spearman和Kendall）关系。

   4. 判定系数：pearson相关系数的平方：$r^2$

### 3.3 Python主要数据探索函数

#### ① 基本统计特征函数

![在这里插入图片描述](https://img-blog.csdnimg.cn/2f8f9d2cf8564cdc979d4a774aea7cd1.png)

- `corr(method='pearson')`：计算数据样本的相关系数矩阵，支持pearson(default)、spearman、kendall

#### ② 拓展统计特征函数

![在这里插入图片描述](https://img-blog.csdnimg.cn/5ee205f9840f47aab47b07654babfb2f.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/7c80ff6e2e94465b9da3c249ca1a9d55.png)

- cum系列函数是作为DataFrame或Series对象的方法而出现的，`D.cumsum()`
- rolling系列是pandas的函数，不是DataFrame或Series对象的方法，`pd.rolling_mean(D, k)`，意思是每k列计算一次均值，滚动计算

#### ③ 统计作图函数

![在这里插入图片描述](https://img-blog.csdnimg.cn/55c16974ef014e779e38f77cc6044a57.png)

- 盒图：表示多个样本的均值

- 误差条形图：同时显示下限误差和上限误差

- 最小二乘拟合曲线图：分析两两变量间的关系

- `plt.plot(x, y, S)`：S指定绘制时图形的类型、样式和颜色

  - `r`、`g`、`b`
  - `o`、`+`、`p`
  - `-`、`--`、`=`

- `D.plot(kind='box')`：kind参数用来指定作图的类型

  - `line`、`bar`、`barh`、`hist`、`box`、`kde`、`area`、`pie`

- 饼状图绘制示例

  ```python
  labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
  sizes = [15, 30, 45, 10]
  colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
  explode = (0, 0.1, 0, 0)
  
  plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
  # 显示为圆，避免比例压缩为椭圆
  plt.axis('equal')
  plt.show()
  ```

  ![请添加图片描述](https://img-blog.csdnimg.cn/4032ce8a66784e6a908d88c6d1d9e92c.png)


## 4. 数据预处理

数据预处理的主要内容包括：数据清洗、数据集成、数据变换和数据规约。

![在这里插入图片描述](https://img-blog.csdnimg.cn/ae85c1f29c354d0fa92178e63603559e.png)

### 4.1 数据清洗

数据清洗主要是删除原始数据集中的无关数据、重复数据，平滑噪声数据，筛选掉与挖掘主题无关的数据、处理缺失值、异常值等。

#### ① 缺失值处理

处理缺失值的方法可分为3类：删除记录、数据插补和不处理。

- 常用的插补方法：

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/df15d6180d3942ac8ce61de2880e91a2.png)

- 常用的插值方法：拉格朗日插值法、牛顿插值法、Hermite插值、分段插值、样条插值法等。

  - 拉格朗日插值公式结构紧凑，在理论分析中很方便，但是当插值节点增减时，插值多项式就会随之变化，这在实际计算中是很不方便的，为了克服这一缺点，提出了牛顿插值法。
  - 牛顿插值法也是多项式插值，但采用了另一种构造插值多项式的方法，与拉格朗日插值相比，具有承袭性和易于变动节点的特点。从本质上来说，两者给出的结果是一样的(相同次数、相同系数的多项式)，只不过表示的形式不同。因此，在 Python 的 Scipy 库中，只提供了拉格朗日插值法的函数(因为实现上比较容易)。

#### ② 异常值处理

- 常用的异常值处理方法：

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/26cf639dfb2643888f64e5f6fc8a7ed6.png)

- 在很多情况下，要先分析异常值出现的可能原因，再判断异常值是否应该舍弃，如果是正确的数据，可以直接在具有异常值的数据集上进行挖掘建模。

### 4.2 数据集成

在数据集成时，来自多个数据源的现实世界实体的表达形式是不一样的，有可能不匹配，要考虑实体识别问题和属性冗余问题，从而将源数据在最低层上加以转换、提炼和集成。

#### ① 实体识别

实体识别：从不同数据源识别处现实世界的实体，它的任务是统一不同源数据的矛盾之处。


























------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
