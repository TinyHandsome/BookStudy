# 《Flask Web开发——基于Python的Web应用开发实战》学习笔记

[TOC]

## 写在前面

## 1. 安装

- Flask有3个主要依赖：路由、调试和Web服务器网关接口（WSGI，Web Server Gateway Interface）
- 创建虚拟环境：`python -m venv venv`
- 激活虚拟环境：`venv\Scripts\activate`
- 关闭虚拟环境：`deactivate`
- 查看虚拟环境中安装了哪些包：`pip freeze`

## 2. 应用的基本结构

- **路由**：处理URL和函数之间关系的程序成为路由。

- 装饰器是python语言的标准特性。常用的方法是把函数注册为事件处理程序，在特定的事件发生时调用。

- 启动应用：

  1. 激活虚拟环境

  2. 设置环境变量和运行

     ```
     set FLASK_APP=E:\【冲鸭】\【学习】1. 代码代码代码冲冲冲\book5\hello.py
     flask run
     ```

- 也可以通过编程的方式启动：

  ```python
  from flask import Flask
  
  app = Flask(__name__)
  
  
  @app.route('/')
  def index():
      return '<h1>Hello World!</h1>'
  
  
  @app.route('/user/<name>')
  def user(name):
      return '<h1>Hello, {}!</h1>'.format(name)
  
  
  if __name__ == '__main__':
      app.run()
  ```

- 调试模式：`set FLASK_DEBUG=1`

- 用编程的方法启动调试模式：`app.run(debug=True)`

- 请求钩子：

  - `before_request`：注册一个函数，在每次请求之前运行
  - `before_first_request`：注册一个函数，只在处理第一个请求之前运行。可以通过这个钩子添加服务器初始化任务
  - `after_request`：注册一个函数，如果没有未处理的异常抛出，在每次请求之后运行
  - `teardown_request`：注册一个函数，即使有未处理的异常抛出，也在每次请求之后运行

## 3. 模板

- 使用**flask_bootstrap**集成Bootstrap
- 视图函数的作用：生成请求的响应
- 自定义错误页面：
  1. 404：客户端请求未知页面或路由时显示
  2. 500：应用有未处理的异常时显示
- 链接：`url_for()`
- 使用**flask-moment**本地化日期和时间

## 4. Web表单

- 使用**flask-wtf**处理Web表单
- flask-wtf需要应用配置一个密钥，目的是为了防止表单遭到跨站请求伪造。
- `StringField`类表示属性为`type="text"`的`HTML<input>`元素
- `SubmitField`类表示属性为`type="submit"`的`HTML<input>`元素
- `POST/重定向/GET模式`：使用重定向作为POST请求的响应
- 字典取值时使用`get()`可以避免未找到键时抛出异常，若不存在，则返回默认值None

## 5. 数据库

- NoSQL数据库：文档数据库和键-值对数据库合称

- 关系型数据库采用一种称为ACID的范式：

  - atomicity（原子性）
  - consistency（一致性）
  - isolation（隔离性）
  - durability（持续性）

- Python数据库框架：**Flask-SQLAlchemy**

- 数据库操作：

  - 在python shell中使用模型

    ```c
    cd E:\【冲鸭】\【学习】1. 代码代码代码冲冲冲\books\book5
    e:
    set FLASK_APP=hello.py
    flask shell
    ```

  - 创建表

    ```python
    from hello import db
    db.create_all()
    ```

  - 插入行

    ```python
    from hello import Role, User
    admin_role = Role(name="Admin")
    mod_role = Role(name="Moderator")
    user_role = Role(name='User')
    user_john = User(username='john', role=admin_role)
    user_susan = User(username='susan', role=user_role)
    user_david = User(username='david', role=user_role)
    ```

  - 对数据库的改动通过数据库 **会话** 管理

    ```python
    db.session.add_all([admin_role, mod_role, user_role, user_john, user_susan, user_david])
    ```

  - 写入数据库，**提交**会话

    ```python
    db.session.commit()
    ```

  - 数据库会话的**回滚**

    ```python
    db.session.rollback()
    ```

  - 修改行

    ```python
    admin_role.name = 'Administrator'
    db.session.add(admin_role)
    db.session.commit()
    ```

  - 删除行

    ```python
    db.session.delete(mod_role)
    db.session.commit()
    ```

  - 查询行

    ```python
    Role.query.all()
    User.query.all()
    ```

  - 使用**过滤器**进行更精确的数据库查询

    ```python
    User.query.filter_by(role=user_role).all()
    ```

  - 查看原生sql查询语句

    ```python
    str(User.query.filter_by(role=user_role))
    ```

  - 重开新的shell，发起一个查询

    ```python
    from hello import Role
    user_role = Role.query.filter_by(name='User').first()
    ```

- 在视图函数中操作数据库

- 集成Python Shell：使用`app.shell_context_processor`装饰器

  ```python
  @app.shell_context_processor
  def make_shell_context():
      return dict(db=db, User=User, Role=Role)
  ```

- 使用**Flask-Migrate**实现数据库迁移

  - 在新项目中可以使用`init`子命令添加数据库迁移支持

    ```python
    flask db init
    ```

  - `upgrade()`：把迁移中的改动应用到数据库中

  - `downgrade()`：将改动删除

## 6. 电子邮件

- 使用`Flask-Mail`提供电子邮件支持

- [使用Flask-Mail和qq邮箱SMTP服务发送邮件](https://blog.csdn.net/wbin233/article/details/73222027)

- 在python shell中发送电子邮件

  ```python
  from flask_mail import Message
  from hello import mail
  msg = Message('test email', sender='694317828@qq.com', recipients=['litian_cup@163.com'])
  msg.body = '这是text body.'
  msg.html = '这是<b>HTML</b> body.'
  with app.app_context():
  	mail.send(msg)
  ```

- [解决邮件发送错误：503 Error: need EHLO and AUTH first](https://blog.csdn.net/lingfeian/article/details/96731620)

- 异步发送电子邮件

## 7. 大型应用的结构

- Flask使用**蓝本（blueprint）**提供了更好的解决方法。蓝本和应用类似，也可以定义路由和错误处理程序。不同的是，在蓝本中定义的路由和错误处理程序处于休眠状态，直到蓝本注册到应用上之后，它们才真正成为应用的一部分。
- `from . import <module>`：相对导入，`.`表示当前包。`from .. import <module>`中的`..`表示当前包的上一层。
- pip自动生成需求文件：`pip freeze >requirements.txt`
- 创建虚拟环境的完整副本：
  1. 创建一个新的虚拟环境
  2. 运行：`pip install -r requirements.txt`











------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
