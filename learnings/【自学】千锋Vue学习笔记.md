# 千锋Vue学习笔记

[TOC]

## 写在前面

- 封面 | 摘要 | 关键词

  ![首页](https://img-blog.csdnimg.cn/c944cb785bb946898ed1a018ad717104.jpeg)

  千锋Vue学习笔记

  ```
  Vue
  李英俊
  前端
  千锋
  ```

- 学习链接

- 感想 | 摘抄

- 学习时遇到的问题

- 直通车

- <span style="color: skyblue; font-weight: bold">PS：相关工程代码都在 Github 上</span>

## 1. 前言

1. Vue是通过拦截变量的get和set方法，来进行监听和更新的
2. `Object.defineProperty`有以下缺点：
   1. 无法监听es6的Set、Map变化
   2. 无法监听Class类型的数据
   3. 属性的新加或者删除也无法监听
   4. 数组元素的增加和删除也无法监听
3. `:src`、`:class`这样的写法的完整写法是：`v-bind:src`
4. 同理，事件 `@click`绑定的完整写法是：`v-on:click`














------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045/`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome/`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822/`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj/`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_/`
- :potato: 我的豆瓣：`https://www.douban.com/people/lyjun_/`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
