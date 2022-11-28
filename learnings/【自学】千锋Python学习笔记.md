# 千锋Python学习笔记

[TOC]

## 写在前面

- 学习链接：[Python 900集（学完可就业/2019版）](https://www.bilibili.com/video/BV15J411T7WQ)：`[1集: 199集]`
- 感想 | 摘抄
- 学习时遇到的问题

## 1. 前言

- python是一种解释型、面向对象、动态数据类型的高级程序设计语言。

- 编程语言就是人类和计算机进行交流的语言。

- REPL：读Read、执行Execute、打印Print、循环Loop 

  cmd：python这个环境就叫REPL

- 想要print有一个方式就是：`type(c).print`，在pycharm中会自动补全

- 集合set和元组touple的区别

  ![img](https://img-blog.csdn.net/20180822202401808?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNTk4MTMz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

- print函数：

  - 内容，可以多内容
  - `sep=' '`，分隔符
  - `end=’\n‘`，结尾h
  - `file=sys.stdout`，控制输出位置
  - 输出字符串
    - 占位符：%s %d %f
    - format

- 整数的表示方式

  - 二进制：`b = 0b101101101`
  - 八进制：`b = 0o34`
  - 十六进制：`b = 0x23`

- 运算符：

  - 赋值运算符
  - 内存分析：`id()`
  - 算数运算符
    - `**`：幂
    - `//`：取整
    - `%`：取余
  - 关系运算符：
    - `>`、`==`、`<`
    - `is`：用户对象比较，比较变量的id是否一致

- 小整数池和大整数池

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/0eacc50fee674849b5a0865a46b2c326.png)

  - pycharm等ide和terminal的大整数池不一样
  - pycharm等ide整体运行的时候共用一个大整数池，终端等交互式运行的时候每行代码单独使用一个整数池
  - 小整数：`[-5, 256]`，这些整数对象是提前建好的，不会被垃圾回收

- input输入的数据为字符串

- 逻辑运算符：返回True、False

  - and
  - or
  - not





















学到：P29

------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
