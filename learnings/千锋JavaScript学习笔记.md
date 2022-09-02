# 学习笔记

[TOC]

## 写在前面

- 封面 | 摘要

  

- 学习链接

- 感想 | 摘抄

- 学习时遇到的问题

- 直通车

- <span style="color: skyblue; font-weight: bold">PS：相关工程代码都在 Github 上</span>

## 1. JS基础

1. js实际上是两种语言风格的混合产物，简化的函数式编程和简化的面向对象编程

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/4af87e8485da4f91b0472e8d6981b39c.png)

2. JS决定行为

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/3887e4a783b140cc8267d0601dfd14ad.png)

3. JS的三大核心组成

   - BOM：Browser Object Model，JS操作浏览器发生变化的属性和方法
   - DOM：Document Object Model，JS操作文档流发生变化的属性和方法
   - ECMAScript：JS的书法语法和书写规则

4. JS的书写位置

   - 行内式：直接把代码书写在标签身上

     **强烈不推荐，既不利于代码的维护，也会导致html文件臃肿**

     - a标签：书写在href属性上

       `<a href="javascript: alert('hello world');">点我一下</a>`

     - 非a标签：书写在行为属性上

       `<div onclick="alert('hello world')">点我一下</div>`

   - 内嵌式：把代码书写在一个 script 标签对内

     **不是很推荐**

     ```html
     <script>
     	alert('hello world');
     </script>
     ```

   - 外链式：把代码书写在一个.js文件内

     `<script src="helloworld.js"></script>`

     **最推荐的书写方式**

5. 变量

   - 变量赋值：`var num = 100`

   - 小结：

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/842d5d3ec7794bf0bb2cf3ac4eddf5a9.png)

   - 单行注释：`//`

   - 多行注释：`/* 注释内容 */`

   - 几个在浏览器中输出的方式

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/ced422a5985e45688c3631017b04a7e3.png)

6. 数据类型

   - 数值类型

     - 科学计数法：`2e5=2x10^5`

     - 进制：

       ![在这里插入图片描述](https://img-blog.csdnimg.cn/03152ceafda14c018d89a29e567cf7e6.png)

     - js中的数据

       ![在这里插入图片描述](https://img-blog.csdnimg.cn/7e86400763eb48cbb47dd62d518880da.png)

   - 字符串：不区分单引号和双引号

   - 布尔类型：true，false

   - 空类型：

     - null：表示有值，有一个空值：`var k1 = null`
     - undefined：表示没有值：`var k2`

   - 使用 `typeof` 关键字来进行数据类型检测，语法：`typeof` 要检测的变量；结果：该变量存储的数据的数据类型

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/d173b74e689142a7ba747ad445c040db.png)

   - 小结：

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/a8f56398a13d4be2bc6fae30e0ba604b.png)

7. 数据类型转换

   - 转数值

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/2e4861953ffb49079a8e31964c4574a8.png)

     - Number就是直接全部转，行就行，不行就NaN
     - parseInt是从前往后扫描，如果是数就要，不是就结束了，如果开始都不是数，就直接NaN
     - parseFloat是可以识别小数，其他的都是只能转化整数

   - 转字符串

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/f29f393510204c4294641580de8a502d.png)

     - 没有特别要注意的地方，就是两种方式的语法不同

   - 转布尔

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/590a84617f3b4f3bbe02629b32e5324c.png)

     - 只有5个值会被转为false，其他的都会被转为true

   - 小结：

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/56ecc4d836c9460f8e9d6ab691be1834.png)

8. 运算符

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/2c9933a99f7144c9b6b36c5b845304b2.png)

   - 算数运算符：进行 数学运算 的符号

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/1c815aee27184fe09629edbaf8940f90.png)

   - 赋值运算符：进行 赋值操作 的符号

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/b81f9787516640798ad9a8fb8fb69e9a.png)

   - 比较运算符：进行 比较运算 的符号

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/7c04b304d4f8473187c78a854c4df36e.png)

   - 逻辑运算符：进行 逻辑运算 的符号

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/d586c4b860c14d76800a21688f182419.png)

   - 自增自减运算符：单独对一个变量进行 +1 或者 -1 操作的符号

     基本跟C语言一样，++和--

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/89de15117df84465ab5367d7cab4216c.png)

   - 小结

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/68906d095ddc4c459a4054cf332df050.png)

9. 条件分支语句

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/0c3c8ddfeb184af9b959bfefcffa6032.png)

10. 案例1：平年还是闰年？

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/2ed60430ab3a47b38163711d67c08ed5.png)

    ```js
    var year = 2004
            
    if (year % 4 == 0 && year % 100 !=0 || year % 400 == 0) {
        console.log(year + '是闰年')
    } else {
        console.log(year + '不是闰年')
    }
    ```

11. 条件分支语句

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/a2208d4e33674b1ea7805f27c1a171dc.png)

    - 记得满足条件的执行逻辑中需要加入break

    - 最后可以加一个default，如果所有选项都不匹配时，则执行default

    - 小结：

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/85003c6d0cf547eda412bbb6d3b82f7f.png)

12. 案例2：一年中的第几天

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/f760d96430834e33a2eabfac3a45eeb4.png)

13. 循环结构语句

    - while

        ![在这里插入图片描述](https://img-blog.csdnimg.cn/30b95cbcd9604550ac315fc0b9d8ef8f.png)

        - 小结：

          ![在这里插入图片描述](https://img-blog.csdnimg.cn/76c091527787488490f1ae3edb47ab5f.png)

    - dowhile;

        ![在这里插入图片描述](https://img-blog.csdnimg.cn/f7c136d8e2d3481099d727e9b944dabb.png)

    - for

        ![在这里插入图片描述](https://img-blog.csdnimg.cn/549f713dd8b14171ab5f86f959aed855.png)

        ```js
        for (var i = 0; i < 3; i ++) {
            console.log('啊吧啊吧' + i)
        }
        console.log('完事儿了')
        ```

        



























学到P198


------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
