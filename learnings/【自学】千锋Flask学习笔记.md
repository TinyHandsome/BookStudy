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

## 8. 钩子函数

1.  面向切面编程
   - 动态介入请求流程
   - before_request
   - after_request
2. Django请求流程
   - urls -> views
   - views -> models
   - models -> views
   - views -> response
3. 添加中间件
   1. client -> process_request: list
   2. 逐一进行process_request
   3. process_request -> urls
   4. urls -> process_view: list
   5. 逐一进行process_view
   6. process_view -> views
   7. views -> models
   8. models -> views
   9. views -> response
   10. response -> process_response: list
   11. 逐一进行process_response
4. 四大内置对象
   1. request
   2. session
   3. g
      - 跨函数传递数据
      - 设置全局变量
   4. config (app)
      - python flask：current_app.config
      - 一定是在项目启动之后

## 9. 用户激活、手机、邮箱

1. 用户激活
   - 邮箱
     - 异步发送邮件
     - 在邮件中包含激活地址
       - 激活地址接收一个一次性的token
       - token是用户注册的时候生成的，存在了cache中
       - key-value
         - key：token
         - value：用户的一个唯一标识
   - 短信
     - 同步操作

2. 小结

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/5af84a7ffa084a9a85fec236b9ad5cbc.png)

## 10. Flask-RESTful

1. 输出
   - 默认输出字典，可以直接进行序列化
   - 如果包含对象
     - 默认会抛出异常，对象不可JSON序列化
   - 使用格式化工具
     - marshal 函数
     - marshal_with 装饰器
     - 条件
       - 格式
         - 字典格式
         - 允许嵌套
         - value 是 fields.xxx
       - 数据
         - 允许任何格式
       - 如果格式和数据完全对应，数据就是预期格式
       - 如果格式比数据种的字段多，程序以然正常运行，不存在的字段是默认值
       - 如果格式比数据中的字段少，程序正常执行，少的字段不会显示
       - **以格式的模板为主**
     - 结论
       - 想要什么格式的返回
       - 格式工具（模板）就是什么样的
       - 和传入的数据没什么直接关系
     - 格式和数据的映射
       - 格式中的字段名和数据中的字段名需要一致
         - 也可以手动指定映射 
         - `attribute='property_name'`
       - 也可以对属性指定默认值
         - default
         - 指定默认值，值传递使用传进来的值
         - 未传递，则使用默认值
     - fields
       - Raw
         - format
         - output
         - 调用
           - 将数据传递进格式化工具的时候，先获取值 output
           - 再对值进行格式化 format
       - String
         - 继承Raw
         - 将value进行格式化
         - 转换成兼容格式的text
       - Integer
         - 继承自Raw
         - 重写了初始化，将default设置为0
         - 重写格式化，直接将value转换成int
       - Boolean
         - 继承自Raw
         - 重写格式化，直接将 value 转换成 bool
       - Nested
         - 继承自Raw
         - 重写output
         - 进行marshal
       - List
         - 继承自Raw
         - 重写了output
           - 判断你的类型
           - 对不同的类型进行不同的处理
             - dict 直接进行处理
             - list 迭代处理
         - 重写format
           - 进行格式化

2. 输入

   - RequestParser
     - 使用过程
       - 先定义一个RequestParser对象
       - 向对象中添加字段
       - 从对象中获取字段
     - 对象在添加参数的时候，可以实现数据的预校验
       - 参数是否必须
       - 数据的类型
       - 还可以设置错误提示
       - 接收多个值： action="append"
       - 也可以接收指定别名
       - location可以指定参数的来源
         - 可以配合 action="append"一起用
         - 获取多个来源的同名变量

3. 爬虫与反爬虫

   - 基于IP频率反爬
     - 客户端使用代理服务器
   - 基于UA的反爬
     - 使用UA池
   - 基于Cookie或用户反爬
     - Cookie池
     - 登录大量账号，存储cookie

4. 小结

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/0e406c284a684ae3b7e49d1318775af3.png)

## 11. 公司组成、项目架构

1. 公司

    - 找工作的途径
      - 投递简历
        - 至关重要
        - 一定要自己写
      - 内推
    - 人力
      - 人力资源
        - 人员招聘
        - 员工考核
        - 社保公积金
        - 员工关系
        - 薪资管理
    - 行政
      - 打杂的
      - 收发快递
      - 接待访客
      - 交物业水电
      - 拉拉网线
      - 设备采购
    - 技术
      - 产品经理
        - PRD
      - 项目经理 | 技术经理 | CTO
      - UI（UD、UE）
      - DBA数据库工程师
        - 后端
        - 移动端
        - 数据分析
      - 数据分析师
        - 爬虫
          - 金融量化交易
          - 信息采集
      - 后端
        - Web
      - 前端
        - HTML
        - 移动端
      - 测试
        - 黑盒测试
        - 白盒测试
      - 运维
    - 财务
      - 发工资
        - 工资构成
          - 全额缴税和五险一金
            - 不超过10%（北京）
          - 基本工资 + 津贴 + 报销款
          - 基本工资 + 绩效 + 现金
    - 运营推广
      - 网络推广
        - 百度竞价
        - 各大IT论坛贴吧
      - 线下推广
        - 地铁推广
        - 去指定区域推广
        - 小区推广
      - 口碑运营（公关）
    - 销售
      - 渠道
      - 线上销售
        - 网络销售
        - 电话销售
      - 线下销售
        - 实体店
        - 体验店
        - 院校
        - 班主任
    - 售后
      - 客服
      - 就业老师
      - 品保
        - 班主任
        - 就业老师
        - 教务
          - 稽查
          - 回访电话
    - 法务
      - 律师团队
2. 开发流程
    - 产品
    - 开会讨论
    - 架构
      - 框架选型
    - 数据库开始
3. 加班
    - 弹性制工作
      - 晚到晚走
      - 最近比较忙，需要加班
        - 吃饭、交通
        - 加班费
        - 加班有统计，可以调休
      - 996
        - 早9晚9上6天
4. 公司
    - 常规公司
      - 通过融资进行发展的公司
    - 外包公司
      - 驻地开发
        - 出差
      - 在自己公司开发
    - 国企
5. 公司发展历程
    - 天使投资
      - PPT产品
      - 固定页面的产品
    - A轮
      - 扩大规模
    - B轮
      - 优化产品
      - 占领市场
      - 对赌
    - C轮
    - D轮
    - E轮
    - IPO上市
6. 工资
    - 期权
    - 股权

## 12. 淘票票

1. 开发
    - 淘票票
    - 端
      - 淘票票后端
        - 淘票票公司自己管理
      - 客户端
        - 看电影用户准备的
      - 影院端
        - 电影放映

2. 通用模块
    - 用户体系
      - 用户权限
      - 用户角色
    - 电影
      - 淘票票后端
        - 增删改查
      - 淘票票影院端
        - 查询
      - 淘票票客户端
        - 查询
    - 排挡
      - 淘票票后端
        - 增删改查
      - 影院端
        - 增删改查
      - 客户端
        - 查
    - 影票
      - 淘票票后端
        - 增删改查
      - 影院端
        - 增删改查
      - 客户端
        - 增删查

3. 可扩展
    - 优惠券
    - 积分系统
    - 影院会员系统
    - 评价系统
    - 套餐
    - 定位（手机、浏览器）
    - 地址
      - 后端规划好
      - 影院端添加

4. 多个接口拥有通用功能

    - 如何复用代码
      - 装饰器
      - 钩子函数
      - 直接封装一个函数
      - 创建一个父类

5. 淘票票后端
      - 管理淘票票用户
      - 淘票票影院管理
      - 电影

6. 淘票票影院端
        - 后端购买来的电影播放权
          - 电影
        - 放映厅
        - 排挡
          - 关系表
          - 电影和放映厅 + 时间

7. 淘票票客户端
        - 查看电影
        - 查看影院
        - 查看排挡
        - 下单
          - 找到具体排挡
          - 选座（座位锁定），并发处理
            - 订单过期
          - 支付

8. 项目架构

       - 一个项目入口
         - App/\__init__
         - apis
           - admin
           - movie_admin
           - movie_user
         - models
           - admin
           - movie_admin
           - movie_user
       - 另外一种架构
         - FlaskTpp
           - \__init__
           - settings
           - ext
         - Admin
           - apis
           - models
         - MovieAdmin
           - apis
           - models
         - MovieUser
           - apis
           - models

9. 系统设计

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/85ae54059a834df2afe4d78ea18a1694.png)

       - 客户端
         - 用户系统
           - 字段
           - username
           - password
           - phone
           - email
           - is_delete
           - permission
         - 权限设计
           - 类似于linux权限设计
             - 精髓，一个字段可以代表多种权限
             - 还能分成两种
               - 完全和linux中一样
                 - 使用二进制
                 - 所有的初始权限值都是2的n次幂
               - 只是给一个数值
                 - 数值越大，权限越高
                 - 数值大的包含数值小的所有权限
           - 多表设计权限系统
             - 用户表
             - 权限表
             - 用户权限表

10. Linux权限设计

        ![在这里插入图片描述](https://img-blog.csdnimg.cn/56ffb1c69bd34f64ac08af43794913bb.png)

11. FlaskTpp

          1. 开发流程
             - 产品经理提出需求
             - 开会，评审
             - 要添加的功能，周期（时间）
             - 数据设计
               - DBA
               - 架构师
               - 后端经验丰富的工程师
               - 自己设计
             - 建库建表
               - 模型建立
             - 对数据进行操作
               - CRUD
               - 和前端联调
                 - 前端需要请求接口
                 - 接口对接
                   - API文档
                   - 接口功能
                   - 接口地址
                   - 接口所需参数
                     - 哪些是必须的，哪些是非必须的，哪些是通用参数
                   - 接口返回数据类型
                     - 数据字段
                     - 状态码
                     - 错误码
             - 设计操作的权限
               - 登录才能操作
               - 权限级别
             - 送测
               - 测试工程师会有bug反馈
             - 修复bug
               - 送测
             - 上线

12. 端

          - 一个项目至少有两端
            - 一端用户端
            - 后台管理端
          - 大部分项目都是有三端的
            - 用户端
              - Web
              - 移动端
                - Android
                - IOS
              - 微信端
            - 商家端
              - Web
              - 移动端
                - Android
                - IOS
              - 微信端
            - 后台管理端
              - Web
              - 移动端
                - Android
                - IOS
              - 微信端
          - 我们实现使用RESTful
            - 用户端的接口
              - 不需要再关注展示端的具体实现
            - 商家端的接口
            - 后台管理接口

13. Property

          - 将函数转换成属性
          - 动态干预数据的存取

14. 权限

         - 两种设计
            - 单个字段实现所有权限
              - Linux：高格调权限设计
                - 使用二级制实现
                - 每一种权限使用一个不重复的二进制确定
                  - 2的n次幂的值
                - 优点
                  - 各种权限互不干扰
            - 包含模式权限
              - 值越大权限越多，包含值小的所有权限
         - 多表实现权限
            - 用户表
            - 权限表
            - 用户权限表（用户表和权限表多对多的关系）

15. 装饰器

         - 面向切面编程的一部分
         - 再不修改原代码的情况下，添加功能、逻辑控制
         - 装饰器上内部参数
           - \*args：用来接收位置参数
             - 关键字参数默认值可以自动处理
             - 如果传递关键字参数，就需要我们自己处理
               - 接收参数
               - 传递参数
           - \**kwargs：用来接收关键字参数
           - 如果原函数拥有返回值
             - 默认只有调用的话，返回值会被丢弃
             - 想接收返回值，要进行数据的返回

16. 权限系统

        - Linux
        - 权限分类
          - 1：读权限
          - 2：写权限
          - 4：修改权限

17. 特殊登陆

        - 扫码登录
          - 前置条件
            - 有一个登录好的账号
          - 使用登录好账号中的token来访问自己的登录接口
            - 常规登录接口
              - 用户名
              - 密码
              - 手机号
              - 邮箱
            - 特殊登录接口
              - 直接可以通过token进行登录
            - 扫码扫出来的就是那个特殊的登录接口
        - 跨应用登录
        - 第三方登录

18. 城市导入脚本

        - 获取城市信息
        - 将城市信息读出来
        - 插入数据库中

19. 项目目前状况

       - 三端划分
         - 客户端
         - 商家端
         - 后台管理
       - 客户端
         - 用户模块
           - 注册登录
           - 信息修改
           - 用户删除（不允许）
           - 权限
       - 商家端
         - XXX
       - 后端
         - XXX
       - 通用
         - 地址管理

20. 电影

       - 电影属于哪个公司
       - 演员
       - 操作
         - CRUD
           - C
             - 应该只有后台登录的管理员能创建
             - token认证
               - 会出现多个端token混乱
               - 不同token对应相同的id值
               - 解决方案：
                 - token 添加前缀或后缀
                 - 修改表结构，user_id的值是字符串，里面存uuid

21. 电影公司

22. 演员表

23. 接下来

       - 电影模块
         - 电影哪来的（后端）
       - 后端
         - 用户实现（淘票票管理系统）
         - 可以实现电影的增删改查
       - 客户端就可以实现电影查询
       - 查询电影院（影院端）
         - 用户实现（影院端）
         - 获取电影列表
         - 购买电影播放权

24. 再之后

       - 电影院有排挡
       - 用户浏览具体排挡下单
       - 票房排行
         - 统计电影卖的所有的票的总和
         - 电影
           - 排挡
             - 订单
               - 价钱
       - 热度排行















学到 P69 1026


------

- :cloud: 我的CSDN：https://blog.csdn.net/qq_21579045
- :snowflake: 我的博客园：https://www.cnblogs.com/lyjun/
- :sunny: 我的Github：https://github.com/TinyHandsome
- :rainbow: 我的bilibili：https://space.bilibili.com/8182822
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
