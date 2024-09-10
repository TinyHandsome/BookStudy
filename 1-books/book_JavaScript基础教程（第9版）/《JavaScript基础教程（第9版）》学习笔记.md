# 《JavaScript基础教程（第9版）》学习笔记

[TOC]

## 写在前面

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210717163123250.png)

- 读后感：



## 1. js基础

1. 数组：`var arr = new Array(1, 2, 3)`

2. 通过 `onmouseover` 和 `onmouseout` 实现图片的修改：

   ```html
   <a
       href="next.html"
       onmouseover="document.images['arrow'].src='images/arrow_on.gif'"
       onmouseout="document.images['arrow'].src='images/arrow_off.gif'"
       ><img src="images/arrow_off.gif" id="arrow" ➝alt="arrow"
   /></a>
   ```

3. 在图像标签中包含了 alt 属性：因为如果希望 HTML 符合 W3C 标准，就必须有 alt
   属性（这个属性为非图形化浏览器提供图像的名称或描述），而且使用 alt 属性有助于残障人士访问你的页面，比如用屏幕阅读器浏览页面的盲人用户

4. JavaScript 并不在意开发者使用哪种引号




















------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
