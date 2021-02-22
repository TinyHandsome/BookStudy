# 千锋Django学习笔记

[TOC]

## 写在前面

- 学习链接：[Python 900集（学完可就业/2019版）](https://www.bilibili.com/video/BV15J411T7WQ)：`[200集: ]`
- 学习的时候遇到的问题：
  1. [PyCharm右键SQLite找不到As Data Source选项](#anchor)
  2. [如何让其他电脑访问到自己的Django项目](#anchor2)

## 1. MVC和MTV

- 虚拟化技术u

  - 虚拟机
  - 虚拟容器
    - Docker
  - 虚拟环境
    - Python专用
    - 将Python依赖隔离

- MVC：一种软件设计典范，核心思想：解耦。

  - 降低各个模块之间的耦合性，方便变更，更容易重构代码，最大程度实现了代码的重用。

- Model：用于封装与应用程序的业务逻辑相关的数据以及对数据的处理方法，是Web应用程序种用于处理应用程序的数据逻辑部分，Model通常只提供功能新的接口，通过这些接口可以获取Model的所有功能。

- View：负责数据的显示和呈现，View是对用户的直接输出。

- Controller：负责从用户端收集用户的输入，可以看成提供View的反向功能，主要处理用户交互。

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210102100404725.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

- Django中的MVC

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021010210053763.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

- MTV：

  - 本质上与MVC没有什么差别，也是各组件为了保持松耦合关系，只是定义上有些许的不同。
  - Model：负责业务对象与数据库（ORM）的对象。这里orm是指，把model中的代码翻译为各个数据库的sql语言。
  - Template：负责把页面站视给用户
  - View：负责业务逻辑，并在适当的时候调用Model和Template
    - 注意：**这里的View跟MVC的View完全不一样，要类别的话，MVC的V对应MTV的T，同理，C对应V**

- 注意：Django中还有一个url分发器（也可以叫做路由），主要用来将一个个URL页面的请求分发给不同的View进行处理，View再调用响应的Model和Template。

- MTV设计模式：

  ![image-20210102101157811](E:\typora_pics_savepath\image-20210102101157811.png)

## 2. Django简介

- 新建一个项目：`django-admin startproject [项目名称]`

- 创建一个应用：`python manage.py startapp [app名称]`

- 运行一个应用：`python manage.py runserver`

- SQLite：

  - 轻量级的嵌入式的数据库
  - 特点：小

  - 场景：
    - 常用场景：Android、IOS、WP
  - 数据库常规操作相似度和MySQL达95%

- <a name = "anchor2">settings.py中需要注意的设置：</a>

  - `ALLOWED_HOSTS = ["*"]`：这里是为了让所有人都能够访问这个服务器，**如果想要其他的电脑也能通过局域网方问到你的项目**，就需要运行的时候输入：`python3 manage.py runserver 0:8000`，记住了，我就运行成功了嘻嘻（我在linux上建的服务器，这里是用win10连接的，成就感爆棚）：

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210103231243811.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

    **这里说个题外话**，如果上面还是不行的话，就可能是防火墙的原因了：

    1. 如果要想别人能够方问呢，除了ALLOWED_HOSTS设置之外，还要关闭防火墙

    2. 如果你百度关闭linux防火墙的话，会发现输入命令之后各种找不到，所以需要先安装防火墙，[参考链接](https://blog.csdn.net/qq_26733603/article/details/101082509)，我安装好后显示如下：

       ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210103230244777.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

    3. 然后就可以查看防火墙状态啦：`sudo ufw status`

    4. 最后，关闭防火墙：`sudo ufw disable`

  - `LANGUAGE_CODE = 'zh-hans'`：这里将语言设置为中文；注意，这里需要注意的是，要用`-`而不是下划线`_`，否则会报错，这是因为：[版本更新后Django项目setting.py中的LANGUAGE_CODE设置变了](https://blog.csdn.net/myisking/article/details/81952874)

  - `TIME_ZONE = 'Asia/Shanghai'`：这里将时间区域设置为中国的上海

- 运行后（舒服~）：

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210103101941525.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

- 运行的时候发现，会提示没有迁移数据库的警告，所以下面要进行一段数据库迁移的操作：

    - <a name = "anchor">**问题1：PyCharm右键SQLite找不到As Data Source选项**：我按照视频步骤来，右键就是死活找不到这个选项。</a>

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210103214323572.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/202101032133045.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

      解决方案也很简单，就是选这里就会出现老师说的那个选项了（如果点击测试链接需要下载驱动，直接下载就完了）：

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021010320511421.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

    - 连接数据库后，打开pycharm下面的terminal，
    
      输入：`python manage.py makemigrations`
      
      并输入：`python manage.py migrate`；再启动服务器：`python manage.py runserver`，现在就没有警告啦。
      
      ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210103225456454.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)
    

## 3. MTV简单流程

1. 实现一个路由
   - urls中-参数
     1. 匹配规则：正则
     2. 视图函数：对应的views中的一个函数，没有括号

2. 去views实现对应的视图函数

   - 第一个参数是request
   - 永远记得返回Response

3. html快捷输入

   1. ul>li
   2. ul*5
   3. ul>li*5
   4. 记住最后一定要按tab键

4. 创建模板的第一种方法：

   - 在app目录中，在pycharm右键templates，设置为模板路径

   - 同时，需要在`settings.py`中给`INSTALLED_APPS`注册app名

5. 创建模板的第二种方法（**在开发中使用这种，因为模板是可以集成和复用的**）：

   - 在项目目录下，新建templates，并设置为模板路径
   - 同时，需要在`settings.py`中给`TEMPLATES`的`DIRS`添加`os.path.join(BASE_DIR, 'templates')`

6. 创建第二个App：`python manage.py startapp Two`

   然后需要在`settings.py`中给`INSTALLED_APPS`增加新增的app名

7. 路由优化配置：

   - 项目如果逻辑过于复杂，可以进行拆分。
   - 拆分为多个App
   - 继续拆分路由器urls
     - 在App中创建自己的`urls.py`，设置`urlpatterns`，路由规则列表
     - 在urls中进行子路由的包含
   - 子路由使用
     - 跟路由规则 + 子路由规则

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021010519451225.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

## 4. 和Model的简单对接

1. 实现数据增删改查
   1. models：使用了ORM技术，Object Relational Mapping，对象关系映射，用于实现面像对象编程语言里不同类型系统的数据之间的转换。可以简单理解为翻译机。

   2. ORM将业务逻辑和SQL进行了一个解耦合
      - `object.save()`
      - `object.delete()`
      
   3. 关系型数据库
      - DDL：Database Define Language
      - 通过models定义实现数据库表的定义
      
   4. 数据操作：
      - 增删改查
      - 存储：`save()`
      - 查询：`Class.objects.all()`、`Class.objects.get(pk=xx)`
      - 更新：基于查询，查好的对象修改属性后`save()`
      - 删除：基于查询，调用`delete()`
      
   5. ctrl + P：参数提示

   6. 更换数据源sqlite为mysql

      1. `settings.py`中将数据源信息换为mysql

         ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021010619313716.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

      2. 利用pycharm的工具连接mysql数据库

         ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210106193325665.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

      3. 执行迁移：`python manage.py migrate`，这个时候会报错没有mysqldb：

         ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210106193500340.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

      4. 连接mysql的驱动：

         1. mysqlclient：2、3都能直接使用， 致命缺点：对mysql安装有要求，必须在指定位置存在配置文件
         2. python-mysql：对2支持很好，3不支持
         3. pymysql：2、3都支持，并且**它还可以伪装成前两个库**（啊，这？）

      5. 现在就要安装pymysql：`pip install pymysql`，这里建议用pip给mysqlclient包升个级，不然后面还会报错的：`pip install --upgrade mysqlclient`

      6. ~~把pymysql伪装成MySQLdb：~~

         ```python
         import pymysql
         pymysql.install_as_MySQLdb()
         ```

         相信我这一步，不要做，只需要安装`mysqlclient`就可以了，不需要伪装MySQLdb，不然的话，会报错`mysqlclient`不符合版本要求，因为`pymysql`的版本是0.10.1，所以伪装之后的`mysqlclient`也是0.10.1。

         ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210106194411809.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

      7. 再执行迁移操作：`python manage.py migrate`，成功！

         ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210106194508424.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

         同时，这些表也迁移过来了（就十分神奇，我服了~）：

         ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210106194558248.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

      8. 然后启动服务，获取四个学生

         ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210106194847230.png)

      9. 再查看

         ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210106194917757.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

   7. 测试数据模型

      - 进入这个项目的shell：`python manage.py shell`

      - 集成了python环境的shell终端

      - 通常在终端中做一些调试工作

      - 如何看代bug：

        - 看日志：先看第一条、再看最后一条
        - 梳理思路：程序在哪一个位置和预期出现了偏差

      - 表关系：1:1、1:M、M:N

      - 建立级联关系

        ```python
        from django.db import models
        
        class Grade(models.Model):
            g_name = models.CharField(max_length=32)
        
        class Student(models.Model):
            s_name = models.CharField(max_length=16)
            # 外键、级联关系
            s_grade = models.ForeignKey(Grade, on_delete=models.PROTECT)
        ```

      - 这里可能会报错：`TypeError: __init__() missing 1 required positional argument: 'on_delete'`

        - 这是因为你用的django版本太新了，创建外键的时候需要指定，如果删除了，应该怎么处理，详见[参考链接](https://www.cnblogs.com/gerenboke/p/12091960.html)

      - 然后就是要迁移哦：

        - `python manage.py makemigrations`
        - `python manage.py migrate`

   8. 经典重现
   
      1. CS/BS
   
         ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210109111000781.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)
   
      2. MVC
   
         ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210109112120314.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)
   
      3. MTV
   
         ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210109134601986.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)
   
      4. Django
   
         ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210109142901974.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

## 5. Model

- 在企业开发中，我们通常都是从数据开始开发的
- 数据库中的数据类型
  - 字符串
  - 数字
  - 日期时间
- 属性命名规则
  - 遵循标识符规则
  - 由于django的查询方式，不允许使用连续的下划线
- 逻辑删除：对于重要数据都做逻辑删除，不做物理删除，实现方法是定义isDelete属性，类型为BooleanField，默认值为False
- 字段类型
  - AutoField
  - CharField
  - TextField
  - IntegerField
  - DecimalField：高精度
  - FloatField
  - BooleanField
  - NullBooleanField
  - DateField
  - TimeField
  - DateTimeField
  - FileField
  - ImageField：继承FileField，图片格式校验
- 字段选项
  - null
  - blank
    - null是数据库范围的概念，`None`；blank是表单验证范畴，`""`
  - db_column
  - db_index
  - default
  - primary_key：主键约束
  - unique：唯一约束
- 关系
  - ForeignKey：一对多
  - ManyToManyField：多对多
  - OneToOneField：一对一
- 模型成员objects
  - Django默认通过模型的objects对象实现模型数据查询
  - Django有两种过滤器用于筛选记录
    - filter：返回符合筛选条件的数据集
    - exclude：返回不符合筛选条件的数据集
    - 多个filter和exclude可以连接在一起查询
- 快捷键
  - .re 快捷生成return
  - 多用`.`看看世界的美好
- 方法
  - 对象方法
    - 可以调用对象的属性，也可以调用类的属性
  - 类方法
    - 不能调用对象属性，只能调用类属性
  - 静态方法
    - 啥都不能调用，不能获取对象属性，也不能获取类属性
    - 只是寄生在我们这个类上而已
- 在管理器上调用方法返回查询集，查询经过过滤器筛选返回新的查询集，所以可以写成链式调用，返回查询及的方法成为过滤器：
  1. `all()`：返回所有数据
  2. `filter()`：返回符合条件的数据
  3. `exclude()`：过滤掉符合条件的数据
  4. `order_by()`：排序
  5. `values()`：一条数据就是一个字典，返回一个列表
- 状态码
  - 2xx：请求成功
  - 3xx：转发或重定向
  - 4xx：客户端错误
  - 5xx：服务器错误，后端开发人员最不想看到的
- 产品上线后需要将`DEBUG`改为`True`
- 获取单个对象
  - 查询条件没有匹配的对象会抛异常：DoesNotExist
  - 如果查询条件存在多个对象也会抛异常：MultipleObjectsReturned
- First和Last
  - 默认情况下可以正常从QuerySet中获取
  - 隐藏bug：可能会出现first和last获取到的是相同的对象
  - 解决方案：显示、手动写排序规则
- `count()`：返回当前查询集中的对象个数
- `exists()`：判断查询集中是否有数据，如果有数据返回True，没有返回False
- 切片
  - 和python中的切片不太一样
  - `QuerySet[5:10]`：获取第5条到第15条数据
  - 相当于sql中的limit和offset
- 缓存集
  - filter
  - exlude
  - all
  - 都不会真正的查询数据库
  - 只有我们在迭代结果集，或者获取单个对象属性的时候，它才会真正的查询数据库
  - 懒查询
    - 为了优化数据结构和数据的查询
- 查询条件
  - 属性：`__运算符=值`
  - gt
  - lt
  - gte
  - lte
  - in：在某一个集合中
  - contains：类似于模糊查询的like
  - startswith：以什么开始，也类似于like
  - endswith：以什么结束，也类似like
  - exact：判断，大小写敏感，`filter(isDelete=False)`
  - isnull，isnotnull：判断是否为空，`filter(sname_isnall=False)`
  - 前面同时添加i，ignore，忽略大小写的匹配
    - iexact
    - icontains
    - istartswith
    - iendswith
- Django中查询条件有时区问题
  - 关闭Django中自定义的时区：√，更好用
  - 在数据库中创建对应的时区表
- F
  - 可以获取我们属性的值
  - 可以实现一个模型的不同属性的运算操作
  - 还可以支持算术运算
- Q
  - 可以对查询条件进行封装
  - 封装之后，可以支持逻辑运算：与 &、或 |、非 ~

- 模型成员
  1. 显性属性：
     - 开发者手动书写的属性
  2. 隐形属性：
     - 开发者没有书写，ORM自动生成的
     - 如果把隐性属性手动声明了，系统就不会为你产生隐性属性了

- 模型总结

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210218135736357.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

## 6. Template

1. 标签
   - 标识符：`{%  %}`
   - 标签分为单标签和成对的标签
   - 成对的标签切记不能省略，开始标签和结束标签
2. 结构标签
   - blcok
     - 块
     - 用来规划我们的布局（挖坑）
     - 首次出现，代表规划
     - 第二次出现，代表填充以前的规划
     - 第三次出现，代表填充以前的规则，默认动作是覆盖，如果不想覆盖，可以添加`{{ block.super }}`，这样就实现了增量式操作。
   - extends
     - 继承
     - 可以获取父模板中的所有结构
   - block + extends
     - 化整为零
   - include
     - 包含
     - 可以将页面作为一部分，嵌入到其他页面中
   - include + block
     - 由零聚一
   - 三个标签也可以混合使用
   - 能用block + extends搞定的，就尽量不要使用include
   - 如果我们继承自一个父模板，子模板自己直接重写页面结构是不生效的，只能在既有的坑中进行填充
3. 静态资源
   - 动静分离
   - 创建静态文件夹
   - 在settings中注册 STATICFILES_DIRS=[]
   - 在模板中使用
     - 先加载静态资源：`{% load static %}`
     - 使用 `{% static 'xxx' %}`，其中xxx为相对路径
   - 坑点：
     - 仅在debug模式中使用
     - 以后需要自己单独处理

## 7. View

1. 视图，用来接收Web请求，并作出响应，视图的本质就是一个Python中的函数。

2. 视图的响应分未两大类：
   1. 以Json数据形式返回
   2. 以网页的形式返回：
      1. 重定向到另一个网页
      2. 错误视图（40x，50x）
   
3. ~~url匹配正则注意事项：~~这一部分，在最新版的django（3.1.4）中，不存在这个问题
   1. 正则匹配时从上到下进行遍历，匹配到就不会继续向后查找了
   2. 匹配的正则前方不需要加反斜线
   3. 正则前需要加（r）表示字符串不转义
   
4. urls
   - 路由器
     - 按照列表的书写顺序进行匹配的
     - 从上到下匹配，没有最优匹配的概念
     
   - 路由规则编写：
     - 我们通常直接指定以 `^` 开头
     - 在结尾处直接添加反斜线
     
   - 路由规则

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210220093047844.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

   - 需要注意的是：在新版本***Django2.x*** 及以上中，url的路由表示用path和re_path代替

   - 路由路径中的参数使用`()`进行获取

     - 一个圆括号，对应视图函数中的一个参数
     - 参数：
       - 路径参数：
         - 位置参数：按照书写顺序进行匹配
         - 关键字参数：按照参数名称匹配，和顺序就无关了
       - 参数个数必须和视图函数中的参数个数一致（除了默认的request以外）
     
   - 反向解析：

     - 在`include`中添加第二个参数`namespace`之后出现 **Specifying a namespace in include() without providing an app_name **的问题：[解决方案](https://www.cnblogs.com/ljxh/p/11099737.html)

       ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210220150720216.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)
       
     - 根据根路由中注册的namespace和在子路由中注册的name，这两个参数来动态获取我们的路径
   
     - 在模板中使用：`{% url 'namespace:name' %}`
   
     - 如果带有位置参数：`{% url 'namespace:name' value1 value2 [valuen...] %}`
   
     - 如果带有关键字参数：`{% url 'namespace:name' key1=value1 key2=value2 [keyn=valuen] %}`
   
5. 错误页面定制

   - 在模板中重写对应错误状态码的页面：`404.html`
   - 关闭debug
   - 实现原则：就近原则

6. 双R

   1. Request

      1. 内置属性

         - method

         - path

         - GET

           - 类字典结构

           - 一个key允许对应多个值

           - get

           - ###### getlist

         - POST

         - META：

           - 各种客户端的元信息
           - REMOTE_ADDR：远端访问IP

   2. Response

7. 知识点

   - 内置函数：`locals()`
   - 将局部变量，使用字典的方式进行打包
   - key是变量名，value是变量中存储的数据
   - 如果关闭调试模式可能会报错：`CommandError: You must set settings.ALLOWED_HOSTS if DEBUG is False.`
     - [解决方案](https://blog.csdn.net/kan2016/article/details/82838509)：设置任何用户均可以访问：`ALLOWED_HOSTS = ['*']`
   
8. 视图总结

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210222171658875.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)









学到（要学）：P232

------

我的CSDN：https://blog.csdn.net/qq_21579045

我的博客园：https://www.cnblogs.com/lyjun/

我的Github：https://github.com/TinyHandsome

纸上得来终觉浅，绝知此事要躬行~

欢迎大家过来OB~

by 李英俊小朋友