# 《Python核心编程（第3版）》学习笔记

[TOC]

## 写在前面

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

### 2.1 socket（套接字）

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



































------

我的CSDN：https://blog.csdn.net/qq_21579045

我的博客园：https://www.cnblogs.com/lyjun/

我的Github：https://github.com/TinyHandsome

纸上得来终觉浅，绝知此事要躬行~

欢迎大家过来OB~

by 李英俊小朋友



