# 《HTML5与CSS3基础教程（第8版）》学习笔记

[TOC]

## 写在前面

- 封面

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/d9c892fdaa8f4b82a822f12eb2b93e17.png)

- 读后感
- 传送门

## 1. 网页的构造块

1. 渐进增强（progressive enhancement）：

   - 不是一门语言，而是一种建站方法，它由Steve Champeon于2003年提出
   - 这个想法很简单，但也很强大：
     - 开始用所有人都能访问的HTML内容和行为构建网站
     - 再用CSS加入你的设计
     - 最后用JavaScript（一种编程语言）添加额外的行为。
     - 这些组件都是分离的，但可以同时发挥作用。

2. 元素

   - 元素由开始标签、内容和结束标签组成

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/94f399cf3b764dc190251b6677c006f0.png)

   - 还有一些元素是空元素（empty element或void element），既不包含文本也不包含其他元素

   - 它们看起来像是开始标签和结束标签的结合，由左尖括号开头，然后是元素的名称和可能包含的属性，然后是一个可选的空格和一个可选的斜杠，最后是必有的右尖括号

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/33d04ea5e7bc4fb5815dc59146ba4160.png)

   - *XHTML 要求空元素结尾处必须有斜杠*

3. 属性和值

   - 属性包含了元素的额外信息

   - 在HTML5 中，属性值两边的引号是可选的，但习惯上大家还是会写上，因此建议始终这样做

   - 属性总是位于元素的开始标签内，属性的值通常放在一对括号中

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/36a451fa5bf947c4adc84324c67c4168.png)

   - 有的元素可以有多个属性，每个属性都有各自的值。

   - 属性的顺序并不重要

   - 不同的属性– 值对之间都用空格隔开

   - 有的属性可以接受任何值，有的则有限制

   - 最常见的还是那些仅接受预定义值（也称为枚举值）的属性

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/e4e56dc9714b495f9f0fe4b89d6adb9e.png)

   - 布尔属性（Boolean attribute）：

     - 这种属性的值是可选的，因为只要这种属性出现就表示其值为真

     - 如果一定要包含一个值，就写上属性名本身

       ![在这里插入图片描述](https://img-blog.csdnimg.cn/f417092defce453bb3228ab67cfca8a9.png)

4. 父元素和子元素

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/1c21856c85c146fb86109fbb5c17d021.png)

5. 规则：

   1. 文件名全部使用小写字母，用短横线分隔单词，用 .html 作为扩展名；混合使用大小写字母会增加访问者输入正确地址以及找到页面的难度

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/4f55c72fdb19419c9ebce6902e02335b.png)

   2. 文件名采用小写字母

   3. 使用正确的扩展名

   4. 用短横线分隔单词

6. URL：Uniform Resource Locator，统一资源定位符

   1. URL 的第一个部分称为模式（scheme）

      - 模式告诉浏览器如何处理需要打开的文件

      - 最 常 见 的 模 式 是 HTTP（Hypertext Transfer Protocol，超文本传输协议）

        ![在这里插入图片描述](https://img-blog.csdnimg.cn/0b6619d09f544b8e91047ff6f807bfed.png)

   2. 对于 FTP 站点以及几乎所有不使用 HTTP 协议的 URL，都应该使用绝对 URL

   3. 绝对 URL 和相对 URL 的比较

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/9a6de0b292b5488db757ac2676503027.png)

7. ftp：File Transfer Protocol，文件传输协议





















学到  11


------

- :cloud: 我的CSDN：https://blog.csdn.net/qq_21579045
- :snowflake: 我的博客园：https://www.cnblogs.com/lyjun/
- :sunny: 我的Github：https://github.com/TinyHandsome
- :rainbow: 我的bilibili：https://space.bilibili.com/8182822
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友

