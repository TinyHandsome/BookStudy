# 两步解决XMind发生了错误，请参阅日志文件

## 写在前面

- 做这件事的原因：
  1. 安装完XMind之后，启动就发现报错。
  2. 然后网上找了半天也没有找到解决办法，然后看到下面参考链接提供的办法，我想到了一个更好的办法哈哈哈。
- 参考链接：[xmind 8 安装后启动失败](https://www.cnblogs.com/wxdestiny/p/10618531.html)
- 如果有错别字呢，哪里写错了呢，请在评论区告诉我嗷，同时，可能会有一些奇奇怪怪的符号夹在文字中，这是因为我用的是MarkDown语法，其中一些符号可能在这个平台（比如CSDN）不支持呢。

## 解决方案

> 如果你没耐心，建议直接看解决方案的**第4步**嗷。

1. 首先你要安装的是XMind8，而不是XMind2020。因为据我研究之后发现，XMind2020是没有XMind.ini文件的，别问，问就是血的教训。（哭）

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201220102645117.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

2. 打开XMind.ini文件之后（你不会连这个文件都找不到吧，不会吧不会吧不会吧）

   1. 你会看到几行，应该是 **三行** `@user.home` 开头的路径。（这里借用一下上面参考文件的图，求作者原谅我）

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201220103039720.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

   2. 你看这些都是路径吧，他们是要把你这些配置文件，放到这个乱七八糟的目录下，一般`@user.home`就是`C:\users\你的用户名\AppData\Roaming\`下面，但是我真不知道为什么它这个路径是放在`Application Data`下面，所以这就是我们的问题所在吧（我不确定嗷，我瞎说的）。

   3. 讲道理上面我真是瞎说的，因为我把`Application Data`改为`AppData\Roaming`之后，也还是报错。（气）我猜这是因为我的users里面有一些奇奇怪怪的文件（用户），你看：

      ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201220103505329.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

   4. 但是 **原理你懂了吧** （不懂锤你），那么我们怎么解决呢：

      1. 把`@user.home/Application Data`换成你的安装路径，像我就是直接改为`D:`

         ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201220104845825.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

      2. 因为我本来XMind就是装在D盘的根目录下的，所以，这些配置文件呀，就会保存到XMind中去。如果你软件安装在了别处，你也可以改到相应的路径，或者不改应该也可以（应该会直接在D盘下面给你建一个这个路径的）

      3. 好了，配置完了，可以打开了嗷

         ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201220104856619.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

      4. 很明显，这是未破解的。~~现在要开始破解了嗷~~（没有，别看了）

      5. **请大家支持正版**。（小声：我破解了，嘻嘻）

------

我的CSDN：https://blog.csdn.net/qq_21579045

我的博客园：https://www.cnblogs.com/lyjun/

我的Github：https://github.com/TinyHandsome

纸上得来终觉浅，绝知此事要躬行~

欢迎大家过来OB~

by 李英俊小朋友