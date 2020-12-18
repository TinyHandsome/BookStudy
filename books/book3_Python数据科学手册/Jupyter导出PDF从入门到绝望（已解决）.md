# Jupyter导出PDF从入门到绝望（已解决）

## 问题描述

我在使用jupyter lab的时候，想要把我的代码和结果导出成pdf格式的（由于里面有图片，所以不想导出成html）。然后报错：

![img](https://img-blog.csdnimg.cn/20190522140525488.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

然后我用pip安装了pandoc，发现并没有什么luan用。并且好像跟报错所指的pandoc不一样。反正就是绝望就完事儿了。

## 解决办法

1. 下载安装windows开发环境包的管理器，Chocolatey。参考官网了连接，用cmd粘代码就能装：[官网](https://chocolatey.org/)

   `@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"`

2. 然后呢，就可以用这个管理工具安装pandoc了，参考[pandoc官网](https://pandoc.org/installing.html)

   `choco install pandoc`

   ![img](https://img-blog.csdnimg.cn/20190522140347835.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

3. 安装完事儿！

   ![img](https://img-blog.csdnimg.cn/20190522141137671.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

4. 然后导出pdf的时候发现，竟然对pandoc的版本有要求，也是佛了，那就重新搞一下把。。。

   ![img](https://img-blog.csdnimg.cn/20190522141725475.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

   安装固定版本的pandoc，根据[官网发布的版本list](<https://pandoc.org/releases.html#pandoc-1.19.2.4-10-sep-2017>)，我选择安装1.19版本的。`choco install pandoc --version 1.19`

   ![img](https://img-blog.csdnimg.cn/20190522145630612.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

   安装时安装完毕了，不知道为啥，一副好像报错了的样子，下的我赶紧去看一下到底是安装好了没。。。

   ![img](https://img-blog.csdnimg.cn/2019052214583633.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

   应该是完事儿了，然后试试导出pdf。

5. pandoc好像是没有问题了，可是另一个包好像又除了问题：

   ![img](https://img-blog.csdnimg.cn/20190522145613941.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

   所以现在又要安装这个：

   `choco install miktex`

   ![img](https://img-blog.csdnimg.cn/20190522150040633.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

6. 完。。。做完这一步，电脑自动重启了，然后jupyter lab打不开了，报错：

   `ImportError: cannot import name 'constants' from 'zmq.backend.cython’`

   然后没办法，用pip升级了一下pyzmq包，总算是能打开了。。。

   ![img](https://img-blog.csdnimg.cn/20190522151612816.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

   然后，告诉我，我下载的插件不能用了，要重新“build”，所以就重新安装了插件。。。（像显示目录啊之类的插件。。。）

   ![img](https://img-blog.csdnimg.cn/2019052215174854.png)

   我真的很绝望。。。

   ![img](https://img-blog.csdnimg.cn/20190522153316641.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

7. 然后依然报同样的错误。。。于是我怀疑，是不是MikTex有错，于是在官网上下了一个exe安装的那种，一路确认下去。。。[参考链接](<https://blog.csdn.net/csdnsevenn/article/details/81091523>)、[下载链接](https://miktex.org/)

   果然，在点了导出pdf的时候，报错缺少的文件就弹出来安装程序了。。。

   ![img](https://img-blog.csdnimg.cn/20190522161935621.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)
   
   然后就成功保存pdf啦！

![img](https://img-blog.csdnimg.cn/20190522162225837.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

## 另辟蹊径

说实话，这样导出来的pdf并不好看，还有一种方法，直接导出html，里面保留了插入的图片的那种，更能还原jupyter原来的排版。[参考链接](<https://www.jianshu.com/p/49a0c9f74d59>)

------

我的CSDN：https://blog.csdn.net/qq_21579045

我的博客园：https://www.cnblogs.com/lyjun/

我的Github：https://github.com/TinyHandsome

纸上得来终觉浅，绝知此事要躬行~

欢迎大家过来OB~

by 李英俊小朋友