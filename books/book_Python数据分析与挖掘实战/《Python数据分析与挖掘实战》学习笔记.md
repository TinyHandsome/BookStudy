# 《Python数据分析与挖掘实战》学习笔记

[TOC]

## 写在前面

- 封面

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/3b6896c35a724a55b07d1a07b97f16d5.png)

- 读后感

  1. 这？字典变成自编？是我有问题，还是你有问题？都出书了，为什么会有这种低级问题？

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/e59bcf39871f43e2a7c2705fd0f67477.png)

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

1. 脏数据

   - 缺失值
   - 异常值
   - 不一致的值
   - 重复数据
   - 含有特殊符号的数据，如#、￥、*等

2. 缺失值分析

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

3. 异常值分析

   异常值分析是检验数据是否有录入错误以及含有不合常理的数据。异常值是指样本中的个别值，其数据明显偏离其余的观测值。异常值也称为离散点，异常值的分析也称为离群点分析。

   1. 简单统计量分析

      对变量做一个描述性统计，进而查看不合理数据。最常用的统计量是最大值和最小值，用来判断这个变量的取值是否超出了合理的范围。

   2. 3σ原则

      如果数据服从正态分布，在3σ原则下，异常值被定义为一组测定值中与平均值的偏差超过3倍标准差的值。这种值的出现属于小概率事件。如果数据不服从正态分布，也可以用远离平均值的多少倍标准差来描述。

   3. 箱型图分析

      箱型图定义，异常值为小于QL - 1.5IQR 或大于QU + 1.5IQR 的值。

      其中，QL称为下四分位数，表示全部观察值中有四分之一的数据取值比它小；QU称为上四分位数，表示全部观察值中有四分之一的数据取值比它大；IQR称为四分位数间距，是QU与QL之差，其间包含了全部观察值的一半。

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/6b5b9332a62a4826a1e7765792f2e821.png)

4. 一致性分析

   数据不一致性是指数据的矛盾性、不相容性。

   不一致数据的产生主要发生在数据集成的过程中，可能由于被挖掘数据是来自于从不同的数据源、对于重复存放的数据未能进行一致性更新造成的。

### 3.2 数据特征分析

1. 分布分析

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

      - 对于定性变量，常常根据变量的分类类型来分组，可以采用饼图和条形图来描述定型变量的分布












------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
