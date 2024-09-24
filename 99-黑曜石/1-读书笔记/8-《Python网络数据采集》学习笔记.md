# 《Python网络数据采集》学习笔记

[TOC]

## 写在前面

- 封面

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/a06b6c1d14eb428080da93dc006849c2.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

- 读后感

  1. 读到3.4scrapy的我跑来描述一下我的感想：再次确定了国外的书真的很不适合中国人，因为某些懂的都懂的原因，书中涉及到的很多链接都无法访问，对于一本爬虫的书来说，简直就是硬伤；其次，这本书并没有指定例子使用的Python的版本，各个库的版本，这对一门非常注中实践的学科来说，简直就是可以直接判定这本书的死开刂，我在 scrapy 中找 SgmlLinkExtractor 的时候真的人麻了，麻的透透的。

- 传送门

## 1. 初见网络爬虫

1. 网络连接

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/5e5e892152884cb18e9c1cb3e4cad558.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

2. BeautifulSoup简介

   1. BeautifulSoup 库的名字取自刘易斯 ·卡罗尔在《爱丽丝梦游仙境》里的同名诗歌

   2. 就像它在仙境中的说法一样，BeautifulSoup 尝试化平淡为神奇

   3. 虚拟环境安装和使用

      ```bash
      virtualenv scrapingEnv
      cd Scripts
      activate
      ```

   4. 退出虚拟环境

      ```bash
      deactivate
      ```

   5. 运行beautifulsoup

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/f5cd7c855a4e494b99e46a902b33e656.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

   6. 可靠的网络连接

      ```python
      from urllib.request import urlopen
      from urllib.error import HTTPError
      from bs4 import BeautifulSoup
      
      def getTitle(url):
          try:
              html = urlopen(url)
          except HTTPError as e:
              return None
          try:
              bsObj = BeautifulSoup(html.read())
              title = bsObj.body.h1
          except AttributeError as e:
              return None
          return title
      
      title = getTitle("http://www.pythonscraping.com/pages/page1.html")
      if title is None:
          print("Title could not be found")
      else:
          print(title)
      ```

## 2. 复杂HTML解析

1. 不是一直都要用锤子
   1. 寻找“打印此页”的链接，或者看看网站有没有 HTML 样式更友好的移动版
   2. 寻找隐藏在 JavaScript 文件里的信息
   3. 虽然网页标题经常会用到，但是这个信息也许可以从网页的 URL 链接里获取
   4. 找找其他数据源
   
2. 再端一碗BeautifulSoup

   1. CSS：Cascading Style Sheet，层叠样式表

   2. `.get_text()` 会把你正在处理的 HTML 文档中所有的标签都清除，然后返回一个只包含文字的字符串

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/03ffd3a8ad1c47dbae87c6f1dda0ef24.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_19,color_FFFFFF,t_70,g_se,x_16)

   3. BeautifulSoup的`find()`和`findAll()`

      1. `findAll(tag, attributes, recursive, text, limit, keywords)`

      2. `find(tag, attributes, recursive, text, keywords)`

      3. `tag`：下面的代码将返回一个包含 HTML 文档中所有标题标签的列表：`.findAll({"h1","h2","h3","h4","h5","h6"})`

      4. `attributes`：下面这个函数会返回 HTML 文档里红色与绿色两种颜色的 span 标签：`.findAll("span", {"class":{"green", "red"}})`

      5. `recursive`：递归参数 recursive 是一个布尔变量。

         1. 如果recursive 设置为 True（默认），findAll 就会根据你的要求去查找标签参数的所有子标签，以及子标签的子标签；
         2. 如果 recursive 设置为 False，findAll 就只查找文档的一级标签
         3. 一般情况下这个参数不需要设置，除非你真正了解自己需要哪些信息，而且抓取速度非常重要，那时你可以设置递归参数

      6. `text`：用标签的文本内容去匹配，而不是用标签的属性

         假如我们想查找前面网页中包含“the prince”内容的标签数量，我们可以把之前的 findAll 方法换成下面的代码：

         ![在这里插入图片描述](https://img-blog.csdnimg.cn/b946626162e74744bf2f69a2c857bb1b.png)

      7. `limit`：显然只用于 findAll 方法

         1. find 其实等价于 findAll 的 limit 等于 1 时的情形
         2. 如果你只对网页中获取的前 x 项结果感兴趣，就可以设置它
         3. 这个参数设置之后，获得的前几项结果是按照网页上的顺序排序的，未必是你想要的那前几项

      8. `keyword`：可以让你选择那些具有指定属性的标签

         ```python
         allText = bsObj.findAll(id="text")
         print(allText[0].get_text())
         ```

         1. 关键词参数 keyword 是 BeautifulSoup 在技术上做的一个冗余功能

         2. 例如，下面两行代码是完全一样的：

            ```python
            bsObj.findAll(id="text")
            bsObj.findAll("", {"id": "text"})
            ```

         3. 用 keyword 偶尔会出现问题，尤其是在用 class 属性查找标签的时候，因为 class 是 Python 中受保护的关键字，在 Python 程序里是不能当作变量或参数名使用的

            - 下面会因为你误用 class 保留字而产生一个语法错误：

              `bsObj.findAll(class="green")`

            - 可以用 BeautifulSoup 提供的有点儿臃肿的方案，在 class 后面增加一个下划线：

              `bsObj.findAll(class_="green")`

            - 最好的方式是用属性参数把 class 用引号包起来：

              `bsObj.findAll("", {"class":"green"})`

   4. 其他BeautifulSoup对象

      1. `BeautifulSoup 对象`：

         ```python
         html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
         bsObj = BeautifulSoup(html)
         ```

      2. `标签 Tag 对象`：BeautifulSoup 对象通过 find 和 findAll，或者直接调用子标签获取的一列对象或单个对象，例如：`bsObj.div.h1`

      3. `NavigableString 对象`：用来表示标签里的文字，不是标签

      4. `Comment 对象`：用来查找 HTML 文档的注释标签，`<!-- 像这样 -->`

   5. 导航树

      1. 前言：

         1. findAll 函数通过标签的名称和属性来查找标签
         2. 如果你需要通过标签在文档中的位置来查找标签，需要用到导航树（Navigating Trees）

      2. 处理子标签和其他后代标签

         1. 子标签就是一个父标签的下一级

         2. 后代标签是指一个父标签下面所有级别的标签

         3. 例如，tr 标签是 tabel 标签的子标签，而 tr、th、td、img 和 span 标签都是 tabel 标签的后代标签

         4. 所有的子标签都是后代标签，但不是所有的后代标签都是子标签

         5. 一般情况下，BeautifulSoup 函数总是处理当前标签的后代标签

            - bsObj.body.h1 选择了 body 标签后代里的第一个 h1 标签，不会去找 body 外面的标签
            - bsObj.div.findAll("img") 会找出文档中第一个 div 标签，然后获取这个 div 后代里所有的 img 标签列表

         6. 如果你只想找出子标签，可以用 `.children` 标签：

            ```python
            from urllib.request import urlopen
            from bs4 import BeautifulSoup
            
            html = urlopen("http://www.pythonscraping.com/pages/page3.html")
            bsObj = BeautifulSoup(html)
            
            for child in bsObj.find("table", {"id": "giftList"}).children:
                print(child)
            ```

            - 这段代码会打印 giftList 表格中所有产品的数据行
            - 如果你用 descendants() 函数而不是 children() 函数，那么就会有二十几个标签打印出来：包括 img 标签、span 标签，以及每个 td 标签

      3. 处理兄弟标签

         - next_siblings()

           ```python
           for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
             print(sibling)
           ```

         - 这段代码会打印产品列表里的所有行的产品，第一行表格标题除外
         - 为什么标题行被跳过了
           1. 对象不能把自己作为兄弟标签
           2. 这个函数只调用后面的兄弟标签
         - `previous_siblings`：和 next_siblings 一样，向前查找标签
         - next_sibling 和 previous_sibling：与 next_siblings 和 previous_siblings 的作用类似，只是它们返回的是单个标签，而不是一组标签
         
      4. 父标签处理
      
         ```python
         print(bsObj.find("img", {"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
         ```
   
3. 正则表达式

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/89b020e0111141db90bf399226d93176.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

4. 正则表达式和BeautifulSoup

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/de7aef1862fe4c3087f7a118914fe8f0.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

   - 正则表达式可以作为 BeautifulSoup 语句的任意一个参数，让你的目标元素查找工作极具灵活性

5. 获取属性

   1. 对于一个标签对象，可以用下面的代码获取它的全部属性：`myTag.attrs`
   2. 这行代码返回的是一个 Python 字典对象，可以获取和操作这些属性
   3. 比如要获取图片的资源位置 src，可以用下面这行代码：`myImgTag.attrs["src"]`

6. Lambda表达式

   1. BeautifulSoup 允许我们把特定函数类型当作 findAll 函数的参数。唯一的限制条件是这些函数必须把一个标签作为参数且返回结果是布尔类型
   2. BeautifulSoup 用这个函数来评估它遇到的每个标签对象，最后把评估结果为“真”的标签保留，把其他标签剔除
   3. 获取有两个属性的标签：`soup.findAll(lambda tag: len(tag.attrs) == 2)`
   
7. 超越BeautifulSoup

   1. lxml：可以用来解析 HTML 和 XML 文档
   2. HTML parser：Python 自带的解析库

## 3. 开始采集

1. 遍历单个域名

   1. Python 的伪随机数（pseudorandom number）生成器用的是梅森旋转（Mersenne Twister）算法，它产生的随机数很难预测且呈均匀分布，就是有点儿耗费 CPU 资源。真正好的随机数可不便宜

   2. 遍历维基百科

      ```python
      from urllib.request import urlopen
      from bs4 import BeautifulSoup
      import datetime
      import random
      import re
      
      random.seed(datetime.datetime.now())
      def getLinks(articleUrl):
          html = urlopen("http://en.wikipedia.org" + articleUrl)
          bsObj = BeautifulSoup(html)
          return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
      
      links = getLinks("/wiki/Kevin_Bacon")
      while len(links) > 0:
          newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
          print(newArticle)
          links = getLinks(newArticle)
      ```

2. 采集整个网站

   1. 浅网（surface Web）：浅网是互联网上搜索引擎可以抓到的那部分网络

   2. 深网（deep Web）：与浅网（surface Web）对立；互联网中其实约 90% 的网络都是深网

   3. 暗网（dark Web）：它们也建立在已有的网络基础上，但是使用 Tor 客户端，带有运行在 HTTP 之上的新协议，提供了一个信息交换的安全隧道

   4. 建立一个爬虫和数据收集（至少是数据打印）的组合程序：

      ```python
      from urllib.request import urlopen
      from bs4 import BeautifulSoup
      import re
      
      pages = set()
      def getLinks(pageUrl):
          global pages
          html = urlopen("http://en.wikipedia.org" + pageUrl)
          bsObj = BeautifulSoup(html)
          try:
              print(bsObj.h1.get_text())
              print(bsObj.find(id="mw-content-text").findAll("p")[0])
              print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
          except AttributeError:
              print("页面缺少一些属性！不过不用担心！")
              
          for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
              if 'href' in link.attrs:
                  if link.attrs['href'] not in pages:
                      # 我们遇到了新页面
                      newPage = link.attrs['href']
                      print("----------------\n" + newPage)
                      pages.add(newPage)
                      getLinks(newPage)
                      
      getLinks("")
      ```

3. 通过互联网采集

   ```python
   from urllib.request import urlopen
   from bs4 import BeautifulSoup
   import re
   import datetime
   import random
   
   pages = set()
   
   random.seed(datetime.datetime.now())
   
   # 获取页面所有的内链的列表
   def getInternalLinks(bsObj, includeUrl):
       internaliLinks = []
       # 找出所有以 "/" 开头的链接
       for link in bsObj.findAll('a', href=re.compile("^(/|.*)" + includeUrl + ")")):
           if link.attrs['href'] is not None:
               if link.attrs['href'] not in internaliLinks:
                   internaliLinks.append(link.attrs['href'])
       return internaliLinks
   
   # 获取页面所有外链的列表
   def getExternalLinks(bsObj, excludeUrl):
       externalLinks = []
       # 找出所有以 "http" 或 "www" 开头且不包含当前URL的链接
       for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
           if link.attrs['href'] is not None:
               if link.attrs['href'] not in externalLinks:
                   externalLinks.append(link.attrs['href'])
       return externalLinks
   
   def splitAddress(address):
       addressParts = address.replace('http://', '').split('/')
       return addressParts
   
   def getRandomExternalLink(startingPage):
       html = urlopen(startingPage)
       bsObj = BeautifulSoup(html)
       externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
       if len(externalLinks) == 0:
           internalLinks = getInternalLinks(startingPage)
           return getNextExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
       else:
           return externalLinks[random.randint(0, len(externalLinks)-1)]
   
   def followExternalOnly(startingSite):
       externalLink = getRandomExternalLink("http://oreilly.com")
       print('随机外链是:' + externalLink)
       followExternalOnly(externalLink)
   
   followExternalOnly("http://oreilly.com")
   ```

   ```python
   # 收集网站上发现的所有外链列表
   allExtLinks = set()
   allIntLinks = set()
   def getAllExternalLinks(siteUrl):
       html = urlopen(siteUrl)
       bsObj = BeautifulSoup(html)
       internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
       externalLinks = getExternalLinks(bsObj, splitAddress(siteUrl)[0])
       
       for link in externalLinks:
           if link not in allExtLinks:
               allExtLinks.add(link)
               print(link)
       
       for link in internalLinks:
           if link not in allIntLinks:
               print("即将获取链接URL是: " + link)
               allIntLinks.add(link)
               getAllExternalLinks(link)
       
   getAllExternalLinks("http://oreilly.com")
   ```

4. 用Scrapy采集

   - 日志一共有5种等级

     - CRITICAL
     - ERROR
     - WARNING
     - DEBUG
     - INFO

   - 在setting中设置日志等级

     ```
     LOG_LEVEL = 'ERROR'
     ```

   - 通过下面命令输出到一个独立的文件中

     `scrapy crawl article -s LOG_FILE=wiki.log`
   
   - Scrapy 用 Item 对象决定要从它浏览的页面中提取哪些信息。Scrapy 支持用不同的输出格式来保存这些信息，比如 CSV、JSON 或 XML 文件格式：
   
     ```
     $ scrapy crawl article -o articles.csv -t csv
     $ scrapy crawl article -o articles.json -t json
     $ scrapy crawl article -o articles.xml -t xml
     ```

## 4. 使用API

1. 利用 HTTP 从网络服务获取信息有四种方式：
   - GET
   - POST
   - PUT
   - DELETE
2. 集合查找速度更快（确定一个对象是否在集合中）：因为 Python 集合就是值为 None 的词典，用的是哈希表结构，查询速度为O(1)。

## 5. 存储数据

1. 存储媒体文件有两种主要的方式：
   - 只获取文件 URL 链接
   - 把源文件下载下来



















学到 P64




------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
