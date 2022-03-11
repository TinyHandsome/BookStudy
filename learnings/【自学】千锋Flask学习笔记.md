# 千锋Flask学习笔记

[TOC]

## 写在前面

- 学习链接：[Python 900集（学完可就业/2019版）](https://www.bilibili.com/video/BV15J411T7WQ)：`[359集: 451集]，共93集`

- 感想 | 摘抄

- 学习时遇到的问题
  - Flask用pycharm启动的时候无法按代码中的设置启动（debug设置为True也没辙）
  
  - 开发模式的环境配置在wsl的ubuntu中，bashrc和zshrc设置FLASK_ENV都没用，只有在windows的系统环境中配置了才有用
  
  - 使用 `python manage.py db init`没有迁移数据库，而是启动了服务器，并且还没有启动debug
  
    答：注意你 `manage.py` 中的主程序，是app不是manager吧憨憨~
    
  - 在使用sqlalchemy的order_by的时候报错：
  
    > sqlalchemy.exc.CompileError: Can't resolve label reference for ORDER BY ...
  
    答：这里需要给 `-id`加上一个text函数
  
    `Customer.query.order_by(text("-id")).first().id`
    
  - 更换flask为0.13.1之后报错：
  
    > ImportError: cannot import name 'import_string'
  
    答：werkzeug版本兼容问题，安装 `pip install werkzeug==0.15.2` 就行了


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
     - 使用过程
       - 安装
         - pip install flask-blueprint
       - 初始化
         - 需要创建蓝图对象
           - name
           - 导入名字 `__name__`
         - 需要使用app进行初始化
           - 注册在App上
       - 使用
         - 和Flask对象差不多
         - 直接作为装饰器用来注册路由

10. 数据库

    - Web开发中，大多数情况使用的都是关系型数据库
    - ORM
      - SQLAlchemy
    - flask-sqlalchemy
      - 使用过程
        - 安装
          - `pip install flask-sqlalchemy`
        - 初始化
          - 需要使用app进行SQLAlchemy对象的创建
            - 使用懒加载方式 init_app 方法搞定
          - SQLALCHEMY_DATABASE_URI
            - 连接数据库的路径
            - URI格式
              - 数据库+驱动://用户名:密码@主机:端口/库
          - SQLALCHEMY_TRACK_MODIFICATIONS
            - 将来被添加进来的一个特性
            - 默认是False
        - 使用
          - 定制模型
            - 继承自Model
            - 创建字段
          - 创建库，创建表
            - 库需要手动创建
            - 表
              - SQLAlchemy对象.create_all
              - 删除 .drop_all
              - 不能差量更新
          - 数据操作
            - 存储
              - 创建对象
              - SQLAlchemy对象.session.add()
              - 添加完成还要进行commit()
    - Flask-Migrate
      - 迁移插件
      - 在FLask中像Django中一样进行模型迁移
      - 使用流程
        - 安装
          - pip install flask-migrate
        - 初始化
          - 使用app和db进行初始化
          - 可以使用懒加载方式
        - 使用
          - flask db 指令
            - init
            - migrate
            - upgrade
          - 结合flask-script使用
            - 在manager添加一个管理指令
              - manager.add_command('db', MigrateCommand)
            - python manage db 指令

11. 二阶拆分

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

13. 项目结构

    - 原版
      - HelloFlask.py
    - 改良
      - 三阶改装
      - manage.py
        - 项目管理文件
      - App
        - `__init__`
          - 初始化文件
          - 天然的单例
          - 调用的顺序是最高的
        - settings
          - config
          - 全局项目配置
        - ext
          - extension 扩展库
          - 除了和路由相关
        - views
          - apis
          - 路由，视图函数
        - models
          - 定制模型

14. ODOO

    - 比django还重的Web框架
    - 可以快速生成网站

15. 三阶拆分

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/b6aee89dcafb44ae8674b930ed8f174a.png)

## 2. Views

1. 路由
   - 路由参数获取
   - <>
     - 语法：`<converter:name>`
     - converter
       - int
       - float
       - string
         - 以`/`作为结尾的
       - path
         - 从path修饰开始，后面的东西都是我们的
         - `/` 没有作用了
       - uuid
         - any

2. 视图函数
   - 默认支持GET、HEAD、OPTIONS
   - 其余请求不支持
   - 想支持其余请求需要手动注册

3. Flask有四大内置对象

   - Request
     - request
   - Session
     - session
   - G
     - g
   - Config
     - 在模板中config
     - 在python代码中，app.config

4. 小结

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/07fbd20a21354386b1e2d43097c251e4.png)

## 3. Request

1. args
   - 请求参数
   - query_string
   - query_params
   - get请求参数
   - 它并不是get专属，所有请求都能获取这个参数
2. form
   - 表单数据
   - post请求参数
     - 直接支持put，patch
3. ImmutableMultiDict
   - args和form都是这个类型
   - dict子类

## 4. Response

1. 创建Response的三种方式
   - 直接返回字符串
   - make_response
   - 直接构建Response
2. 参数设置
   - 内容
   - 状态码
3. render_template
   - 帮助把模板变成html字符串
4. 重定向
   - redirect
   - 反向解析：url_for
5. 终止处理
   - abort：本质上就是一个exception
   - HttpException：
     - 子类指定两个属性即可实现
     - code
     - description
6. 异常捕获
   - 可以提升程序交互
   - 让程序变得友好
   - 注册errorhandler

## 5. 会话技术

1. 跨请求共享数据

2. 出现原因

   - web开发中http都是短连接
   - http请求是无状态的
   - 请求从request开始，到response就结束了

3. Cookie

   - 客户端会话技术
   - 数据存储在客户端
   - key-value
   - flask中的cookie默认对中文等进行了处理，直接可以使用中文

4. Session

   - 服务端会话技术
   - 数据存储在服务器
   - key-value
   - flask中
     - 将session存储在cookie中
     - 对数据进行序列化
     - 还进行了base64
     - 还进行了zlib压缩
     - 还传递了hash
   - session的时间是31天

5. Token

6. flask-session

   - 实现了服务端session
   - 将数据存储在服务端，将数据对应的key存储在cookie中
   - RedisSessionInterface
     - save_session：将数据进行了pickle序列化

7. flask-bootstrap

   - bootstrap/base.html
     - html_attribs：给整个html添加属性
     - html
       - head
         - title
         - metas
         - styles
       - body_attribs
         - body
           - navbar：导航条
           - content：内容
           - scripts

8. 小结

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/9ee64384a3b84142880e45b37f2081e8.png)

## 6. 模型和模板

1. 模板路径默认在Flask(app)创建的路径下

2. 如果想自己指定模板路径
   - 在Flask创建的时候，指定template_folder
   - 在蓝图创建的时候，也可以指定template_folder
   - 蓝图指定此蓝图同意前缀：`/xxx`
   - 模板中使用反向解析和在Python代码中一样
     - url_for

3. 静态资源
   - 静态资源在flask中是默认支持的
   - 默认路径在和flask同级别的static中
   - 想要自己指定
     - 可以Flask创建的时候指定 static_folder
     - 也可以在蓝图中指定
   - 静态资源也是有路由的
     - endpoint是static
     - 参数有一个filename
   - `{{ for_for('static', filename='xxx') }}`

4. flask-debugtoolbar
   - 从Django中借鉴
   - 样式基本一致
   - 使用方式更简单
     - 安装
     - 使用app初始化

5. 模型
   - 约束
   - 模型信息指定
     - 表名映射
       - \__tablename__
     - 模型继承
       - 默认继承并不会报错，它会将多个模型的数据映射到一张表中，导致数据混乱，不能满足基本使用
       - 抽象的模型是不会在数据库中产生映射的
         - \__abstract__ = True
   - 文档
     - falsk-sqlalchemy
     - sqlalchemy
   - 项目中数据库优化
     - 怎么连接
     - 连接多少个
     - django和flask
       - 默认都是有数据库连接池的
   - 数据查询
     - 获取单个对象
       - first
       - get
       - get_or_404
     - 获取结果集
       - all
         - 特殊、特例
         - 列表：list
       - filter
         - BaseQuery对象
           - \__str__ 输出的是这个对象数据的SQL
         - 条件
           - 类名.属性名.魔术方法(临界值)
           - 类名.属性名  操作符运算符  临界值
           - contains
           - startswith
           - endswith
           - in_
           - link
           - \__gt__
           - \__ge__
           - \__lt__
           - \__le__
         - 筛选
           - filter_by()
           - offset()
           - limit()
           - order_by()
           - get()
           - first()
           - paginate()
           - offset和limit不区分顺序，都是先执行offset
           - order_by调用必须在offset和limit之前
         - 与或非
           - \_and
           - \_or
           - \_not
       - filter_by
         - 用在级联数据上
         - 条件语法精准
         - 字段 = 值
       - 级联数据
         - 获取
           - 手动实现获取
           - 使用关系 relationship 进行级联查询
             - 反向引用
         - 关系
           - 1:1
             - ForeignKey + Unique
           - 1:M
             - ForeignKey 
           - M:N
             - 额外关系表
             - 两个 ForeignKey 
       - 筛选在flask-sqlalchemy中，all如果使用，只能放在最后

6. 小结

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/14701a9a481f47d595f2d79556ef7466.png)

## 7. 数据传输加密反爬

1. 爬虫
   - 数据获取
   - 数据提取
   - 数据存储
2. 反爬
   - 数据加密反爬
   - 在服务端对数据进行特定算法的加密
   - 在客户端进行数据的解密
     - 浏览器还是可破解的
     - Android或IOS移动端，破解率基本为零









学到 P35


------

- :cloud: 我的CSDN：https://blog.csdn.net/qq_21579045
- :snowflake: 我的博客园：https://www.cnblogs.com/lyjun/
- :sunny: 我的Github：https://github.com/TinyHandsome
- :rainbow: 我的bilibili：https://space.bilibili.com/8182822
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
