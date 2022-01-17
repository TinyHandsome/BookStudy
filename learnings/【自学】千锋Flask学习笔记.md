# 千锋Flask学习笔记

[TOC]

## 写在前面

- 学习链接：[Python 900集（学完可就业/2019版）](https://www.bilibili.com/video/BV15J411T7WQ)：`[359集: 451集]，共93集`
- 感想 | 摘抄
- 学习时遇到的问题

## 1. Flask介绍

1. Flask是一个基于Python实现的Web开发 “微”框架 
2. Flask跟Django一样，也是一个基于MVC设计模式的Web框架
3. Flask依赖三个库：
   - Jinja2 模板引擎
   - Werkzeub WSGI工具集
   - Itsdangerous 基于Django的签名模块
4. 参数配置：在启动的时候还可以添加参数，在run()中：
   - debug：是否开启调试模式，开启后修改过python代码会自动重启
   - threaded：是否开启多线程
   - port：启动指定服务器的端口号
   - host：主机，默认是127.0.0.1，指定为0.0.0.0代表本机所有ip
5. debugger：
   - Flask中调试器拥有保护功能
   - PIN
   - 如果需要在页面中进行调试，需要输入PIN码进行确认
6. Linux
   - 环境变量
     - 系统级
       - /etc/environment
       - /etc/profile
     - 用户级
       - ~/.bashrc
     - 临时级
       - 在窗口中直接export













学到 P3 09 49


------

- :cloud: 我的CSDN：https://blog.csdn.net/qq_21579045
- :snowflake: 我的博客园：https://www.cnblogs.com/lyjun/
- :sunny: 我的Github：https://github.com/TinyHandsome
- :rainbow: 我的bilibili：https://space.bilibili.com/8182822
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
