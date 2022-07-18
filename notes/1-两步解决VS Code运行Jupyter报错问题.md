# 两步解决VS Code运行Jupyter报错问题

报错内容：

> Unable to start session for kernel Python 3. Select another kernel to launch with.

我用**两步**解决了问题，至于原因没搞清楚，如果有搞清楚了的大佬，请在评论区告诉我。

本文的目的主要是，为了帮助打开jupyter就报错、shift+enter运行就报错的朋友们。

**解决方案：**

1. **将traitlets这个包的版本降回到4.3.3**，[参考链接](https://my.oschina.net/u/4319831/blog/4546680)

   ```
   python3 -m pip install traitlets==4.3.3 --force-reinstall
   ```

   这里我百度到的，基本正经的解决方案就找到了这一个。

   问题来了，我重新安装了这个包，还是不行。

   但我做了第2步操作之后就行了。

2. **将vscode中的setting.json中关于python的路径设置清空，并重启**：

   清空前：

   ```
   "python.defaultInterpreterPath": "D:\\python3.78\\python.exe"
   ```

   清空后：

   ```
   "python.defaultInterpreterPath": ""
   ```

   然后关了vscode重启。

3. 好了这个时候，你就会发现：

   1. 你没有选择python版本或者路径，也能在vscode中运行jupyter
   2. 左下角python解释器版本那里会变红，告诉你要你选择一个python解释器
   3. 选择你用的python，也不影响jupyter的使用了
   4. 完美解决

4. 至于有没有必要降低traitlets版本，我也不知道，因为我刚好凑巧把这两步做了之后，问题就解决了。

   有没有大佬在出问题之后，先试一下第2步，看能不能直接解决，结果在评论区告诉一下我好吗？

5. 如果你看不懂，请在评论区问我，好吗？别急，慢慢来，好吗？

------

- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友