# 《Python核心编程（第3版）》学习笔记

[TOC]

## 写在前面

- 读后感：
  - 真本书写的真的八行，外国人写的书，好的是真的好，烂的是真的烂，这本书不知道为什么吹的人那么多，烂的扣jio，有的例子真的不想抄一遍了，神神叨叨的，跑也跑不通，让自己填自己连接，我特么我知道怎么填，读你干嘛啊。
  - 最严重的问题，也就是上面说的，很多例子对应的链接已经不行了，连也连不上，特别是**在第二章、第三章学网络的时候**，特别明显，就是学了个寂寞。
  - 怎么说呢，这本书无论是对初学者还是对已经有了一定基础的python学习者，**都十分的不友好**，我的评价是：**生硬且古板**。很多已经淘汰的技术，着墨太多，并且案例无法复现。很有很多错误的地方，比如英文打错了。。。我人都傻了，[点我查看打错的地方](#error1)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201110153410970.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

## 1. 正则表达式

### 1.1 常用语法

- 正则表达式符号

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/2020111015351738.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

- 特殊字符

  ![image-20201110153547114](E:\typora_pics_savepath\image-20201110153547114.png)

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

### 2.1 socket（套接字）网络编程

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

### 4.2 thread、threading和Queue













学到Page92

















python魔法

核心编程

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



