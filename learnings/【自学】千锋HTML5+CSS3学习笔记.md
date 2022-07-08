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

   - 外部样式的创建

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/24e7550bb3934b37b0569d95553e316e.png)

   - 外部css导入

     ```html
     <style>
             @import url(index.css);
     </style>
     ```

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/12d40b08bc854bcc9bcb3358e05feb11.png)

   - 行内

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/0ae9640c694e4d28b7b6bddc83c4db33.png)

   - **就近原则**：`!important` >行内>内部>外部

## 4. 选择器

1. 为什么要用选择器：

   要使用CSS对HTML页面中的元素实现一对一，一对多或者多对一的控制，这就需要用到CSS选择器

2. 元素选择器/类型选择器（element选择器），如：`div{width:100px; height: 100px; background:red;}`

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/2dab9f8f9e9e438d86473c03997ad3b7.png)

3. class选择器/类选择器

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/4807b887194844479fb0704dbf1f9424.png)

   - 优先级也是就近原则，这里就近只的是style定义的顺序，而不是class的继承顺序

4. id选择器

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/c563fa5863844e55bcab8c196cb705bd.png)

   - 不能给一个标签用上多个id

5. \* 通配符/通配符选择器

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/e0e569a6d2d543efbc796c278819b613.png)

6. 群组选择器：提出公共代码，节约代码量

   ```css
   div, p, h1, box1 {
               background-color: yellow;
           }
   ```

7. 后代选择器

   ```css
   div p {
               background-color: aqua;
           }
   ```

   - 底层查找逻辑：从右到左，先找子类，再找父类

8. 伪类选择器

   ![image-20220622152542175](E:\typora_pics_savepath\image-20220622152542175.png)

   - 需要遵循顺序编写

     ```html
     <style>
             a:link {
                 color: red;
             }
     
             a:visited {
                 color: aqua;
             }
     
             a:hover {
                 color: blue;
             }
     
             a:active {
                 color: coral;
             }
     </style>
     ```

   - link-visited-hover-active

9. 选择器的权重

   - 当多个选择器，选中的是同一个元素，且都为他们定义了样式，如果属性发生了冲 选择器的权重

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/17af9b2b8ab445e9b7ad6563b935fc65.png)

   - 包含选择器：子类选择器（嵌套的）的权重要大于普通元素的选择器


## 5. CSS属性

1. 文本属性

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/87f83d2aa8994b809811390f539bbbf5.png)

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/7f9db198b9b64b7e9ab6d8a88c8c789a.png)

   - 100：细体，lighter
   - 400：正常，normal
   - 700：加粗，bold
   - 900：更粗，bolder

2. 文本间距

   - 词间距，word-spacing：针对英文的词之间的间距
   - 字符间距，letter-spacing：字符与字符之间，文字与文字之间

3. 首行缩进，text-indent

   - 只对首行生效
   - 2em，指当前字体大小的2个字符

4. 文字装饰：

   - 下划线、上划线、删除线

   - 如果想要多条线

     ```css
     text-decoration: line-through underline overline;
     ```

5. 文本转换：text-transform，大写、小写，首字母大写

6. font：

   ```css
   .p_font {
               font: italic bold 20px/1em 微软雅黑;
           }
   ```

7. 列表属性

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/6a59b80f47d345cf8aca55929e096ce4.png)

   - 设置图片的话，需要对每一个li定义类，每个类设置不同的图片
   - list-style：合并写法

8. 背景属性

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/de6f46769d8b4839a3f6d899365e4e36.png)

   - 背景图片小于盒子大小：默认平铺效果

   - 背景图片大于盒子大小：裁剪显示左上角的部分

   - background-repeat：

     - repeat：默认平铺
     - repeat-x：x轴平铺
     - repeat-y：y轴平铺
     - no-repeat：不平铺

   - background-size：

     - 100px 100px
     - 100% 100%
     - cover：把背景图像扩展至足够大，以使背景图像完全覆盖背景区域，有一部分会被裁掉
     - contain：把图像扩展至最大尺寸，以使其宽度和高度完全适应内容区域，有一部分背景无法铺满

   - background-attachment：

     - 默认是scroll
     - 设置fixed可以制作视差效果

   - 背景属性的符合写法：

     1. 用空格隔开

     2. 顺序可以换

     3. **可以只取一个值，放在后面能覆盖前面的值**

     4. background-size属性只能单独用

     5. 顺序可以随便换

     6. 位置的顺序要贴着写，不能随便换

        ```css
        div {
                    width: 600px;
                    height: 600px;
                    /* background-color: yellow;
                    background-image: url(pics/马卡龙.png);
                    background-repeat: no-repeat;
                    background-position: center;
                    background-attachment: fixed; */
        
                    background: yellow url(pics/马卡龙.png) no-repeat center fixed;
                }
        ```

9. 浮动属性

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/d229161b838c46fbba82231338faad0b.png)

   - 作用：

     - 让竖着的东西横着来
     - 定义网页中的其他文本如何绕着该元素显示

   - 浮动是见缝插针的，能往下排就往下排，其次才会换行

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/c76f3d768cf04cfcb4c67f8299b04e3a.png)

10. 清浮动

    1. 写固定高度

    2. 清浮动的clear用法

       ![在这里插入图片描述](https://img-blog.csdnimg.cn/f292d5c017a24b259f8a5dc724345e69.png)

    3. 当前浮动元素后面补一个盒子，不设置宽高，clear:both

    4. overflow: hidden

       - 通过隐藏的bfc让浮动的元素计算高度

## 6. 盒子模型

1. 什么是盒子模型

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/e998ad0eb27f4852a02c50d3a3ea452f.png)

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/9c284a4ae5c344a9bc2cf16730993fa5.png)

2. padding：内边距

   1. 一个值，四个方向都一样
   2. 两个值，上下，左右
   3. 三个值，上 左右 下
   4. 四个值，上右下做
   5. 单独设置某一个方向的padding：`padding-left`，类似的，top、bottom、left、right
   6. padding不支持负数

3. border：边框

   1. 样式：
      - solid
      - double
      - dashed
      - dotted
   2. 背景色也能蔓延到边框，即boder压在bg-color上的
   3. boder属性拆分：
      - border-width
      - border-style
      - border-color

4. margin：外边距

   1. 支持多个方向一起写：`margin: 10px 20px 30px 40px;`
   2. 也支持属性拆分：
      - margin-top
      - margin-left
      - …
   3. 很多标签自带margin值，所以有时候会需要将margin设置为0
   4. 外边距支持设置负值，盒子往反方向移动
   5. 最快屏幕居中方案：`margin: 0 auto;`，上下为0，左右自动；上下auto是没有意义的
   6. 外边距的特性：
      - 兄弟关系，两个盒子垂直外边距与水平外边距的问题
        - 垂直方向上，外边距取最大值。
        - 水平方向上，外边距合并处理。
      - 父子关系，给子加外边距，但作用于父身上了，怎么解决
        - 方案1：子margin-top ==> 父的padding-top，注意高度计算
        - 方案2：给父盒子设置边框，transparent：透明
        - 方案3：加浮动，子和父都可以
        - 方案4：overflow:hidden，BFC


### 6.1 溢出属性

1. 溢出属性（容器的）

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/e39a01b7dabe4117b41adc1303c1de81.png)

2. 空余空间

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/3f8f68319604474b8f142d55dfadaa89.png)

   - nowrap：不换行
   - pre：显示空格、回车，不换行
   - pre-wrap：显示空格，回车，换行
   - pre-line：显示回车，不显示空格，换行

3. 省略号显示

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/b2d4995c5d5f4c8cb81c10937529a01b.png)

### 6.2 元素显示类型

1. 元素显示类型

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/3c7eec43d13e42de8759520393ff406b.png)

2. 块元素：

   - `display: block`
   - `display: list-item`
   - 独占一行显示
   - p标签放文本可以，不能放块级元素

3. 行内：

   - `display: inline`
   - 不能设置长宽
   - padding和margin只有左右有用，上下没用

4. 行内块:

   - 既能设置宽高，又能跟其他标签一起分享空间
   - `display: inline-block`
   - `img`、`input`

5. 元素类型互相转换：设置display属性

   - `display: none`，隐藏属性
   - 空格：子代选择器，`.item li`：子代中有li的都选中
   - \> ：亲代选择器，`.item>li`：只选择自己的亲儿子

6. 安利首页设计

   1. 版心
   2. 通栏
   3. 留白

7. 



































学到 P76


------

- :cloud: 我的CSDN：https://blog.csdn.net/qq_21579045
- :snowflake: 我的博客园：https://www.cnblogs.com/lyjun/
- :sunny: 我的Github：https://github.com/TinyHandsome
- :rainbow: 我的bilibili：https://space.bilibili.com/8182822
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友

