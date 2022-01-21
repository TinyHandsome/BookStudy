# 千锋Flask学习笔记

[TOC]

## 写在前面

- 学习链接：[Python 900集（学完可就业/2019版）](https://www.bilibili.com/video/BV15J411T7WQ)：`[359集: 451集]，共93集`
- 感想 | 摘抄
- 学习时遇到的问题
  - Flask用pycharm启动的时候无法按代码中的设置启动（debug设置为True也没辙）
  - 开发模式的环境配置在wsl的ubuntu中，bashrc和zshrc设置FLASK_ENV都没用，只有在windows的系统环境中配置了才有用


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

7. Flask-Script

   - 可以添加Flask脚本的扩展库
   -  添加命令行参数
   - 使用
     - 安装：pip install flask-script
     - 初始化：使用app构建Manager对象
     - 调用：
       - runserver
         - -d：调试模式
         - -r：自动重试加载
         - -p：port（`0.0.0.0`代表所有端口）
         - -h：host
         - --threaded：开启多线程模式
       - shell

8. 简单的一阶程度拆分

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/e942ba599a25454f87023f5099610dce.png)

9. 路由的管理

   - 使用的时候容易出现循环应用的问题
   - 使用懒加载的方式
     - 使用函数调用的形式进行加载
   - 使用新方案解决
     - 蓝图
       - 代表的一种规划
     - 路由的规划
   - flask-blueprint

10. 数据库

    - Web开发中，大多数情况使用的都是关系型数据库
    - ORM
      - SQLAlchemy
    - flask-sqlalchemy

11. 关系图

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/f3ae1c050b34428b9454b98c66246823.png)

12. 公司开发环境

    - 开发环境
      - 开发人员使用
    - 测试环境
      - 测试人员使用
    - 演示环境
      - 给产品看的
      - 做演习、彩排
    - 生产环境、线上环境
      - 真实环境
      - 给用户看的













学到 P8


------

- :cloud: 我的CSDN：https://blog.csdn.net/qq_21579045
- :snowflake: 我的博客园：https://www.cnblogs.com/lyjun/
- :sunny: 我的Github：https://github.com/TinyHandsome
- :rainbow: 我的bilibili：https://space.bilibili.com/8182822
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
