# 千锋Django学习笔记

[TOC]

## 写在前面

- 学习链接：[Python 900集（学完可就业/2019版）](https://www.bilibili.com/video/BV15J411T7WQ)：`[200集: 358集]，共159集`
- 感想|摘抄：
  1. 优秀的程序员：
     - 松耦合、解耦合
     - 高内聚
  2. Django版本：1.1
- 学习的时候遇到的问题：
  1. [PyCharm右键SQLite找不到As Data Source选项](#anchor)
  2. [如何让其他电脑访问到自己的Django项目](#anchor2)

## 1. MVC和MTV

- 虚拟化技术

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

         伪装报错的原因：[mysqlclient 1.4.0 or newer is required; you have 0.10.0.](https://blog.csdn.net/lvluobo/article/details/107850673)

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

## 8. 会话

1. 爬虫
   - 模拟人去请求数据
   - 提取数据
   - 存储数据
   - 核心内容
     - 数据爬取
     - 数据提取
     - 数据存储
     - 提升效率：进程、线程、协程
   - MIME：
     - 作用：指定传输数据使用哪种形式打开
     - 格式：大类型/小类型 
       - image/png
       - image/jpg
   
2. Json
   1. JsonObject
      - {}
      - key-value
   2. JsonArray
      - []
      - 列表中可以是普通数据类型，也可以是jsonObject
   3. JsonObject和JsonArray可以嵌套
   4. 给移动端/Ajax的时候用JsonResponse
      - 前后端分离
      - DRF
   5. Google Chrome插件名：JsonFomatter、JsonView
   
3. HttpResponse
   1. HttpResponseRedirect
      - 重定向，暂时
      - 302
      - 简写 redirect
   2. JsonResponse
      - 以Json格式返回数据
      - 重写了`__init__`，序列化Json数据，指定content_type为application/json
   3. HttpResponsePermanentRedirect
      - 重定向，永久性
      - 302
   4. HttpResponseBadRequest
      - 400
   5. HttpResponseNotFound
      - 404
   6. Http404
      - Exception
      - raise 主动抛出异常
   
4. 会话技术
   1. 出现场景
      - 服务器如何识别客户端
      - Http在WEB开发中基本都是短连接
   2. 请求的生命周期
      - requetst开始
      - response结束
   3. 种类
      - cookie
        - 客户端会话技术
        - 数据存储在客户端
        - 键值对存储
        - 支持过期时间
        - 默认Cookie会自动携带，本网站所有Cookie
        - Cookie跨域名、跨网站
        - 通过HttpResponse
        - Cookie默认不支持中文
        - 可以加盐（加密），获取时还需要解密
      - session
        - 服务端会话技术
        - 数据存储在服务器中
        - 默认Session存储在内存中
        - Django中默认会把Session持久化到数据库中
        - Django中Session的默认过期时间是14天
        - 主键是字符串
        - 数据是使用了数据安全
          - 使用了base64
          - 在前部添加了一个混淆串
        - Session依赖于Cookie
      - token
        - 服务端会话技术
        - 自定义的Session
        - 如果Web页面开发中，使用起来和Session基本一致
        - 如果使用在移动端或者客户端开发中，通常以Json形式传输，需要移动端自己存储Token，需要获取Token关联数据的时候，主动传递Token。
      - Cookie、Session和Token对比
        - cookie使用起来更简洁，服务器的压力更小；数据不是很安全
        - session服务器要维护session，相对安全
        - token自定义的session，拥有session的所有优点，自己维护略微麻烦，支持更多的终端
   
5. CSRF

   - 防跨站攻击
   - 防止恶意注册，确保客户端是我们自己的客户端
   - 使用了cookie中的csrftoken进行验证，传输
   - 服务器发送给客户端，客户端将cookie获取过来，还要进行编码转换（数据安全）
   - 如何实现的
     - 在我们中存在csrf_token标签的页面中，响应会自动设置一个cookie，csrftoken
     - 当我们提交的时候，会自动验证csrftoken
     - 验证通过，正常执行以后流程，验证不通过，直接403

6. 目前状态

   - MTV
     - 基本完成
     - Template不会再讲了
     - Views也不会再讲了
     - Model
       - Model关系
       - Model继承
   - 高级
     - 第三方插件
     - 底层的部分原理
       - AOP 面向切面编程
         - 反扒
         - 安全
     - 文件上传
     - 前后端分离
       - RESTful
     - 日志
     - 后台管理
     - 用户角色、用户权限
     - 部署
     - 支付宝支付

7. 算法

   1. 编码解码
      - Base64
      - urlencode
   2. 摘要算法、指纹算法、杂凑算法
      - MD5、SHA
        - MD5默认是128位的二进制
        - 32位的二进制
        - 32位的Unicode
      - 单向不可逆的
      - 不管输入多长，输出都是固定长度
      - 只要输入有任意的变更，输出都会发生巨大的变化
   3. 加密
      - 对称加密
        - 一把钥匙
        - DES、AES
        - 加密解密效率高
        - 钥匙一旦丢失，所有数据全GG
      - 非对称加密
        - 两把钥匙，成对的
        - 公钥和私钥
        - RSA、PGP
        - 安全性最高
        - 算法复杂，需要时间长
        - 支付宝、微信都是RSA

8. 登录

   - 首先要有一个页面
     - 页面中有输入框
     - 有登录按钮
   - 点完登录，默认进入个人中心
   - 个人中心可以显示用户名

9. 编码

   - ASCII
   - Unicode

10. Session交互图  

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210305160614371.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

11. 会话总结

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210317170317755.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

## 9. 迁移原理和模型关系

1. 迁移
   1. 分两步实现
      1. 生成迁移文件
      2. 执行迁移文件
   2. 迁移文件的生成
      - 根据models文件生成对应的迁移文件
      - 根据models和已有迁移文件的差别生成新的迁移文件
   3. 执行迁移文件
      - 先去迁移记录中查找哪些文件迁移过，哪些未迁移过
        - app_label + 迁移文件名字
      - 执行未迁移的文件
      - 执行完毕，记录执行过的迁移文件
   4. 重新迁移
      1. 删除迁移文件
      2. 删除迁移文件产生的表
      3. 删除迁移记录
2. 模型关系
   1. 1：1
      - 应用场景
        - 用于复杂表的拆分
        - 扩展新功能
      - Django中OneToOneField
        - 使用的时候，关系声明还是有细微差别
      - 实现
        - 使用外键实现的
        - 对外键添加了唯一约束
      - 数据删除
        - 级联表
          - 主表
          - 从表
          - 谁声明关系，谁就是从表
          - 在开发中如何确认主从
            - 当系统遭遇不可避免的毁灭时，只能保留一张表的时候，这个表就是主表
        - 默认特性
          - 从表数据删除，主表不受影响
          - 主表数据删除，从表数据直接删除
        - PROTECT受保护
          - 开发中为了防止误操作，我们通常会设置此模式
          - 主表如果存在级联数据，删除动作受保护，不能成功
          - 主表不存在级联数据，可以删除成功
        - SET
          - SET_NULL：允许为NULL
          - SET_DEFAULT：存在默认值
          - SET()：设为指定值
      - 级联数据获取
        - 主获取从，隐性属性，默认就是级联模型的名字
        - 从获取主，显性属性，就是属性的名字
   2. 1：M
      - ForeignKey
      - 主从获取
        - 主获取从：隐性属性，级联模型_set
          - student_set   Manager的子类
            - all
            - filter
            - exclude
            - Manager上能使用的函数都能使用
        - 从获取主：显性属性
   3. M：N
      - 实际上最复杂
      - 开发中很少直接使用多对多属性，而是自己维护多对多
      - 产生表的时候会产生单独的关系表
        - 关系表中存储关联表的主键，通过多个外键实现的
        - 多个外键值不能同时相等
      - 级联数据获取
        - 从获取主
          - 使用属性，属性是一个Manager子类
        - 主获取从
          - 隐性属性
            - 也是Manager子类，操作和从操作主完全一样
      - 级联数据
        - add
        - remove
        - clear
        - set
   4. ManyRelatedManager
      - 函数中定义的类
      - 并且父类是一个参数
      - 动态创建
   5. 模型继承
      - Django中模型支持继承
      - 默认继承是会将通用字段放到父表中，特定字段放在自己的表中，中间使用外键连接
        - 关系型数据库，关系越复杂，效率越低，查询越慢
        - 父类表中也会存储过多的数据
      - 使用元信息来解决这个问题
        - 使模型抽象化
        - 抽象的模型就不会在数据库中产生映射了
        - 子模型映射的表中直接包含父模型的字段
   6. 在企业开发中
      - model -> sql
        - 都可以使用
      - sql -> model
        - django也提供了很好的支持
        - `python manage.py inspectdb`
          - 可以直接根据表生成模型
          - 元信息中包含一个属性 `managed=False`
      - 如果自己的模型不想被迁移系统管理，也可以使用 `managed=False` 进行声明

## 10. 静态资源

1. html中的img属性：`<img src="{{ icon_url }}" alt="{{ username }}">`，alt 属性是一个必需的属性，它规定在图像无法显示时的替代文本。

2. 在models中设置文件上传的保存路径：

   1. 在settings中设置media路径：

      `MEDIA_ROOT = os.path.join(BASE_DIR, 'static/upload')`

   2. 在models中设置属性：

      `u_icon = models.ImageField(upload_to='%Y/%m/%d/icons')`

      可以通过增加时间标记进行分文件夹保存
   
3. MCS结构体系，multi client server

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210331195524811.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

4. model、静态资源、文件上传、requests总结

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210331195700881.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

## 11. 缓存

1. 缓存，Django Cache

   - 提升服务器响应速度
   - 将执行过的操作数据存储下来，在一定时间内，再次获取数据的时候，直接从缓存中获取
   - 比较理想的方案，缓存使用内存级缓存
   - Django内置缓存框架

2. 缓存框架的核心目标

   1. 较少的代码
      - 缓存应该尽可能快
      - 因此围绕缓存后端的所有框架代码应该保存在绝对最小值，特别是对于获取操作
   2. 一致性
      - 缓存API应该是提供跨越不同缓存后端的一致接口
   3. 可扩展性
      - 基于开发人员的需求，缓存API应该可以在应用程序级别扩展

3. 缓存

   Django中内置了缓存框架，并提供了几种常用的缓存

   1. 基于Memcached缓存
   2. 使用数据库进行缓存
   3. 使用文件系统进行缓存
   4. 使用本地内存进行缓存
   5. 提供缓存扩展接口

4. 缓存配置

   1. 在views前面新增装饰器：`@cache_page(30)`，括号中的时间为缓存保留的时间（秒）

   2. 缓存数据流程图

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210412172615920.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

   3. 如果不用装饰器，也可以通过set和get缓存的方式，进行手动写入和获取缓存

      ```python
      # @cache_page(30)
      def news(request):
          result = cache.get("news")
          # 如果缓存中能找到news对应的值，直接返回该值
          if result:
              return HttpResponse(result)
      
          news_list = []
          for i in range(10):
              news_list.append("最近贸易战又开始了 %d" % i)
      
          sleep(5)
      
          data = {
              'news_list': news_list
          }
      
          # 如果缓存中没有找到news的值，则返回response，并将内容写入到缓存中
          response = render(request, 'news.html', context=data)
          cache.set('news', response.content, timeout=60)
      
          return response
      ```

5. redis：内存级的数据库，django中没有redis的缓存实现，所以需要pypi安装

   `pip install django-redis`

   `pip install django-redis-cache`

6. redis在windows中启动的方法

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021041219581947.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

7. 修改缓存为redis

   ```python
   CACHES = {
       'default': {
           # django原生缓存
           # 'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
           # 'LOCATION': 'my_cache_table',
           # 'TIMEOUT': 60 * 5,
   
           # redis缓存
           "BACKEND": "django_redis.cache.RedisCache",
           "LOCATION": "redis://127.0.0.1:6379/1",
           "OPTIONS": {
               "CLIENT_CLASS": "django_redis.client.DefaultClient",
           }
       }
   }
   ```

8. 查看redis缓存的数据

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210412200501137.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

9. 查看过期时间

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021041220062498.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

10. 配置不同的数据库，选择不同的数据库进行缓存

    1. 配置

       ```python
       CACHES = {
           'default': {
               # django原生缓存
               'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
               'LOCATION': 'my_cache_table',
               'TIMEOUT': 60 * 5,
           },
           'redis_backend': {
               # redis缓存
               "BACKEND": "django_redis.cache.RedisCache",
               "LOCATION": "redis://127.0.0.1:6379/1",
               "OPTIONS": {
                   "CLIENT_CLASS": "django_redis.client.DefaultClient",
               },
           }
       }
       ```

    2. 选择

       ```python
       @cache_page(60, cache='redis_backend')
       ```

## 12. 中间件和AOP

1. 中间件：是一个轻量级的、底层插件。可以介入Django的请求和相应过程（面向切面编程）。中间件的本质是一个python类，装饰器。

2. AOP：面像切面编程，Aspect Oriented Programming。AOP主要实现的目的是针对业务处理过程中的切面进行提取，它所面对的是处理步骤中的某个过程或阶段，以获得逻辑过程中各个部分之间低耦合的隔离效果。

3. 中间件可以切入的点

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021041508371487.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

4. 切入函数

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210415092610226.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

5. 自定义中间件

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210415092727932.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

6. AOP中间件的作用

   1. 实现统计功能
      1. 统计IP
      2. 统计浏览器
      
   2. 实现权重控制
   
      1. 黑名单
      2. 白名单
   
   3. 实现反爬
   
      1. 反爬虫
   
         1. 十秒之内只能查询一次
   
         2. 频率请求限制反爬
   
            ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210415163902458.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)
   
      2. 实现频率控制
      
   4. 通过中间件的`process_exception`函数实现 界面友好化、应用交互友好化
   
      访问中出错、出异常后跳转到首页
   
7. HTTP默认端口为80，HTTPs默认端口为443

8. csrf问题验证失败解决方法

   1. 注释设置中的csrf中间件
   2. 在页面的POSThtml代码中，添加`{% csrf_token %}`
   3. 在views视图函数中添加csrf豁免装饰器：`csrf_exempt`

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210421171813552.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

9. 中间件调用顺序

   1. 中间件注册的时候是一个列表
   2. 如果我们没有在切点出直接进行返回，中间件会依次执行
   3. 如果我们直接进行了返回，后续中间就不再执行了

10. 切点

    1. process_request
    2. process_view
    3. process_template_response
    4. process_response
    5. process_exception

11. 切面

## 13. 分页器

1. 分页器原理

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210424172516164.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

2. 分页显示：`Paginator`

   ```python
   def get_students_with_page(request):
       page = int(request.GET.get("page", 1))
       per_page = int(request.GET.get("per_page", 10))
   
       students = Student.objects.all()
       paginator = Paginator(students, per_page)
   
       page_obj = paginator.page(page)
       data = {
           "page_object": page_obj
       }
       return render(request, 'students_with_page.html', context=data)
   ```

3. `@property`：将函数设为类的私有属性，我们可以观测它。

4. 验证码

   ```python
   def get_code(request):
       # 初始化画布，初始化画笔
       mode = 'RGB'
       size = (200, 100)
       red = get_color()
       green = get_color()
       blue = get_color()
   
       color_bg = (red, green, blue)
       image = Image.new(mode=mode, size=size, color=color_bg)
       imagedraw = ImageDraw(image, mode=mode)
       imagefont = ImageFont.truetype(settings.FONT_PATH, 100)
   
       verify_code = generate_code()
   
       request.session['verify_code'] = verify_code
   
       for i in range(len(verify_code)):
           fill = (get_color(), get_color(), get_color())
           imagedraw.text(xy=(50 * i, 0), text=verify_code[i], font=imagefont, fill=fill)
   
       for i in range(10000):
           fill = (get_color(), get_color(), get_color())
           xy = (random.randrange(201), random.randrange(100))
           imagedraw.point(xy=xy, fill=fill)
   
       fp = BytesIO()
       image.save(fp, "png")
       return HttpResponse(fp.getvalue(), content_type="image/png")
   ```

5. 富文本

   - 带格式的文字：
     - 博客、论坛
       - 富文本：RTF
       - MarkDown
   - 安装插件：`django-tinymce`（2.7.0）
   
6. 总结

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210517175111644.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

## 14. AXF项目

### 14.1 需求分析

1. 技术部

    - 产品经历
      - 产品狗
      - 一条产品线两个产品
      - 产品PRD（Product Requirement Document）产品需求文档
      - 原型图（其实就和真实网站长的差不多，只不过页面都是静态的，假的）
    - 后端
      - 后端基本都是人最多的
      - 最少2人
        - Python
        - Java
        - PHP
        - Node.js
        - Go
      - 根据需求进行表结构设计
        - 有哪些表
        - 表中有哪些字段
        - 表有哪些关系
    - UI
      - UD：界面设计
      - UE：用户体验
    - 前端
      - MTV
      - HTML5 Web前端 一个人
        - REACTNATIVE
      - Android
      - IOS
    - 测试
      - 黑盒测试
        - 功能测试
        - 点点测试（Excel，check_list）
      - 白盒测试
        - 不会正向开发，可以写代码测试你的代码
        - 高级开发，专门用来查找bug
    - 运维
      - 上线
      - 维护稳定运转
    - 版本迭代
      - 产品
    
2. AXF项目分析
    - 主页面显示
      - 最简单的，数据查询，显示
    - 商品数据展示
      - 级联查询，排序
    - 用户系统
      - 核心系统
    - 购物车系统
      - 商品和用户的关系
      - 订单系统
        - 购物车数据转换成订单
      - 支付系统
        - 接口调用
    - 扩展
      - 地址管理系统
      - 积分系统
      - 会员级别
      - 评价系统
      - 优惠券系统
      - 数据安全
      - 过滤器
      - 反爬
      - 权限：用户角色
    - 部署
      - 动静分离部署
    
3. 开始开发
    - 基本工程搭建
    - 前端静态搭建
    - Model -> DB
    - 业务逻辑开发
    - 前后端一起来
      - ajax
    
4. 前端基础架构

    - base模板

      - 导入通用资源
        - reset.css，[自己找的地址](https://segmentfault.com/a/1190000009369872)

    - viewpoint：将html从windows适配到手机

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210608195147429.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

    - 前端适配

      - 推荐百分比，而不推荐固定尺寸
      - 适配单位
        - px：像素
        - em：
          - 相对单位
          - 默认相对于父级元素
          - 默认大小 1em = 16px
        - rem
          - 相对单位
          - 相对于根基元素（root）
          - 默认大小 1rem = 16px
        - 所有图形界面，底层计算都是px
      - 弹性盒模型
      - 响应式布局

    - 项目中

      - 屏幕宽度的十分之一作为rem的基础单位

5. 数据展示

    - 建立数据
      - 先建表
      - Model -> SQL
    - 插入数据
    - 数据查询

6. 程序调试

    - 打印日志
      - print
      - log
        - logging
    - debug
      - 断电调试
      - 解决稳定复现bug的好方案
    - 统计工具
      - DjangoDebugToolbar
        - Django调试工具条
        - 拥有极强的调试功能
        - 提供了各种信息的获取

7. 项目

    - 端的概念
      - 京东自营
        - 用户端
        - 后台管理端
      - 第三方卖家
        - 用户端
        - 商家端
        - 后台管理端
      - 淘宝
        - 用户端
          - BS/CS
          - MCS
        - 商家端
          - BS/CS
        - 后台管理端
          - BS/CS
    - AXF
      - 用户端
        - MTV
          - 前后端都需要我们自己搞定
      - 糅合之前学过的知识点
      - 写地址的时候，记得把地址写全了，比如说最后面的`/`，如果不写的话，会多一次重定向
    - 前后端分离
      - 后端RESTApi
        - JSON传输数据
      - 前端
        - VUE
        - Android
        - IOS

### 14.2 一些开发时遇到的问题

1. [pymysql 报错：from . import connections # noqa: E402](https://blog.csdn.net/weixin_44678368/article/details/112631405)

    这里需要下载 0.10.1的pymysql，不然会报错

2. [mysqlclient 1.4.0 or newer is required; you have 0.10.1](https://knight.blog.csdn.net/article/details/108576312)

    需要在 `__init__`文件下加如下内容

    ```python
    import pymysql
    pymysql.version_info = (1, 4, 13, "final", 0)
    pymysql.install_as_MySQLdb()
    ```

3. [pycharm 高亮提示 unresolved template reference的解决](https://blog.csdn.net/louisliushu/article/details/89069341)

    需要设置django的settings.py的位置

4. 安装 django-debug-toolbar的时候，不要直接 `pip install`，否则会直接卸载了你低版本的django，给你装一个高级的，然后运行就会报错了

    所以需要安装指定版本的： `pip install django-debug-toolbar==1.10.1`

### 14.3 一些需要注意的细节

1. 链接路径后面无特殊要求，一定要加 `/`（可以少一步请求）
2. js获取jquery对象属性
   1. attr：可以获取任意属性
   2. prop：只能获取内置属性
3. 项目中多块逻辑拥有相同操作
   1. 封装一个函数
   2. 装饰器
   3. 中间件
4. 浏览器行为
   1. 重定向
   2. 跨域
5. 价钱后端必算，前端选算


### 14.4 Note

1. User

   - 用户表设计
       - username
       - password
       - email
       - phone
       - icon
       - is_active
       - is_delete
   
2. 高级密码安全工具
   - 不再使用单一的算法实现
       - 至少使用两种以上的算法
       - 算法中融入时间散列
   - 将输入数据进行哈希处理
   - 哈希处理之后拼接时间戳
       - 中建使用特定拼接符号
   - 将拼好的数据进行编码
   - 验证策略
       - 将输入进行相同的哈希策略
       - 将数据库中的密码进行解码处理
       - 去除时间散列的混淆
       - 比较哈希码
   
3. 版本升级后，策略不兼容
   - 第一版本，注册之后，密码是明文
   - 第二版本，注册之后，密码是hash值
   - 第三版本，注册之后，密码是hash + 时间散列
   - 假定目前处于第三版本，让你同时兼容第一第二版本
       - 对请求的参数添加版本号，没添加的就是旧版本
       - 对于低版本使用特定认证，认证完后，在会话中将低版本的版本号存下来
           - 小米低版本兼容
           - 除了密码外，又加了短信验证码验证
   
4. homework
   - 邮箱校验
   - 密码一致性校验
   - 自己封装一个高级密码安全工具
   
5. 用户激活，认证
   - 途径
     - 邮件
     - 短信
     - 人工审核
   - 邮件
     - 发送邮件
       - 收件人地址
       - 发件人的信息
         - 用户名
         - 密码
         - 服务器
           - 邮件服务器
           - 端口
         - 内容
     - 点击邮件中的链接就可以激活
       - 链接中存在用户的唯一标识
         - http://xxxxx/activate/?u_token=YYY
         - u_token 缓存中作为key，value -> user_id
         - u_token -> uuid
       - 标识存在过期时间
       - 标识存在使用次数限制
   
6. 错误信息
   - 先将错误信息存储下来
   - 在错误显示页面获取错误信息
     - 保证错误信息只能出现一次
     - 获取到数据之后，直接将自己删除
   
7. 购物车

   - 购物多对多的关系

     - 用户
     - 商品

   - 订单

     - 订单和已购买商品是一对多的关系
     - 表关系
       - 订单表
         - 属于哪个用户
       - 订单商品表
         - 购物车里
       - 地址
         - 每个订单对应一个地址
         - 一个地址可以对应多个订单 
         - 订单会级联收获地址表，而不是人的地址表
       - 优惠券

   - 购物车设计

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/859889bb01b54a56ab0770f4b9be887c.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

   - 购物车逻辑

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/981083ba0e994bfabfd5733145d85ab7.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)
   
8. 添加购物车

   - 需要用户
     - 如果用户未登录，直接跳转登录
   - 需要商品
     - 传第商品唯一标识

   - 添加的合法性验证
     - 此数据不存在，创建购物车数据
     - 此数据存在，直接将数量+1

9. 全选逻辑

   - 默认状态
     - 全选按钮是选中
       - 内部所有商品是选中的
     - 全选按钮未选中
       - 内部商品只要存在未选中的，全选就应该是未选中
   - 点击全选
     - 原状态是选中
       - 全选和所有商品都变成未选中
     - 原状态是未选中
       - 全选和所有商品都变成选中
   - 点击单个商品
     - 商品由选中变成未选中
       - 全选一定变成未选中
     - 商品由未选中变成选中
       - 全选的默认状态就是未选中
       - 可能变成选中

10. 支付

    - 官方文档
    - 常见的支付
      - 支付宝
        - 企业资质
        - 营业执照
      - 微信
        - 要求同支付宝
        - 要认证，一次200，一年一收
      - 银联
      - 百度钱包
      - 京东钱包
    - 支付宝支付
      - 支付宝开放平台
      - 蚂蚁金服开放平台 
    
11. 部署

    - 默认Django中使用的是开发者服务器
      - runserver
        - 路由处理功能，动态资源处理
        - 如果是debug的话，静态资源处理功能
      - 功能健壮，性能比较低，仅适用于开发
    - 部署不会使用单一服务器
      - Apache
      - Nginx
        - HTTP服务器
          - 处理静态资源
        - 反向代理
          - uWSGI：HTTP服务器
          - gunicorn：HTTP服务器
        - 邮件服务器
        - 流媒体服务器

## 15. Nginx

- Nginx简介

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/a6fa567d83a1456fbdfdf33a3e353c0c.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

- [Nginx开发从入门到精通](http://tengine.taobao.org/book/)

- HTTP和反向代理

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/1fc288250f38438b96749cef93a1e279.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

- [win10上安装nginx](https://www.cnblogs.com/wzz2500/p/11401118.html)

- Nginx配置文件

  - 指令分未简单指令和块指令
  - 一个简单指令：由名称和参数组成，以空格分隔，并以分号结尾
  - 一个块指令：和简单指令具有相同的结构，但不是以分号结束，而是以一个大括号包围的一堆附加指令结束
  - 如果一个大括号内可以由其他的指令，它接被称为一个上下文，比如（events，http，server，location）

- Nginx配置文件结构

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/fe72ca1fa77d47759e8f8e4a7f9ac806.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_14,color_FFFFFF,t_70,g_se,x_16)

- main：

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/852c2fc380ab40f9a91977b15fb9926c.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

- events：

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/3ce3cfa2c76f4609aaeae910e53816b9.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

- http

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/0057b286bacb49ebae6fa7a2c0073669.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

- server

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/9406098b852a4dcca7e39e70daec4922.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

- location

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/be9759fb8452454ab5f6b3d08ee109bb.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

- Django部署

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/1fdf162133514c109a65267b65702a21.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_19,color_FFFFFF,t_70,g_se,x_16)

- nginx配置文件（关于AXF项目）

  ```conf
  #user  nobody;
  worker_processes  1;
  
  #error_log  logs/error.log;
  #error_log  logs/error.log  notice;
  #error_log  logs/error.log  info;
  
  #pid        logs/nginx.pid;
  
  
  events {
      worker_connections  1024;
  }
  
  
  http {
      include       D:/nginx-1.20.1/conf/mime.types;
      default_type  application/octet-stream;
  
      sendfile        on;
      #tcp_nopush     on;
  
      #keepalive_timeout  0;
      keepalive_timeout  65;
  
      #gzip  on;
  
      server {
          listen       80;
          server_name  localhost;
          root  E:/1-Work/3-Code/python_projects/6-AXFProject/GPAXF;
  
          #charset koi8-r;
  
          #access_log  logs/host.access.log  main;
  
          location /static {
              alias E:/1-Work/3-Code/python_projects/6-AXFProject/GPAXF/static;
              # root   html;
              # index  index.html index.htm;
          }
  
          error_page   500 502 503 504  /50x.html;
          location = /50x.html {
              root   html;
          }
      }
  }
  ```

- nginx配置文件测试

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/80896296e42d48e0ae2f8ad8926deac4.png)

- 启动nginx

  `nginx -c E:/1-Work/3-Code/python_projects/6-AXFProject/GPAXF/config.conf`

- 安装uwsgi报错

  - 这是因为uwsgiconfig.py文件中，os.uname()是不支持windows系统的，platform模块是支持任何系统

  - [所以要用离线包安装才行](https://blog.csdn.net/qq_38327141/article/details/119819290)

    ```
    修改uwsgiconfig.py中的所有os.uname,将其改为platform.uname,在文件顶部添加import platform
    ```

  - **经检测，uwsgi里面的.h中的库都是linux的，windows没办法**
  
  - 拉倒吧













学到（要学）：P105

------

- :cloud: 我的CSDN：https://blog.csdn.net/qq_21579045
- :snowflake: 我的博客园：https://www.cnblogs.com/lyjun/
- :sunny: 我的Github：https://github.com/TinyHandsome
- :rainbow:  我的bilibili：https://space.bilibili.com/8182822

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
