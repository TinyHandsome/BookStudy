# 简单谈谈contextlib的使用

## 写在前面

- 做这件事的原因：
  1. 在看书的时候，我发现了有大佬们用contextlib管理上下文，真的很牛皮，但是百度了以下，每个大佬都写了很多很全很深刻，讲道理五花八门使我应接不暇，于是乎我决定自己简单写一下，就写一个用例，也就是我能想到的用例来解释contextlib，至于其他的高级用法，大家请自行百度嗷
- 推荐几个链接吧：
  - [Python魔法模块之contextlib](https://www.cnblogs.com/pyspark/articles/8819803.html)
  - [每周一个 Python 模块 | contextlib](https://www.jianshu.com/p/94bc38e65fff)
- 如果有错别字呢，哪里写错了呢，请在评论区告诉我嗷，同时，可能会有一些奇奇怪怪的符号夹在文字中，这是因为我用的是MarkDown语法，其中一些符号可能在这个平台（比如CSDN）不支持呢。

## 使用方法

1. 你肯定用过`with open`的方法打开文件，然后进行读取写入等操作是吧：

   ```python
   with open('/tmp/a.txt', a) as file_obj:
       file_obj.write("hello carson")
   ```

2. `contextlib`就是实现这种功能的黑魔法。先说上面的文件操作流程：

   1. 打开文件，给file_obj
   2. 处理鸭，读啊，写啊，啥的
   3. 关闭打开的文件file_obj，即使中间出了错误啊啥的，Exception啥的，也能关闭的那种。

3. 用`contextlib`实现呢，就是：

   ```python
   from contextlib import contextmanager
   
   @contextmanager
   def make_open_context(filename, mode):
       fp = open(filename, mode)
       try:
           yield fp
       finally:
           fp.close()
   
   with make_open_context('/tmp/a.txt', 'a') as file_obj:
       file_obj.write("hello carson666")
   ```

   1. 看到这个yield，如果你不懂的话，看链接吧：[yield方法解释](https://blog.csdn.net/mieleizhi0522/article/details/82142856)。如果不懂yield，后面的没法说了。

      简单来说：把yield看作return，但是肯定是有区别的：

      1. 如果你调用这个函数 `with make_open_context('/tmp/a.txt', 'a') as file_obj:` ，那么会让函数运行到`yield fp`也就是`return fp`，欸，就返回了是吧，返回的`fp`给`file_obj`了。
      2. 然后就是跑<u>处理的内容</u>，即：`file_obj.write("hello carson666")`，好,处理部分跑完了。
      3. 然后就会继续刚才的函数中的代码：`finally: fp.close()`

   2. 也就是说，`yield`所对应的行会把函数分为两部分，第一部分在`with make_open_context('/tmp/a.txt', 'a') as file_obj:`中运行，然后返回的值给`as`的对象`file_obj`；接着运行<u>处理的内容</u>；完事了再运行后面的第二部分。

4. 好了，直到这个流程了，我们可以做什么呢，做前面和后面是一样的，但是中间是不一样的事务，这样的任务。

   你是不是懵了，没关系，看下面这个例子：

   ```python
   from contextlib import contextmanager
   
   @contextmanager
   def book_mark():
       print('《', end="")
       yield
       print('》', end="")
   
   with book_mark():
       # 核心代码
       print('且将生活一饮而尽', end="")
   ```

   输出：`《且将生活一饮而尽》`

---

我的CSDN：https://blog.csdn.net/qq_21579045

我的博客园：https://www.cnblogs.com/lyjun/

我的Github：https://github.com/TinyHandsome

纸上得来终觉浅，绝知此事要躬行~

欢迎大家过来OB~

by 李英俊小朋友

