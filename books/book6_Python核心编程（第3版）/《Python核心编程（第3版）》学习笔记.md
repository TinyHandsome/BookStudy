# 《Python核心编程（第3版）》学习笔记

[TOC]

## 写在前面

- 读后感：
  - 真本书写的真的八行，外国人写的书，好的是真的好，烂的是真的烂，这本书不知道为什么吹的人那么多，烂的扣jio，有的例子真的不想抄一遍了，神神叨叨的，跑也跑不通，让自己填自己连接，我特么我知道怎么填，读你干嘛啊。还有啊，翻译得真跟shi一样，直接谷歌机翻也比这翻译的好吧。
  - 最严重的问题，也就是上面说的，很多例子对应的链接已经不行了，连也连不上，特别是**在第二章、第三章学网络的时候**，特别明显，就是学了个寂寞。
  - 怎么说呢，这本书无论是对初学者还是对已经有了一定基础的python学习者，**都十分的不友好**，我的评价是：**生硬且古板**。很多已经淘汰的技术，着墨太多，并且案例无法复现。很有很多错误的地方，比如英文打错了。。。我人都傻了，[点我查看打错的地方](#error1)
  - 数据库编程这一张是真的学的头痛，代码我一行都没敲，是真的跟不下去。就看了下逻辑和包，用的时候再去参考API吧，[特别是ORM](#2)
  - [扩展Python](#extension_python)这一章，本来我是真的很感兴趣的，可能是我水平不够叭，每个字我都认识，连在一起不知道在说什么，真的很痛苦，也没学到东西。（同样这章的吐槽，可以直达，[点我](#horse)）
  - 讲道理，这本书最大的作用，就是见证历史，看看远古操作是什么样的，**我们现在用python编程门槛这么低，都是站在巨人的肩膀上。**
  - 很累，真心累，学了个寂寞，重在参与吧

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201110153410970.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

## 1. 正则表达式

### 1.1 常用语法

- 正则表达式符号

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/2020111015351738.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

- 特殊字符

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210112153401819.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

- 择一匹配（或）：`|`

- 匹配任意单个字符：`.`，除了`\n`意外的任何字符

  怎样匹配`.`呢？：`\.`

- 匹配开头位置：`^`或者`\A`

- 匹配结尾位置：`$`或者`\Z`

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201113090646720.png#pic_center)

- 匹配字符边界：`\b`和`\B`

  - `\b`用于匹配一个单词的边界，开始

  - `\B`用于匹配不是单词边界，即不开始

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201113091002696.png#pic_center)

- 字符集的方法只适用于单字符的情况：`[abrd]`，否则应该使用：`ab|rd`

- 限定范围：`a-zA-Z0-9`

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201113105636268.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

- 使用闭包操作符实现**存在性**和**频数**的匹配

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201113110307806.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

- 表示字符集的特殊字符

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201113110407676.png#pic_center)

- 使用圆括号指定分组：提取任何已经成功匹配的特定字符串或者子字符串。

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201113110858962.png#pic_center)

- 扩展表示语法

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201113111135191.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

### 1.2 re模块

- 常见的正则表达式属性

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201113111311775.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

- 可选标记：

  - `re.IGNORECASE`：忽略大小写
  - `re.MULTILINE`：多行字符串匹配
  - `re.DOTALL`：`.`也包含换行符
  - `re.VERBOSE`：在正则表达式字符串中允许空白字符和注释，让它更可读。

- match()：从字符串的起始部分对模式进行匹配；如匹配成功，返回一个匹配对象；若匹配失败，则返回None。使用匹配对象的group()显示成功的匹配。

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201116134437212.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

- search()：search()的工作方式与match()完全一致，不同之处在于search()会用它的字符串参数，在任意位置对给定正则表达式模式搜索第一次出现的匹配情况。如果搜索到成功的匹配，就会返回一个匹配对象；否则，返回None。

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201116134857798.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

- 匹配多个字符串

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201116135629142.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

- 匹配任何单个字符

  `.`不能匹配一个换行符`\n`或者非字符，即空字符串。

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201116163325227.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

- 搜索真正的小数点

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201116164136328.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

- 创建字符集

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201118153805209.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

- 用`()`将所选的模式框选出来，然后在后面加上`?`表示出现0次或1次

- 重复、特殊字符以及分组

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201124095140411.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

- 添加一个子组来构造一个新的正则表达式

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201124100333687.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

- 提取上述正则表达式的字母和数字部分

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201124100547219.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

- group()通常用于以普通方式显示所有的匹配部分，但也能用于获
  取各个匹配的子组。可以使用groups()方法来获取一个包含所有匹配子字符串的元组。

  1. 表达式中没有括号

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201124100742997.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

  2. 表达式中有括号

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201124100938821.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

  3. 表达式中多个括号

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201124101044346.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

  4. 表达式中嵌套括号

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/2020112410120456.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

- 匹配字符串的起始和结尾以及单词边界

  1. 匹配+不作为起始+在边界

     单词边界是单词和空格之间的位置。这里检测到the是有边界的，然后从the前面的边界开始找the

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201124101546600.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

  2. 有边界+没有边界

     这里的`\B`找没有边界的the，并匹配边界后面的the

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201124101848239.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

- 在正则表达式字符串前记得加**原始字符串**：`r`

- findall()：

  - findall()查询字符串中某个正则表达式模式全部的非重复出现情况。这与search()在执行字符串搜索时类似，但与match()和search()的不同之处在于，findall()总是返回一个列表。如果findall()没有找到匹配的部分，就返回一个空列表，但如果匹配成功，列表将包含所有成功的匹配部分（从左向右按出现顺序排列）。

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201124102904510.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

- finditer():

  - finditer()函数是在Python 2.2 版本中添加回来的，这是一个与findall()函数类似但是更节省内存的变体。两者之间以及和其他变体函数之间的差异（很明显不同于返回的是一个迭代器还是列表）在于，和返回的匹配字符串相比，finditer()在匹配对象中迭代。
  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201124103603974.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)
  
  - 这里需要注意的是：如果`next()`报错，则需要改为`__next__()`
  
- 在单个字符串中执行单个分组的多重匹配

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201124104328364.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

- 用finditer()完成

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201124104449782.png#pic_center)

- 使用`sub()`和`subn()`搜索与替换

  - 有两个函数/方法用于实现搜索和替换功能：`sub()`和`subn()`。两者几乎一样，都是将某字符串中所有匹配正则表达式的部分进行某种形式的替换。用来替换的部分通常是一个字符串，但它也可能是一个函数，该函数返回一个用来替换的字符串。subn()和sub()一样，但subn()还返回一个表示替换的总数，替换后的字符串和表示替换总数的数字一起作为一个拥有两个元素的元组返回。

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201124105739210.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

  - 多组匹配

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201124105835759.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

- 根据分组结果，重新组合成新的结果

  使用匹配对象的group()方法除了能够取出匹配分组编号外，还可以使用\N，其中N 是在替换字符串中使用的分组编号。

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201124110552799.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

- 在限定模式上使用`split()`分隔字符串

  - 如果给定分隔符不是使用特殊符号来匹配多重模式的正则表达式，那么`re.split()`与`str.split()`的工作方式相同

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201124110913742.png#pic_center)

  - 复杂分割

    如果空格紧跟在五个数字（ZIP 编码）或者两个大写字母（美国联邦州缩写）之后，就用split 语句分割该空格。这就允许我们在城市名中放置空格。

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201124111752738.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

- 扩展符号

  - `re.I`和`re.M`实现多行混合

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201126091724406.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

  - `re.S/re.DOTALL`获取`\n`
  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201201174713889.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)
  
  - `re.X/re.VERBOSE`：在正则表达式字符串中允许空白字符和注释，让它更可读。
  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201201175346682.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)
  
  - `?:`：意思是不捕获分组，`(?:X)`这样表示X不作为一个分组，就是为了划分而已，不匹配。
  
    ```python
    re.findall(r'http://(?:\w+\.)*(\w+\.com)', 'http://google.com http://www.google.com http://code.google.com')
    
    # ['google.com', 'google.com', 'google.com']
    ```
  
  - `(?P<name>)`：给组命名为`name`
  
    通过使用一个名称标识符而不是使用从1 开始增加到N 的增量数字来保存匹配，如果使用数字来保存匹配结果，我们就可以通过使用`\1,\2 ...,\N`，`\`来检索
  
    ```python
    re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})', '(800) 555-1212').groupdict()
    
    # {'areacode': '800', 'prefix': '555'}
    ```
  
    ```python
    re.sub(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})', '(\g<areacode>) \g<prefix>-xxxx', '(800) 555-1212')
    
    # '(800) 555-xxxx'
    ```
  
  - `(?P=name)`：匹配前面已命名的组，比如验证号码是否符合规范
  
    ```python
    bool(re.match(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?P<number>\d{4}) (?P=areacode)-(?P=prefix)-(?P=number) 1(?P=areacode)(?P=prefix)(?P=number)', '(800) 555-1212 800-555-1212 18005551212'))
    
    # 好看的版本
    bool(re.match(r'''(?x)
        # 匹配(800) 555-1212，保存 areacode、prefix、no
        \((?P<areacode>\d{3})\) [ ] (?P<prefix>\d{3})-(?P<number>\d{4})
    
        # 空格
        [ ]
    
        # 匹配 800-555-1212
        (?P=areacode)-(?P=prefix)-(?P=number)
    
        # 空格
        [ ]
    
        # 匹配 18005551212
        1(?P=areacode)(?P=prefix)(?P=number)
    
        ''',
    
        '(800) 555-1212 800-555-1212 18005551212'
    ))
    
    # 结果如下
    # True
    ```
  
  - `(?=)`：正向前视断言
  
    如下，找到后面跟着` van Rossum`的字符串，不匹配`(?=)`本身
  
    ```python
    re.findall(r'\w+(?= van Rossum)', '''
    Guido van Rossum
    Tim Peters
    Alex Martelli
    Just van Rossum
    Raymond Hettinger
    ''')
    
    # ['Guido', 'Just']
    ```
  
  - `(?!)`：负向前视断言
  
    如下，找到后面不跟着`noreply`或`postmaster`的字符串，不匹配`(?!)`本身及以后
  
    ```python
    re.findall(r'(?m)^\s+(?!noreply|postmaster)(\w+)', 
    '''
        sales@phptr.com
        postmaster@phptr.com
        eng@phptr.com
        noreply@phptr.com
        adimn@phptr.com
    '''
    )
    
    # ['sales', 'eng', 'adimn']
    ```
  
  - 使用`finditer`循环遍历结果，生成list
  
    ```python
    ['%s@aw.com' % e.group(1) for e in re.finditer(r'(?m)^\s+(?!noreply|postmaster)(\w+)', 
    '''
        sales@phptr.com
        postmaster@phptr.com
        eng@phptr.com
        noreply@phptr.com
        adimn@phptr.com
    ''')]
    
    # ['sales@aw.com', 'eng@aw.com', 'adimn@aw.com']
    ```
  
  - `(?(num或name)X|Y)`：如果分组所提供的num或者变量名存在，则返回X，否则返回Y
  
    ```python
    bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xx'))
    # False
    
    bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'yx'))
    # True
    ```
  
    这里，如果第1个是x，则有编号1，即`(x)`；是y，则没有编号1。后面的如果前面有编号，则返回y，即xy；如果前面的没有编号，则返回x，即yx
  
    **注意：**`(?:)`指的是不捕获外面这个括号的分组，所以里面的x是捕获的，而`(x)|y`是不捕获的。
  
- 杂项

  - \w 和\W 字母数字字符集同时受re.L/LOCALE 和Unicode（re.U/UNICODE）标记所影响。

  - 退格符\b 和正则表达式\b 之间的差异

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201204171350697.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)


## 2. 网络编程

- 套接字：是计算机网络数据结构，socket。Socket是应用层与TCP/IP协议族通信的中间软件抽象层，它是一组接口。在设计模式中，Socket其实就是一个门面模式，它把复杂的TCP/IP协议族隐藏在Socket接口后面，对用户来说，一组简单的接口就是全部，让Socket去组织数据，以符合指定的协议。
- 有两种类型的套接字：**基于文件**的和**面向网络**的。
- 如果一个套接字像一个电话插孔——允许通信的一些基础设施，那么主机名和端口号就像区号和电话号码的组合

### 2.1 socket网络编程

- socket：套接字

- `socket(socket_family, socket_type, protocol=0)`：`socket_family`是AF_UNIX或AF_INET，`socket_type`是SOCK_STREAM或SOCK_DGRAM，`protocol`通常省略，默认为0。

  - 创建TCP/IP套接字：`tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
  - 创建UDP/IP套接字：`udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)`

- 常见的套接字对象方法和属性

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201216103303837.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)![在这里插入图片描述](https://img-blog.csdnimg.cn/20201216103331527.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

- 创建TCP服务器

  ```python
  from socket import *
  from time import ctime
  
  HOST = ''
  PORT = 21567
  BUFSIZ = 1024
  ADDR = (HOST, PORT)
  
  tcpSerSock = socket(AF_INET, SOCK_STREAM)
  tcpSerSock.bind(ADDR)
  tcpSerSock.listen(5)
  
  while True:
      print('等待连接...')
      tcpCliSock, addr =tcpSerSock.accept()
      print('...连接自：', addr)
  
      while True:
          data = tcpCliSock.recv(BUFSIZ)
          if not data:
              break
          tcpCliSock.send('[%s] %s' % (bytes(ctime(), 'utf-8'), data))
  
      tcpCliSock.close()
  tcpSerSock.close()
  ```

- 创建TCP客户端

  ```python
  from socket import *
  
  HOST = 'localhost'
  PORT = 21567
  BUFSIZ = 1024
  ADDR = (HOST, PORT)
  
  tcpCliSock = socket(AF_INET, SOCK_STREAM)
  tcpCliSock.connect(ADDR)
  
  while True:
      data = input('> ')
      if not data:
          break
      tcpCliSock.send(bytes(data, encoding="utf-8"))
      data = tcpCliSock.recv(BUFSIZ)
      if not data:
          break
      print(str(data, encoding="utf-8"))
  
  tcpCliSock.close()
  ```

- UDP 和TCP 服务器之间的另一个显著差异是，因为数据报套接字是无连接的，所以就没有为了成功通信而使一个客户端连接到一个独立的套接字“转换”的操作。这些服务器仅仅接受消息并有可能回复数据。

- UDP 客户端循环工作方式几乎和TCP 客户端完全一样。唯一的区别是，事先不需要建立与UDP 服务器的连接，只是简单地发送一条消息并等待服务器的回复。

- socket模块属性

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201226160257398.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)![在这里插入图片描述](https://img-blog.csdnimg.cn/20201226160322578.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

### 2.2 SocketServer 模块

1. 创建SocketServer TCP服务器

   ```python
   from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
   from time import ctime
   
   HOST = ''
   PORT = 21567
   ADDR = (HOST, PORT)
   
   
   class MyRequestHandler(SRH):
       def handle(self):
           print('...连自：', self.client_address)
           self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))
   
   
   tcpServ = TCP(ADDR, MyRequestHandler)
   print('等待连接...')
   tcpServ.serve_forever()
   ```

2. 创建SocketServer TCP 客户端

   ```python
   from socket import *
   
   HOST = 'localhost'
   PORT = 21567
   BUFSIZ = 1024
   ADDR = (HOST, PORT)
   
   while True:
       tcpCliSock = socket(AF_INET, SOCK_STREAM)
       tcpCliSock.connect(ADDR)
       data = input('> ')
       if not data:
           break
       tcpCliSock.send(bytes('%s\r\n' % data, encoding='utf-8'))
       data = tcpCliSock.recv(BUFSIZ)
       if not data:
           break
       print(str(data, encoding='utf-8').strip())
       tcpCliSock.close()
   ```

### 2.3 Twisted框架介绍

- 创建Twisted Reactor TCP 服务器

  ```python
  from twisted.internet import protocol, reactor
  from time import ctime
  
  PORT = 21567
  
  
  class TSServProtocol(protocol.Protocol):
      def connectionMade(self):
          clnt = self.clnt = self.transport.getPeer().host
          print('...连接自：', clnt)
  
      def dataReceived(self, data):
          self.transport.write(bytes('[%s] %s' % (ctime(), str(data, encoding='utf-8')), encoding='utf-8'))
  
  
  factory = protocol.Factory()
  factory.protocol = TSServProtocol
  print('等待连接...')
  reactor.listenTCP(PORT, factory)
  reactor.run()
  ```

- 创建Twisted Reactor TCP 客户端

  ```python
  from twisted.internet import protocol, reactor
  
  HOST = 'localhost'
  PORT = 21567
  
  
  class TSClntProtocol(protocol.Protocol):
      def sendData(self):
          data = input('> ')
          if data:
              print('...发送： %s...' % data)
              self.transport.write(bytes(data, encoding='utf-8'))
          else:
              self.transport.loseConnection()
  
      def connectionMade(self):
          self.sendData()
  
      def dataReceived(self, data):
          print(str(data, encoding='utf-8'))
          self.sendData()
  
  
  class TSClntFactory(protocol.ClientFactory):
      protocol = TSClntProtocol
      clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()
  
  
  reactor.connectTCP(HOST, PORT, TSClntFactory())
  reactor.run()
  ```

## 3. 因特网客户端编程

### 3.1 文件传输

1. 常见的文件传输协议：

   - HTTP
   - FTP
   - scp/rsync

2. FTP，File Transfer Protocol，文件传输协议

   - FTP只使用TCP，而不是UDP
   - FTP可以看作客户端/服务器编程中的特殊情况，因这里的客户端和服务器都使用两个套接字来通信：
     - 一个是控制和命令端口，21
     - 一个是数据端口，20
   - FTP有两种模式：主动和被动，只有在主动模式下服务器才使用数据端口。

3. 使用Python编写FTP客户端程序：

   - 流程：

       1. 连接到服务器
       2. 登录
       3. 发出服务请求
       4. 退出
       
   -  ftplib.FTP对象的方法：
   
       ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210104170327777.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)![在这里插入图片描述](https://img-blog.csdnimg.cn/20210104170352144.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)
   
   - 客户端FTP程序示例
   
       ```python
       import ftplib
       import os
       import socket
       
       HOST = 'ftp.mozilla.org'
       DIRN = 'pub/mozilla.org/webtools'
       FILE = 'bugzilla-LATEST.tar.gz'
       
       
       def main():
           # 创建一个FTP对象，尝试连接到FTP服务器
           try:
               f = ftplib.FTP(HOST)
           except (socket.error, socket.gaierror) as e:
               print('error: cannot reach "%s"' % HOST)
               return
           print('*** Connected to host "%s"' % HOST)
       
           # 尝试用anonymous登录
           try:
               f.login()
           except ftplib.error_perm:
               print('ERROR: cannot login anonymously')
               f.quit()
               return
           print('*** Logged in as "anonymous"')
           # 转到发布目录
           try:
               f.cwd(DIRN)
           except ftplib.error_perm:
               print('ERROR: cannot CD to "%s"' % DIRN)
               f.quit()
               return
           print('*** Changed to "%s" folder' % DIRN)
           # 下载文件
           try:
               f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)
           except ftplib.error_perm:
               print('ERROR: cannot read file "%s"' % FILE)
               os.unlink(FILE)
           else:
               print('*** Downloaded "%s" to CWD' % FILE)
           f.quit()
       
       
       if __name__ == '__main__':
           main()
       ```

### 3.2 网络新闻

- NNTP对象的方法

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210106175954253.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)
  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210106180036639.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

- 真本书的网络编程写的真的八行，外国人写的书，好的是真的好，烂的是真的烂，这本书不知道为什么吹的人那么多，烂的扣jio，这里的例子真的不想抄一遍了，神神叨叨的，跑也跑不通，学网络建议直接去看flask和django的书。

### 3.3 电子邮件

- MTA：传送代理，Mail Transfer Agent

- MTS：消息传输系统

- 为了发送电子邮件，邮件客户端必须要连接到一个MTA，MTA 靠某种协议进行通信。MTA之间通过消息传输系统（MTS）互相通信。只有两个MTA 都使用这个协议时，才能进行通信。

- SMTP：简单邮件传输协议，Simple Mail Transfer Protocol

- ESMTP：扩展 SMTP，Extended SMTP，对标准 SMTP 协议进行的扩展。它与 SMTP 服务的区别仅仅是，使用 SMTP 发信不需要验证用户帐户，而用 ESMTP 发信时，服务器会要求用户提供用户名和密码以便验证身份。在所有的验证机制中，信息全部采用Base64编码。验证之后的邮件发送过程与 SMTP 方式没有两样。

- LMTP：本地邮件传输协议，Local Mail Transfer Protocol。SMTP和SMTP服务扩展（ESMTP）提供了一种高效安全传送电子邮件的方法，而在实现SMTP时需要管理一个邮件传送队列，在有些时候这样做可能有麻烦，需要一种没有队列的邮件传送系统，而LMTP就是这样的一个系统，它使用ESMTP的语法，而它和ESMTP可不是一回事，而LMTP也不能用于TCP端口25。

- SMTP 是在因特网上的MTA 之间消息交换的最常用MTSMTA。用SMTP 把电子邮件从一台（MTA）主机传送到另一台（MTA）主机。发电子邮件时，必须要连接到一个外部SMTP服务器，此时邮件程序是一个SMTP 客户端。而SMTP 服务器也因此成为消息的第一站。

- MUA：Mail User Agent，邮件用户代理，在家用电脑中运行的应用程序。

- POP：Post Office Protocal，邮局协议，第一个用于下载邮件的协议。

- IMAP：Internet Message Access Protocol，因特网消息访问协议。

  > POP无法很好地应对多邮件客户端，因此现在被废弃了，IMAP4rev1现在广泛使用。

- MIME，Mail Interchange Message Extension，邮件呼唤消息扩展（这啥呀，百度都搜不到，搜到的是Multipurpose Internet Mail Extensions，**多用途互联网邮件扩展类型**，这本书真的没有瞎编吗，还是译者瞎翻译？）

### 3.4 实战

- 憋实战了叭，根本跑不通

  ```python
  from email.mime.image import MIMEImage
  from email.mime.multipart import MIMEMultipart
  from email.mime.text import MIMEText
  from smtplib import SMTP
  
  
  def make_mpa_msg():
      email = MIMEMultipart('alternative')
      text = MIMEText('Hello World!\r\n', 'plain')
      email.attach(text)
      html = MIMEText('<html><body><h4>Hello World!</h4></body></html>', 'html')
      email.attach(html)
      return email
  
  
  def make_img_msg(fn):
      f = open(fn, 'r')
      data = f.read()
      f.close()
      email = MIMEImage(data, name=fn)
      email.add_header('Content-Dispostion', 'attachment; filename="%s"' % fn)
      return email
  
  
  def sendMsg(fr, to, msg):
      s = SMTP('localhost')
      errs = s.sendmail(fr, to, msg)
      s.quit()
  
  
  if __name__ == '__main__':
      print('Sending multipart alternative msg...')
      msg = make_mpa_msg()
  
      SENDER = ''
      RECIPS = ''
      SOME_IMG_FILE = r''
  
      msg['From'] = SENDER
      msg['To'] = ', '.join(RECIPS)
      msg['Subject'] = 'multipart alternative test'
      sendMsg(SENDER, RECIPS, msg.as_string())
  
      print(('Sending image msg...'))
      msg = make_img_msg(SOME_IMG_FILE)
      msg['From'] = SENDER
      msg['To'] = ', '.join(RECIPS)
      msg['Subject'] = 'Image file test'
      sendMsg(SENDER, RECIPS, msg.as_string())
  ```

- <a name = 'error1'>SaaS：Software as a Service，软件即服务（这里的Service书中还打错了。。。我佛了）</a>

- 使用`timeit`查看代码运行时长

- TLS：Transport Layer Security，传输层安全

## 4. 多线程编程

### 4.1 线程和进程

1. 多线程：multithreaded，MT

2. IPC：Inter-Process Communication，进程间通信

3. 线程包括开始、执行顺序和结束三部分。它有一个指令指针，用于记录当前运行的上下文。当其他线程运行时，它可以被抢占（中断）和临时挂起（也称为睡眠）——这种做法叫做让步（yielding）。

4. GIL：Global Interpreter Lock，全局解释器锁

5. **不建议使用thread模块**：，其中最明显的一个原因是在主线程退出之后，所有其他线程都会在没有清理的情况下直接退出。而另一个模块threading 会确保在所有“重要的”子线程退出前，保持整个进程的存活。

6. 下面的脚本在一个单线程程序里连续执行两个循环。一个循环必须在另一个开始前完成。总共消耗的时间是每个循环所用时间之和。

   ```python
   from time import sleep, ctime
   
   
   def loop0():
       print('start loop 0 at: ', ctime())
       sleep(4)
       print('loop 0 done at: ', ctime())
   
   
   def loop1():
       print('start loop 1 at: ', ctime())
       sleep(2)
       print('loop 1 done at:', ctime())
   
   
   def main():
       print('starting at: ', ctime())
       loop0()
       loop1()
       print('all Done at: ', ctime())
   
   
   if __name__ == '__main__':
       main()
   ```

### 4.2 thread

1. thread模块和锁对象

   - 锁对象：lock object，原语锁、简单锁、互斥锁、互斥和二进制信号锁。

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210111103654255.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

2. `thread.start_new_thread()`必须包含开始的两个参数，于是即使要执行的函数不需要参数，也需要传递一个空元组。这里需要注意的是，在python3中想要使用thread，导入的是`_thread`

   ```python
   import _thread as thread
   from time import sleep, ctime
   
   
   def loop0():
       print('start loop 0 at: ', ctime())
       sleep(4)
       print('loop 0 done at: ', ctime())
   
   
   def loop1():
       print('start loop 1 at: ', ctime())
       sleep(2)
       print('loop 1 done at: ', ctime())
   
   
   def main():
       print('starting at: ', ctime())
       thread.start_new_thread(loop0, ())
       thread.start_new_thread(loop1, ())
       sleep(6)
       print('all DONE at: ', ctime())
   
   
   if __name__ == '__main__':
       main()
   ```

3. 引入锁，并去除单独的循环函数

   ```python
   import _thread as thread
   from time import sleep, ctime
   
   loops = [4, 2]
   
   
   def loop(nloop, nsec, lock):
       print('start loop', nloop, 'at: ', ctime())
       sleep(nsec)
       print('loop', nloop, 'done at:', ctime())
       lock.release()
   
   
   def main():
       print('starting at: ', ctime())
       locks = []
       nloops = range(len(loops))
   
       # 首先创建一个锁列表
       for i in nloops:
           # 得到锁对象，获取锁需要花费一些时间
           lock = thread.allocate_lock()
           # 获得每个锁，把锁锁上
           lock.acquire()
           locks.append(lock)
   
       for i in nloops:
           thread.start_new_thread(loop, (i, loops[i], locks[i]))
   
       # 等待/暂停主线程，直到所有锁都被释放之后才会继续执行。
       for i in nloops:
           while locks[i].locked():
               pass
   
       print('all Done at: ', ctime())
   
   
   if __name__ == '__main__':
       main()
   ```

### 4.3 threading

1. thread仅供学习用，正常用的话，都选threading。除了Thread 类以外，该模块还包括许多非常好用的同步机制。

   > 避免使用thread 模块的另一个原因是该模块不支持守护线程这个概念。当主线程退出时，所有子线程都将终止，不管它们是否仍在工作。如果你不希望发生这种行为，就要引入守护线程的概念了。

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210111111802159.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

2. 守护线程：进程退出时不需要等待这个线程执行完成。

3. threading 模块的Thread 类是主要的执行对象

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210111151123952.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)
   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210111151153636.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

4. 使用Thread的方法：

   1. 创建Thread 的实例，传给它一个函数。

      ```python
      import threading
      from time import sleep, ctime
      
      loops = [4, 2]
      
      
      def loop(nloop, nsec):
          print('start loop', nloop, 'at: ', ctime())
          sleep(nsec)
          print('loop', nloop, 'done at:', ctime())
      
      
      def main():
          print('starting at: ', ctime())
          threads = []
          nloops = range(len(loops))
      
          for i in nloops:
              t = threading.Thread(target=loop, args=(i, loops[i]))
              threads.append(t)
      
          for i in nloops:
              threads[i].start()
      
          for i in nloops:
              threads[i].join()
      
          print('all Done at: ', ctime())
      
      
      if __name__ == '__main__':
          main()
      ```

   2. 创建Thread 的实例，传给它一个可调用的类实例。

      ```python
      import threading
      from time import sleep, ctime
      
      loops = [4, 2]
      
      
      class ThreadFunc(object):
          def __init__(self, f, args, name=''):
              self.name = name
              self.f = f
              self.args = args
      
          def __call__(self):
              self.f(*self.args)
      
      
      def loop(nloop, nsec):
          print('start loop', nloop, 'at: ', ctime())
          sleep(nsec)
          print('loop', nloop, 'done at:', ctime())
      
      
      def main():
          print('starting at: ', ctime())
          threads = []
          nloops = range(len(loops))
      
          for i in nloops:
              t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
              threads.append(t)
      
          for i in nloops:
              threads[i].start()
      
          for i in nloops:
              threads[i].join()
      
          print('all Done at: ', ctime())
      
      
      if __name__ == '__main__':
          main()
      ```

   3. 派生Thread 的子类，并创建子类的实例。

      对Thread 子类化，而不是直接对其实例化。这将使我们在定制线程对象时拥有更多的灵活性，也能够简化线程创建的调用过程。

      运行时**报错**：`AssertionError: Thread.__init__() not called`

      解决方案：这是因为在子类的初始化函数中没有初始化父类初始化函数，所以需要加上：`super().__init__()`

      ```python
      import threading
      from time import sleep, ctime
      
      loops = [4, 2]
      
      
      class MyThread(threading.Thread):
          def __init__(self, f, args, name=''):
              super().__init__()
              self.name = name
              self.f = f
              self.args = args
      
          def run(self):
              self.f(*self.args)
      
      
      def loop(nloop, nsec):
          print('start loop', nloop, 'at: ', ctime())
          sleep(nsec)
          print('loop', nloop, 'done at:', ctime())
      
      
      def main():
          print('starting at: ', ctime())
          threads = []
          nloops = range(len(loops))
      
          for i in nloops:
              t = MyThread(loop, (i, loops[i]), loop.__name__)
              threads.append(t)
      
          for i in nloops:
              threads[i].start()
      
          for i in nloops:
              threads[i].join()
      
          print('all Done at: ', ctime())
      
      
      if __name__ == '__main__':
          main()
      ```

5. 实例化`Thread（调用Thread()）`和调用`thread.start_new_thread()`的最大区别是新线程**不会立即开始执行**。

6. `join()`方法将**等待线程结束**，或者在提供了超时时间的情况下，达到超时时间。使用`join()`方法要比等待锁释放的无限循环更加清晰（这也是这种锁又称为**自旋锁**的原因）。

7. `__call__()`方法：主要实现的是将类的对象当作函数直接调用。

8. 之前的特殊方法`__call__()`在这个子类中必须要写为`run()`。

9. `threading` 模块的其他函数

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210111162054771.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

### 4.4 单线程和多线程执行对比

1. 为了让`Thread` 的子类更加通用，将这个子类移到一个专门的模块中，并添加了可调用的`getResult()`方法来取得返回值。

   ```python
   import threading
   from time import ctime
   
   
   class MyThread(threading.Thread):
       def __init__(self, func, args, name=''):
           super().__init__()
           self.name = name
           self.func = func
           self.args = args
           self.res = None
   
       def __post_init__(self):
           super().__init__()
   
       def getResult(self):
           return self.res
   
       def run(self):
           print('starting', self.name, 'at: ', ctime())
           self.res = self.func(*self.args)
           print(self.name, 'finished at: ', ctime())
   ```

2. 单线程执行斐波那契、阶乘和累加

   ```python
   from myThread import MyThread
   from time import ctime, sleep
   
   
   def fib(x):
       sleep(0.005)
       if x < 2:
           return 1
       return (fib(x-2) + fib(x-1))
   
   
   def fac(x):
       sleep(0.1)
       if x < 2:
           return 1
       return (x * fac(x-1))
   
   
   def sums(x):
       sleep(0.1)
       if x < 2:
           return 1
       return (x + sums(x-1))
   
   
   funcs = [fib, fac, sums]
   n = 12
   
   
   def main():
       nfuncs = range(len(funcs))
   
       print('*** SINGLE THREAD')
       for i in nfuncs:
           print('starting', funcs[i].__name__, 'at: ', ctime())
           print(funcs[i](n))
           print(funcs[i].__name__, 'finished at: ', ctime())
   
       print('\n*** MULTIPLE THREADS')
       threads = []
       for i in nfuncs:
           t = MyThread(funcs[i], (n, ), funcs[i].__name__)
           threads.append(t)
   
       for i in nfuncs:
           threads[i].start()
   
       for i in nfuncs:
           threads[i].getResult()
   
       print('all DONE')
   
   
   if __name__ == '__main__':
       main()
   ```

### 4.5 多线程实践

- 函数名最前面的单下划线表示这是一个特殊函数，只能被本模块的代码使用，不能被其他使用本文件作为库或者工具模块的应用导入。

- 同步：

  - 需求背景：如果两个线程运行的顺序发生变化，就有可能造成代码的执行轨迹或行为不相同，或者产生不一致的数据。（比如数据库写入内容，读取内容）
  - 含义：当任意数量的线程可以访问临界区的代码，但在给定的时刻只有一个线程可以通过时，就是使用同步的时候了。

- 当多线程争夺锁时，允许第一个获得锁的线程进入临界区，并执行代码。所有之后到达的线程将被阻塞，直到第一个线程执行结束，退出临界区，并释放锁。

  ```python
  from atexit import register
  from random import randrange
  from threading import Thread, Lock, currentThread
  from time import sleep, ctime
  
  
  class CleanOutputSet(set):
      def __str__(self):
          return ', '.join(x for x in self)
  
  
  lock = Lock()
  loops = (randrange(2, 5) for x in range(randrange(3, 7)))
  remaining = CleanOutputSet()
  
  
  def loop(nsec):
      myname = currentThread().name
      lock.acquire()
      remaining.add(myname)
      print('[%s] Started %s' % (ctime(), myname))
      lock.release()
      sleep(nsec)
      lock.acquire()
      remaining.remove(myname)
      print('[%s] Completed %s (%d secs)' % (ctime(), myname, nsec))
      print('(remaining: %s)' % (remaining or 'None'))
      lock.release()
  
  
  def _main():
      for pause in loops:
          Thread(target=loop, args=(pause, )).start()
  
  
  @register
  def _atexit():
      print('all DONE at: ', ctime())
  
  
  if __name__ == '__main__':
      _main()
  ```

- 使用上下文管理：还有一种方案可以不再调用锁的acquire()和release()方法，从而更进一步简化代码。这就是使用`with 语句`，此时每个对象的上下文管理器负责在进入该套件之前调用acquire()并在完成执行之后调用release()。

- 信号量：信号量是最古老的同步原语之一。它是一个计数器，当资源消耗时递减，当资源释放时递增。信号量代表资源是否可用。信号量比锁更加灵活，因为可以有多个线程，每个线程拥有有限资源的一个实例。

  ```python
  from atexit import register
  from random import randrange
  from threading import BoundedSemaphore, Lock, Thread
  from time import sleep, ctime
  
  
  lock = Lock()
  MAX = 5
  candytray = BoundedSemaphore(MAX)
  
  
  def refill():
      lock.acquire()
      print('Refilling candy...')
      try:
          candytray.release()
      except ValueError:
          print('full, skipping')
      else:
          print('OK')
      lock.release()
  
  
  def buy():
      lock.acquire()
      print('Buy candy...')
      if candytray.acquire(False):
          print('OK')
      else:
          print('empty, skipping')
      lock.release()
  
  
  def producer(loops):
      for i in range(loops):
          refill()
          sleep(randrange(3))
  
  
  def consumer(loops):
      for i in range(loops):
          buy()
          sleep(randrange(3))
  
  def _main():
      print('starting at:', ctime())
      nloops=randrange(2, 6)
      print('THE CANDY MACHINE (full with %d bars)' % MAX)
      Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2),)).start()
      Thread(target=producer, args=(nloops,)).start()
  
  @register
  def _atexit():
      print('all Done at: ', ctime())
  
  if __name__ == '__main__':
      _main()
  ```

### 4.6 Queue模块

- Queue/queue模块常用属性

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210112140654921.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)
  ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021011214081143.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

- 生产消费者问题

  ```python
  from random import randint
  from time import sleep
  from queue import Queue
  from myThread import MyThread
  
  def writeQ(queue):
      print('producing object for Q...', end='')
      queue.put('xxx', 1)
      print('size now', queue.qsize())
  
  def readQ(queue):
      val = queue.get(1)
      print('consumed object from Q...size now', queue.qsize())
  
  def writer(queue, loops):
      for i in range(loops):
          writeQ(queue)
          sleep(randint(1, 3))
  
  def reader(queue, loops):
      for i in range(loops):
          readQ(queue)
          sleep(randint(3, 5))
  
  funcs = [writer, reader]
  nfuncs = range(len(funcs))
  
  def main():
      nloops = randint(2, 5)
      q = Queue(maxsize=32)
  
      threads = []
      for i in nfuncs:
          t = MyThread(funcs[i], [q, nloops], funcs[i].__name__)
          threads.append(t)
  
      for i in nfuncs:
          threads[i].start()
  
      for i in nfuncs:
          threads[i].join()
  
      print('all DONE')
  
  if __name__ == '__main__':
      main()
  ```

### 4.7 线程的替代方案

- 由于Python 的GIL 的限制，多线程更适合于I/O 密集型应用（I/O 释放了GIL，可以允许更多的并发），而不是计算密集型应用。对于后一种情况而言，为了实现更好的并行性，你需要使用多进程，以便让CPU 的其他内核来执行。

- 对于多线程或多进程而言，threading模块的主要替代品包括以下几个：

  1. subprocess
  2. multiprocessing
  3. concurrent.futures
     - I/O密集型应用：concurrent.futures.ThreadPoolExecutor
     - 计算密集型应用：concurrent.futures.ProcessPoolExecutor

- 使用`concurrent.futures`模块的图书排名

  ```python
  from concurrent.futures import ThreadPoolExecutor
  from re import compile
  from time import ctime
  from urllib.request import urlopen as uopen
  
  REGEX = compile(b'#([\d,]+) in Books ')
  AMZN = 'http://amazon.com/dp/'
  ISBNs = {
      '0132269937': 'Core Python Programming',
      '0132356139': 'Python Web Development with Django',
      '0137143419': 'Python Fundamentals'
  }
  
  def getRanking(isbn):
      with uopen('{0}{1}'.format(AMZN, isbn)) as page:
          return str(REGEX.findall(page.read())[0], 'utf-8')
  
  def _main():
      print('At', ctime(), 'on Amazon...')
      with ThreadPoolExecutor(3) as executor:
          for isbn, ranking in zip(ISBNs, executor.map(getRanking, ISBNs)):
              print('- %r ranked %s' % (ISBNs[isbn], ranking))
  
      print('all DONE at: ', ctime())
  
  if __name__ == '__main__':
      _main()
  ```

- 相关模块总结

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210113135321464.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

- 一些问题：

  1. [进程和线程的区别是什么？](https://blog.csdn.net/kuangsonghan/article/details/80674777)

     根本区别：进程是操作系统资源分配的基本单位，而线程是任务调度和执行的基本单位。

     在开销方面：每个进程都有独立的代码和数据空间（程序上下文），程序之间的切换会有较大的开销；线程可以看做轻量级的进程，同一类线程共享代码和数据空间，每个线程都有自己独立的运行栈和程序计数器（PC），线程之间切换的开销小。

     所处环境：在操作系统中能同时运行多个进程（程序）；而在同一个进程（程序）中有多个线程同时执行（通过CPU调度，在每个时间片中只有一个线程执行）

     内存分配方面：系统在运行的时候会为每个进程分配不同的内存空间；而对线程而言，除了CPU外，系统不会为线程分配内存（线程所使用的资源来自其所属进程的资源），线程组之间只能共享资源。

     包含关系：没有线程的进程可以看做是单线程的，如果一个进程内有多个线程，则执行过程不是一条线的，而是多条线（线程）共同完成的；线程是进程的一部分，所以线程也被称为轻权进程或者轻量级进程。

  2. 在Python 中，哪种类型的多线程应用表现得更好，I/O 密集型还是计算密集型？

     由于Python 的GIL 的限制，多线程更适合于I/O 密集型应用（I/O 释放了GIL，可以允许更多的并发），而不是计算密集型应用。对于后一种情况而言，为了实现更好的并行性，你需要使用多进程，以便让CPU 的其他内核来执行。

## 5. GUI编程

### 5.1 概述

- GUI：图形用户界面，Graphical User Interface。

- Tkinter是python默认的GUI库，基于Tk工具包，该工具包最初是为 **工具命令语言** （Tool Command Language，Tcl）设计的。

- Tk控件：

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210113143322245.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

### 5.2 示例

1. Label控件

   ```python
   import tkinter as tk
   
   top = tk.Tk()
   label = tk.Label(top, text='Hello World')
   label.pack()
   tk.mainloop()
   ```

2. Button控件

   ```python
   import tkinter as tk
   
   top = tk.Tk()
   quit = tk.Button(top, text='Hello World', command=top.quit)
   quit.pack()
   tk.mainloop()
   ```

3. label和button控件演示

   ```python
   import tkinter as tk
   top = tk.Tk()
   
   hello = tk.Label(top, text='Hello World!')
   hello.pack()
   
   quit = tk.Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
   quit.pack(fill=tk.X, expand=1)
   tk.mainloop()
   ```

4. label、button和scale控件

   ```python
   import tkinter as tk
   
   def resize(ev=None):
       label.config(font='Helvetica -%d bold' % scale.get())
   
   top = tk.Tk()
   top.geometry('250x150')
   
   label = tk.Label(top, text='Hello World!', font='Helvetica -12 bold')
   label.pack()
   
   scale = tk.Scale(top, from_=10, to=40, orient=tk.HORIZONTAL, command=resize)
   scale.set(12)
   scale.pack(fill=tk.X, expand=1)
   
   quit = tk.Button(top, text='QUIT', command=top.quit, activeforeground='white', activebackground='red')
   quit.pack()
   
   tk.mainloop()
   ```

### 5.3 偏函数

- 根据标志类型创建拥有合适前景色和背景色的路标。使用偏函数可以帮助你“模板化”通用的GUI 参数。

  ```python
  from functools import partial as pto
  from tkinter import Tk, Button, X
  from tkinter.messagebox import showinfo, showwarning, showerror
  
  WARN = 'warn'
  CRIT = 'crit'
  REGU = 'regu'
  
  SIGNS = {
      'do not enter': CRIT,
      'railroad crossing': WARN,
      '55\nspeed limit': REGU,
      'wrong way': CRIT,
      'merging traffic': WARN,
      'one way': REGU,
  }
  
  critCB = lambda: showerror('Error', 'Error Button Pressed!')
  warnCB = lambda: showwarning('Warning', 'Warning Button Pressed!')
  infoCB = lambda: showinfo('Info', 'Info Button Pressed!')
  
  top = Tk()
  top.title('Road Signs')
  Button(top, text='Quit', command=top.quit, bg='red', fg='white').pack()
  MyButton = pto(Button, top)
  CritButton = pto(MyButton, command=critCB, bg='white', fg='red')
  WarnButton = pto(MyButton, command=warnCB, bg='goldenrod1')
  ReguButton = pto(MyButton, command=infoCB, bg='white')
  
  for eachSign in SIGNS:
      # 获取每个字典的值
      signType = SIGNS[eachSign]
      # 获取值的.title()也就是第一个字母大写，对应了不同的Button
      cmd = '%sButton(text=%r%s).pack(fill=X, expand=True)' % (signType.title(), eachSign, '.upper()' if signType == CRIT else '.title()')
      eval(cmd)
  
  top.mainloop()
  ```

- [`functools`详解](https://blog.csdn.net/qq_1290259791/article/details/84930850)

  1. patial

     > 用于创建一个偏函数，将默认参数包装一个可调用对象，返回结果也是可调用对象。
     > 偏函数可以固定住原函数的部分参数，从而在调用时更简单。

     ```python
     from functools import partial
     
     def add(a, b):
         return a+b
     
     addOne = partial(add, 10)
     print(add(1, 2))
     # 3
     print(addOne(1))
     # 11
     ```

  2. update_wrapper

     > 使用 `partial` 包装的函数是没有`__name__`和`__doc__`属性的。
     > `update_wrapper` 作用：将被包装函数的`__name__`等属性，拷贝到新的函数中去。	

     ```python
     from functools import update_wrapper
     def wrapper(f):
         def wrapper_function(*args, **kwargs):
             """这个是修饰函数"""
             return f(*args, **kwargs)
         return wrapper_function
     
     @wrapper
     def wrapped():
         """这个是被修饰的函数"""
         print('wrapped')
     
     print(wrapped.__doc__)      # 这个是修饰函数
     print(wrapped.__name__)     # wrapper_function
     
     def wrapper2(f):
         def wrapper_function2(*args, **kwargs):
             """这个是修饰函数"""
             return f(*args, **kwargs)
         update_wrapper(wrapper_function2, f)
         return wrapper_function2
     
     @wrapper2
     def wrapped2():
         """这个是被修饰的函数"""
         print('wrapped')
     
     print(wrapped2.__doc__)      # 这个是被修饰的函数
     print(wrapped2.__name__)     # wrapped2
     ```

  3. wraps

     > `warps` 函数是为了在装饰器拷贝被装饰函数的`__name__`。
     > 就是在`update_wrapper`上进行一个包装

     ```python
     from functools import wraps
     
     def wrap1(func):
         # 去掉就会返回inner
         @wraps(func)
         def inner(*args):
             print(func.__name__)
             return func(*args)
         return inner
     
     
     @wrap1
     def demo():
         print('Hello World!')
     
     print(demo.__name__)        # demo
     ```

  4. reduce

     > 在 Python2 中等同于内建函数 reduce
     > 函数的作用是将一个序列归纳为一个输出
     > reduce(function, sequence, startValue)

     ```python
     在 Python2 中等同于内建函数 reduce
     函数的作用是将一个序列归纳为一个输出
     reduce(function, sequence, startValue)
     ```

  5. cmp_to_key

     > 在 list.sort 和 内建函数 sorted 中都有一个 key 参数

     ```python
     x = ['hello', 'world', 'ni']
     x.sort(key=len)
     print(x)
     
     from functools import cmp_to_key
     ll = [9, 2, 23, 1, 2]
     print(sorted(ll, key=cmp_to_key(lambda x, y: y - x)))
     print(sorted(ll, key=cmp_to_key(lambda x, y: x - y)))
     ```

  6. lru_cache

     > 允许我们将一个函数的返回值快速地缓存或取消缓存。
     > 该装饰器用于缓存函数的调用结果，对于需要多次调用的函数，而且每次调用参数都相同，则可以用该装饰器缓存调用结果，从而加快程序运行。
     > 该装饰器会将不同的调用结果缓存在内存中，因此需要注意内存占用问题。

     ```python
     from functools import lru_cache
     
     # maxsize参数告诉lru_cache混村最近多少个返回值
     @lru_cache(maxsize=30)
     def fib(n):
         if n < 2:
             return n
         return fib(n-1) + fib(n-2)
     
     print([fib(n) for n in range(10)])
     fib.cache_clear()
     ```

  7. singledispatch

     > 单分发器， Python3.4新增，用于实现泛型函数。
     > 根据单一参数的类型来判断调用哪个函数。

     ```python
     from functools import singledispatch
     
     @singledispatch
     def fun(text):
         print('String: ' + text)
     
     @fun.register(int)
     def _(text):
         print(text)
     
     @fun.register(list)
     def _(text):
         for k, v in enumerate(text):
             print(k, v)
     
     @fun.register(float)
     @fun.register(tuple)
     def _(text):
         print('float, tuple')
     
     fun('i am is gouzei')
     fun(123)
     fun(['a', 'b', 'c', 'd'])
     fun(1.243)
     print(fun.registry)
     print(fun.registry[int])
     ```

### 5.4 中级Tkinter

- 这个应用是一个目录树遍历工具。它会从当前目录开始，提供一个文件列表。双击列表中任意其他目录，就会使得工具切换到新目录中，用新目录中的文件列表代替旧文件列表。

- `hasattr()`：[该函数用于判断对象是否包含对应的属性。](https://blog.csdn.net/brucewong0516/article/details/82813219)

- `os.chdir() `：[用于改变当前工作目录到指定的路径。](https://www.runoob.com/python/os-chdir.html)

- 实现代码：

  ```python
  import os
  from time import sleep
  from tkinter import *
  
  class DirList(object):
      def __init__(self, initdir=None):
          self.top = Tk()
          self.label = Label(self.top, text='Directory Lister v1.1')
          self.label.pack()
  
          self.cwd = StringVar(self.top)
  
          self.dirl = Label(self.top, fg='blue', font=('Helvetica', 12, 'bold'))
          self.dirl.pack()
  
          self.dirfm = Frame(self.top)
          self.dirsb = Scrollbar(self.dirfm)
          self.dirsb.pack(side=RIGHT, fill=Y)
          self.dirs = Listbox(self.dirfm, height=15, width=50, yscrollcommand=self.dirsb.set)
          self.dirs.bind('<Double-1>', self.setDirAndGo)
          self.dirsb.config(command=self.dirs.yview)
          self.dirs.pack(side=LEFT, fill=BOTH)
          self.dirfm.pack()
  
          self.dirn = Entry(self.top, width=50, textvariable=self.cwd)
          self.dirn.bind('<Return>', self.doLS)
          self.dirn.pack()
  
          self.bfm = Frame(self.top)
          self.clr = Button(self.bfm, text='Clear', command=self.clrDir, activeforeground='white', activebackground='blue')
          self.ls = Button(self.bfm, text='List Directory', command=self.doLS, activeforeground='white', activebackground='green')
          self.quit = Button(self.bfm, text='Quit', command=self.top.quit, activeforeground='white', activebackground='red')
          self.clr.pack(side=LEFT)
          self.ls.pack(side=LEFT)
          self.quit.pack(side=LEFT)
          self.bfm.pack()
  
          if initdir:
              self.cwd.set(os.curdir)
              self.doLS()
  
      def clrDir(self, ev=None):
          self.cwd.set("")
  
      def setDirAndGo(self, ev=None):
          self.last = self.cwd.get()
          self.dirs.config(selectbackground='red')
          check = self.dirs.get(self.dirs.curselection())
          if not check:
              check = os.curdir
          self.cwd.set(check)
          self.doLS()
  
      def doLS(self, ev=None):
          error = ''
          tdir = self.cwd.get()
          if not tdir:
              tdir = os.curdir
  
          if not os.path.exists(tdir):
              error = tdir + ': no such file'
          elif not os.path.isdir(tdir):
              error = tdir + ': not a directory'
  
          if error:
              self.cwd.set(error)
              self.top.update()
              sleep(2)
              if not (hasattr(self, 'last') and self.last):
                  self.last = os.curdir
              self.cwd.set(self.last)
              self.dirs.config(selectbackground='LightSkyBlue')
              self.top.update()
              return
  
          self.cwd.set('FETCHING DIRECTORY CONTENTS...')
          self.top.update()
          dirlist = os.listdir(tdir)
          dirlist.sort()
          os.chdir(tdir)
  
          self.dirl.config(text=os.getcwd())
          self.dirs.delete(0, END)
          self.dirs.insert(END, os.curdir)
          self.dirs.insert(END, os.pardir)
          for eachFile in dirlist:
              self.dirs.insert(END, eachFile)
  
          self.cwd.set(os.curdir)
          self.dirs.config(selectbackground='LightSkyBlue')
  
  def main():
      d = DirList(os.curdir)
      mainloop()
  
  if __name__ == '__main__':
      main()
  ```


### 5.5 其他GUI简介

1. Tk接口扩展（Tix）

   ```python
   from functools import partial as pto
   from tkinter import Tk, Button, X
   from tkinter.messagebox import showinfo, showwarning, showerror
   
   WARN = 'warn'
   CRIT = 'crit'
   REGU = 'regu'
   
   SIGNS = {
       'do not enter': CRIT,
       'railroad crossing': WARN,
       '55\nspeed limit': REGU,
       'wrong way': CRIT,
       'merging traffic': WARN,
       'one way': REGU,
   }
   
   critCB = lambda: showerror('Error', 'Error Button Pressed!')
   warnCB = lambda: showwarning('Warning', 'Warning Button Pressed!')
   infoCB = lambda: showinfo('Info', 'Info Button Pressed!')
   
   top = Tk()
   top.title('Road Signs')
   Button(top, text='Quit', command=top.quit, bg='red', fg='white').pack()
   MyButton = pto(Button, top)
   CritButton = pto(MyButton, command=critCB, bg='white', fg='red')
   WarnButton = pto(MyButton, command=warnCB, bg='goldenrod1')
   ReguButton = pto(MyButton, command=infoCB, bg='white')
   
   for eachSign in SIGNS:
       # 获取每个字典的值
       signType = SIGNS[eachSign]
       # 获取值的.title()也就是第一个字母大写，对应了不同的Button
       cmd = '%sButton(text=%r%s).pack(fill=X, expand=True)' % (signType.title(), eachSign, '.upper()' if signType == CRIT else '.title()')
       eval(cmd)
   
   top.mainloop()
   ```
   
2. Python MegaWidgets（PMW）

   ```python
   from tkinter import Button, END, Label, W
   from Pmw import initialise, ComboBox, Counter
   
   top = initialise()
   lb = Label(top, text='Animals (in pairs; min: pair, max: dozen)')
   lb.pack()
   
   ct = Counter(top, labelpos=W, label_text='Number: ', datatype='integer', entryfield_value=2, increment=2, entryfield_validate={'validator': 'integer', 'min': 2, 'max': 12})
   ct.pack()
   
   cb = ComboBox(top, labelpos=W, label_text='Type: ')
   for animal in ('dog', 'cat', 'hamster', 'python'):
       cb.insert(END, animal)
   cb.pack()
   
   qb = Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
   qb.pack()
   
   top.mainloop()
   ```

3. wxWidgets和wxPython

   ```python
   import wx
   class MyFrame(wx.Frame):
       def __init__(self, parent=None, id=-1, title=""):
           wx.Frame.__init__(self, parent, id, title, size=(200, 140))
           top = wx.Panel(self)
           sizer = wx.BoxSizer(wx.VERTICAL)
           font = wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD)
           lb = wx.StaticText(top, -1, 'Animals (in pairs; min: pair, max: dozen)')
           sizer.Add(lb)
   
           c1 = wx.StaticText(top, -1, 'Number: ')
           c1.SetFont(font)
           ct = wx.SpinCtrl(top, -1, '2', min=2, max=12)
           sizer.Add(c1)
           sizer.Add(ct)
   
           c2 = wx.StaticText(top, -1, 'Type: ')
           c2.SetFont(font)
           cb = wx.ComboBox(top, -1, '', choices=('dog', 'cat', 'hamster', 'python'))
           sizer.Add(c2)
           sizer.Add(cb)
   
           top.SetSizer(sizer)
           self.Layout()
   
   class MyApp(wx.App):
       def OnInit(self):
           frame = MyFrame(title='wxWidgets')
           frame.Show(True)
           self.SetTopWindow(frame)
           return True
   
   def main():
       app = MyApp()
       app.MainLoop()
   
   if __name__ == '__main__':
       main()
   ```

4. GTK+和PyGTK

   很离谱，这个包因为编码的原因，竟然安装不了，直接跳过吧。。。

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021012515370080.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

5. Tile/Ttk

   ```python
   from tkinter import Tk, Spinbox
   from tkinter.ttk import Style, Label, Button, Combobox
   
   top = Tk()
   Style().configure("TButton", foreground='white', background='red')
   
   Label(top, text='Animals (in pairs; min: pair, max: dozen)').pack()
   Spinbox(top, from_=2, to=12, increment=2, font='Helvetica -14 bold').pack()
   Label(top, text='Type: ').pack()
   Combobox(top, values=('dog', 'cat', 'hamster', 'python')).pack()
   Button(top, text='QUIT', command=top.quit, style='TButton').pack()
   
   top.mainloop()
   ```

### 5.6 相关模块和其他GUI

- Python中可用的GUI系统

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210125155352149.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)
  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210125155421943.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)
  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210125155539815.png)
  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210125155509243.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

## 6. 数据库编程

### 6.1 python的DB-API

1. DB-API模块属性

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126111217465.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

2. `connect()`函数属性

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126111432192.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

3. `Connect`对象方法

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021012613332111.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

4. `Cursor`对象属性

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021012613553152.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

5. 类型对象和构造函数

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126141921403.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

6. RDBMS：关系数据库管理系统，Relational DataBase Management System

### 6.2 <a name='2'>ORM</a>

1. 数据库这一章的代码也忒乱了，根本没有敲一遍的欲望，还需要自己配置好数据库之后，才能敲代码，再见了您嘞。
2. 这本书最大的问题是，很多内容都是基于python2的，然后python3很多都是提了一嘴，写的代码为了兼容两个版本，显得十分冗杂，讲道理，看到这么乱的思路和代码，我是真的无法纯粹的学习ijing 数据库编程的相关内容。
3. 后面的ORM主要包括的是`SQLAlchemy`和`SQLObject`，需要用的时候，百度API吧。

### 6.3 非关系型数据库

1. 背景：Web 和社交服务的流行趋势会导致产生大量的数据，并且数据产生的速率可能要比关系数据库能够处理得更快。
2. NoSQL：Not Only SQL，非关系型数据库，它们不保证关系数据的ACID特性。
3. 单就非关系数据库而言，就有对象数据库、键-值对存储、文档存储（或者数据存储）、图形数据库、表格数据库、列/可扩展记录/宽列数据库、多值数据库等很多种类。
4. 简单的键值对存储：
   - Redis
   - Voldemort
   - Amazon
   - Dynamo
5. 列存储
   - Cassandra
   - Google Bigtable
   - HBase
6. MongoDB：有点像关系数据库的无模式衍生品，比基于列的存储更简单、约束更少，但是比普通的键-值对存储更加灵活。一般情况下其数据会另存为JSON 对象，并且允许诸如字符串、数值、列表甚至嵌套等数据类型。
7. NoSQL中的术语是：**文档、集合**，而不是关系型数据库中的**行、列**。
8. PyMongo：注意，这里不要`from pymongo import Connection`了，会报错的，应该用`from pymongo import MongoClient`

## 7. Microsoft Office 编程

### 7.1 Excel

1. 这里用tkinter和win32com的包，可以显式操作Excel

2. `Tk().withdraw()`：不让Tk顶级窗口出现

3. 这里用的是`win32.gencache.EnsureDispatch('%s.Application' % app)`

   这个是静态调度，对象和属性经过了缓存，如果需要运行时构建，那就是动态调度：`win32com.client.Dispatch('%s.Application' % app)`

4. `Visible`必须设置为True，这样才能够在桌面上看见应用

5. 这里的`ss.Close(False)`，意思时关闭时不保存。

   ```python
   from tkinter import Tk
   from time import sleep
   from tkinter.messagebox import showwarning
   import win32com.client as win32
   
   warn = lambda app: showwarning(app, 'Exit?')
   RANGE = range(3, 8)
   
   
   def excel():
       app = 'Excel'
       xl = win32.gencache.EnsureDispatch('%s.Application' % app)
       ss = xl.Workbooks.Add()
       sh = ss.ActiveSheet
       xl.Visible = True
       sleep(1)
   
       sh.Cells(1, 1).Value = 'Python-to-%s Demo' % app
       sleep(1)
       for i in RANGE:
           sh.Cells(i, 1).Value = 'Line %d' % i
           sleep(1)
   
       sh.Cells(i+2, 1).Value = "Th-th-th-that's all folks!"
   
       warn(app)
       ss.Close(False)
       xl.Application.Quit()
   
   if __name__ == '__main__':
       Tk().withdraw()
       excel()
   ```

6. 中级就是获取网页的数据，然后写入excel，讲道理，现在用的时候，根本不会这么麻烦。

### 7.2 Word

1. Word中的代码，几乎跟excel一毛一样

   ```python
   from tkinter import Tk
   from time import sleep
   from tkinter.messagebox import showwarning
   import win32com.client as win32
   
   warn = lambda app: showwarning(app, 'Exit?')
   RANGE = range(3, 8)
   
   def word():
       app = 'Word'
       word = win32.gencache.EnsureDispatch('%s.Application' % app)
       doc = word.Documents.Add()
       word.Visible = True
       sleep(1)
   
       rng = doc.Range(0, 0)
       rng.InsertAfter('Python-to-%s Test\r\n\r\n' % app)
       sleep(1)
   
       for i in RANGE:
           rng.InsertAfter('Line %d\r\n' % i)
           sleep(1)
   
       rng.InsertAfter("\r\nTh-th-th-that's all folks!\r\n")
   
       warn(app)
       doc.Close(False)
       word.Application.Quit()
   
   if __name__ == '__main__':
       Tk().withdraw()
       word()
   ```

### 7.3 PowerPoint

1. 讲道理，都什么年代了，用python操作ppt就很扯。

2. 代码我是敲完了，但是这都啥啊，各种报错，也没法解决。

   `TypeError: 'Shapes' object is not subscriptable`

   脑阔疼

   ```python
   from tkinter import Tk
   from time import sleep
   from tkinter.messagebox import showwarning
   import win32com.client as win32
   
   warn = lambda app: showwarning(app, "Exit?")
   RANGE = range(3, 8)
   
   def ppoint():
       app = 'PowerPoint'
       ppoint = win32.gencache.EnsureDispatch('%s.Application' % app)
       pres = ppoint.Presentations.Add()
       ppoint.Visible = True
   
       sl = pres.Slides.Add(1, win32.constants.ppLayoutText)
       sleep(1)
       sla = sl.Shapes[0].TextFrame.TextRange
       sla.Text = 'Python-to-%s Demo' % app
       sleep(1)
       slb = sl.Shapes[1].TextFrame.TextRange
       for i in RANGE:
           slb.InsertAfter("Line %d\r\n" % i)
           sleep(1)
       slb.InsertAfter("\r\nTh-th-th-that's all folks!")
   
       warn(app)
       pres.Close()
       ppoint.Quit()
   
   if __name__ == '__main__':
       Tk().withdraw()
       ppoint()
   ```

### 7.4 Outlook

1. 不会吧不会吧不会吧，不会还有人用Outlook吧（狗头）

2. 特别是中级示例，我一看用的outlook2003，我就想关闭退出一起合成了。

   ```python
   from tkinter import Tk
   from tkinter.messagebox import showwarning
   import win32com.client as win32
   
   
   def warn(app): return showwarning(app, 'Exit?')
   
   
   RANGE = range(3, 8)
   
   
   def outlook():
       app = 'Outlook'
       olook = win32.gencache.EnsureDispatch('%s.Application' % app)
   
       mail = olook.CreateItem(win32.constants.olMailItem)
       recip = mail.Recipients.Add('you@127.0.0.1')
       subj = mail.Subject = 'Python-to-%s Demo' % app
       body = ["Line %d" % i for i in RANGE]
       body.insert(0, '%s\r\n' % subj)
       body.append("\r\nTh-th-th-that's all folks!")
       mail.Body = '\r\n'.join(body)
       mail.send()
   
       ns = olook.GetNamespace("MAPI")
       obox = ns.GetDefaultFolder(win32.constants.olFolderOutbox)
       obox.Display()
   
       warn(app)
       olook.Quit()
   
   if __name__ == '__main__':
       Tk().withdraw()
       outlook()
   ```

## 8. 扩展Python<a name='extension_python'> </a>

1. 配置vscode运行c代码，[参考链接](https://blog.csdn.net/qq_43067190/article/details/82117149?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control&dist_request_id=959377f5-4aa7-44d4-8e58-7d7a8d9a4255&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control)，[参考连接2](https://blog.csdn.net/qq_28581077/article/details/81380341?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-6.control&dist_request_id=a426fbc9-fb15-48cc-9efa-8f3fe57b736a&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-6.control)

2. 一键配置环境的工具：[VSCodeConfigHelper](https://guyutongxue.github.io/VSCodeConfigHelper/)

3. C程序调试时报错：`Unable to start debugging. Unexpected GDB output from command "-environment -cd xxx"`，这是因为路径中有中文的原因，所以调试报错。并不影响编译和运行：[参考链接](https://blog.csdn.net/weixin_43280025/article/details/102536941)

   1. 编译：`gcc -g test.c -o test.exe`
   2. 运行：`./test.exe`
   
   > 这里配置真的是太难了，好歹是配好了

4. 成功：

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210227094108509.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)
   
5. 我真的不懂这里的`bufsiz`是要干嘛，也没定义这个值，我就奇了怪了，不就是定义数组的长度么，你也没传参，也没定义，你传你:horse:呢？ <a name='horse'> </a>

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210301101719513.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

6. 你这个大括号又是从哪里来的，是我瞎了吗？

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210301102257408.png)

7. 上面都是我抄代码的经过，遇到这些问题，实在是觉得抄一遍也没用，也没法运行，浪费我的时间，但凡有一点用，我都会抄一遍来着。哎，真心累。

8. 常用的编写扩展的工具

   1. SWIG
   2. Pyrex
   3. Cython
   4. Psyco
   5. PyPy
   6. 嵌入Python

## 9. Web客户端和服务器

### 9.1 概述

1. SSL：安全套接字层，Secure Socket Layer。为了对传输数据进行加密，需要在普通的套接字（Socket）上添加一个额外的安全层，加密通过该套接字传输的数据。

2. 正向代理：通过代理服务器，网络管理员可以只让一部分计算机访问网络，也可以更好地监控网络的数据传输。另一个有用的特征是可以缓存数据，再次访问时，网页的加载速度会快很多。

3. 反向代理：反向代理的行为像是有一个服务器，客户端可以连接这个服务器。客户端访问这个后端服务器，接着后端服务器在网上进行真正的操作，获得客户端请求的数据。

4. 正向代理用来处理缓存数据，更接近客户端。反向代理更接近后端服务器，扮演服务器端角色，如缓存服务器的数据，、负载平衡等。反向代理服务器还可以用来作为防火墙或加密数据（通过SSL、HTTPS、安全FTP（SFTP）等）。

5. URL：统一资源定位符，Uniform Resource Locator。

6. URI：统一资源标识符，Uniform Resource Identifier。

7. URL是URI的一部分。

8. URN：统一资源名称，Uniform Resource Name，非URL的URI。

9. 现在唯一使用URI的只有URL，而很少听到URI和URN，后者只作为可能会用到的XML标识符了。

10. URL的格式：`prot_sch:://net_loc/path;params?query#frag`，其中：

    net_loc可以进一步拆分成多个组件，一些是必备的，另一些是可选的：`user:passwd@host:port`

    | URL组件  | 描述                                      |
    | -------- | ----------------------------------------- |
    | prot_sch | 网络协议或下载方案                        |
    | net_loc  | 服务器所在地（也许含有用户信息）          |
    | path     | 使用斜杠（/）分割的文件或CGI应用的路径    |
    | params   | 可选参数                                  |
    | query    | 连接符（&）分割的一系列键值对             |
    | frag     | 指定文档内特定锚的部分                    |
    | user     | 用户名                                    |
    | passwd   | 用户密码                                  |
    | host     | 运行Web服务器的计算机名称或地址（必须的） |
    | port     | 端口号（如果不是默认的80）                |

### 9.2 Web客户端工具

1. `from urllib.parse import urlparse, urlunparse, urljoin`

   1. `urlparse`将urlstr字符串拆分成6个元组

      `urlparse (urlstr, defProtSch=None, allowFrag=None)`

   2. `urlunparse`的功能与`urlparse`相反，其将敬`urlparse`处理的URL生成urltup这个6元组：`(prot_sch, net_loc, path, params, query, frag)`，拼接成URL并返回

      `urlunparse(urltup)`

   3. `urljoin`取得根域名，并将其根路径与newurl连接起来

      `urljoin (baseurl, newurl, allowFrag=None)`

   4. 总结：

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210305102007428.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

   5. 测试：

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210305102130429.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

2. `from urllib.request import urlopen`

   1. `urlopen (urlstr, postQueryData=None)`

   2. `urlopen`打开urlstr所指向的URL。如果没有给定协议或者下载方案（Scheme），或者传入了file方案，urlopen会打开一个本地文件

   3. MIME：多目标因特网邮件扩展，Multipurpose Internet Mail Extension，`f.info()`方法可以返回MIME头文件，这个头文件通知浏览器返回的文件类型，以及可以用哪些应用程序打开

   4. urlopen文件类型对象的方法

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210305105431649.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

3. `from urllib.request import urlretrieve`

   1. `urlretrieve(url, filename=None, reporthook=None, data=None)`
   2. `urlretrieve`不是用来以文件的形式访问并打开URL，而是用于下载完整的HTML，把另存为文件
   3. `urlretrieve`返回一个二元组`(filename, mime_hdrs)`，filename是含有下载数据的本地文件名，mime_hdrs是Web服务器响应后返回的一系列MIME文件头，对本地文件来说，mime_hdrs是空的

4. `from urllib.parse import quote, quote_plus`

   1. `quote(urldata, safe='/')`

   2. `quote`函数用来获取URL数据，并将其编码，使其可以用于URL字符串中。

   3. `quote_plus`与`quote`很像，只是它还可以将空格编码成`+`号

   4. 测试：

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210305144711872.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

5. `from urllib.parse import unquote, unquote_plus`

   1. `unquote`与`quote`函数的功能完全相反，前者将所有编码为`%xx`式的字符转换成等价的ASCII码值
   2. `unquote(urldate)`

6. `from urllib.parse import urlencode`

   1. 将字典的键值对通过`quote_plus`编译成有效的CGI查询字符串，用`quote_plus`对这个字符串进行编码

   2. 测试：

      ![image-20210305145335998](E:\typora_pics_savepath\image-20210305145335998.png)

7. `urllib.parse`和`urllib.request`函数总结：

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210305145435610.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

8. 

























核心编程：学到 9.2.4

python魔法

python从入门到放弃视频教程

flask书

flask视频教程



























------

我的CSDN：https://blog.csdn.net/qq_21579045

我的博客园：https://www.cnblogs.com/lyjun/

我的Github：https://github.com/TinyHandsome

纸上得来终觉浅，绝知此事要躬行~

欢迎大家过来OB~

by 李英俊小朋友



