# Djongo操作MongoDB新增字段

> 摘要：Djongo作为Django的扩展，支持Django原生语法操作MongoDB。但是我现在有一个需求，那就是能够在不修改models.py的情况下，对模型类的对象新增一个字段并赋值，同时，其他的数据直接获得这个新字段，并自动赋空值。这也是利用了MongoDB非关系型数据库的优势。
>
> 关键词：Django，Djongo，MongoDB，Python，ENFORCE_SCHEMA

1. 先说结论：行，但不完全行。

2. 什么意思呢，我们先看[官方文档-Get Started](https://www.djongomapper.com/get-started/)

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/42585c05929b4b22a163c9505859cbf9.png)

   - 搜索这个问题的程序员们肯定搜到这儿了，看了 **ENFORCE_SCHEMA** 这个字段的作用，一看Default，淦，默认的就是False了，怎么还是不行？

     > (Default) Implicitly creates collections. Returns missing fields as `None` instead of raising an exception.

   - 看到这儿很高兴，是不是这个描述就已经实现了你的需求了，别急，往下看。

3. 继续搜索这个关键字：**ENFORCE_SCHEMA**，我们想知道这个效果到底是怎么实现的呢？我搜遍了全网也没找到实现的Demo，只是在描述中略见星光。

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/68ffb39dbfb5426e856b0022375250ab.png)

   - 描述很舒服

     > You can add and exclude fields per entry and MongoDB will not complain. This can make life easier, especially when there are frequent changes to the data model.

   - 看到样例之后

     > The modified Model can be saved **without running any migrations**.

   - 也就是说，不经过任何迁移，修改的模型，也能被保存

   - 再看最后的描述

     > `ENFORCE_SCHEMA: False` works by silently setting the missing fields with the value `None`. If your app is programmed to expect this (which means it is not a bug) you can get away by not calling any migrations.

   - 也就是说，通过这种设置，也就是默认的设置：

     **不用做任何迁移，改变models.py，也可以实现增减字段的效果**

4. 结论：

   - 单纯的在views中操作变量的属性，比如新增一个没有的属性 `s.temp = '啊吧啊吧'`，然后 `s.save()`，这样做是行不通的。
   - 而是要去修改 `models.py` 中类的属性，即使不进行迁移，也不影响新数据的存储。


------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
