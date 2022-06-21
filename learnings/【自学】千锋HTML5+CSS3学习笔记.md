# 千峰HTML5+CSS3学习笔记

[TOC]

## 写在前面

- 学习链接：[千锋HTML5前端开发教程1000集](https://www.bilibili.com/video/BV17z4y1D7Yj)：`[1集: 183集]，共183集`
- 感想 | 摘抄
  1. 查询标签在各大浏览器中的兼容问题：[caniuse](https://caniuse.com/)
  1. 费曼学习技巧：以教促学
- 学习时遇到的问题

## 1. 前言

1. 居中：<center>居中文字</center>
2. WEB（网页）的组成部分
   1. HTML结构：W3C制定了机构HTML的语法、标准
   2. CSS表现：W3C制定了表现CSS的语法、标准
   3. JS行为：W3C、ECMA制定了行为标准（W3C DOM，ECMAScript）


## 2. HTML

1. 标记
   1. 常规标记，双标记
   2. 空标记，单标记

2. \<!DOCTYPE html>：特殊切固定的文档声明标签

3. hr：水平线

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/481287776acd4a3fbb51989a7d566c84.png)

4. 特殊符号

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/4c930e33814a4153aff45d477edf7a86.png)

5. div标签

   - 没有具体含义，用来划分页面的区域，独占一行。
   - 输入 `div*3` 可以直接键入三行div

6. span标签

   - 没有实际意义，主要应用在对于文本独立修饰的时候，内容有多宽就占用多宽的空间距离。

7. li标签

   - li里面可以随意放标签，但是ol里面只能放置li
   - 数字是自动生成的
   - params：
     - type：1，a，A，i，I
     - start：取值只能是一个数字

8. ul标签

   - 快捷创建：`ul>li{aaa}*3`
   - ul里面只能放li，li里面可以放其他标签
   - 默认是黑色的实心圆
   - params：
     - type：disc、circle、square、none（用得最多）

9. dl标签

   - 自定义列表
   - 主要用于图文混排
   - dl > dt+dd

10. 图片标签

    - 同级目录

      - 相对路径
        - `code.gif`
        - `./code.gif`
      - 绝对路径

    - 返回上一级后查找路径

      - `../code.gif`

    - 图片标签的属性

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/96edb97601244feba45f45c129f4fafc.png)

    - 宽高设置

      - 只设置一个属性：等比例缩放
      - 设置两个属性：按设置缩放

11. 超链接标签

    - 能够实现不同页面的跳转

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/1476e2b2e084446eaaa439bedbe6329e.png)

    - `target="_self"`：默认值，当前窗口打开

    - `target="_blank"`：新窗口打开

12. 表格：

    - 表格创建快捷键：`table>tr*3>td*3`

    - 表格属性：

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/92d5d46afb20466e94d61831d50ffa85.png)

    - 行tr的属性，table row

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/a2143eb56fbc499fa23cd9ce77e883b6.png)

    - 单元格td属性：table data

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/373ac438a19a4921a1b10a3cc11e37e4.png)

      - 如果一个单元格的设置宽度，影响的是这一整列的宽度
      - 如果一个单元格的设置宽度，影响的是这一整行的高度

    - 表格合并

      - 合并列：Colspan = 所要合并的单元格的 **列数** 必须给td
      - 合并行：Rowspan = 所要合并的单元格的 **行数** 必须给td

13. 表单标签

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/b6fce2cdab004fb884f2de5d678ae939.png)

    - form中method的post和get的区别

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/8d47d83b9c8d474c961f3a0d27f6d07b.png)

## 3. CSS

1. cascading style sheets，层叠样式表

2. 作用：修饰网页信息的显式样式

3. CSS语法：

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/68109782d4a84c0c905376dcad9faecc.png)

   ```css
   <style>
           h1 {
               color: red;
           }
           h2 {
               color: blue;
           }
   </style>
   ```

4. 内部样式表、外部样式表、行内样式表

















学到 P24


------

- :cloud: 我的CSDN：https://blog.csdn.net/qq_21579045
- :snowflake: 我的博客园：https://www.cnblogs.com/lyjun/
- :sunny: 我的Github：https://github.com/TinyHandsome
- :rainbow: 我的bilibili：https://space.bilibili.com/8182822
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友

