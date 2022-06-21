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




















------

- :cloud: 我的CSDN：https://blog.csdn.net/qq_21579045
- :snowflake: 我的博客园：https://www.cnblogs.com/lyjun/
- :sunny: 我的Github：https://github.com/TinyHandsome
- :rainbow: 我的bilibili：https://space.bilibili.com/8182822
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友

