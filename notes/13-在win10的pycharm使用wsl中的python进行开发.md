# 在win10的pycharm使用wsl中的python进行开发

[TOC]

## 写在前面

- 环境

  - wsl1（win10版本不够安装wsl2）
  - ubuntu1804，非官方商店安装
  - 平平无奇的pycharm
  - 这里提两个python环境
    - 一个是ubuntu自带的 python3.6.9
    - 一个是用pyenv下载的 python3.5.4

- 问题

  - win10中pycharm如何配置wsl中ubuntu的python

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/3261b02d3cbb467e893fd6907ba55476.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

- 参考链接

  - [写的很好但还是差点东西](https://blog.csdn.net/AggressionStorm/article/details/115034728)

## 解决方案

1. 编辑`wsl.distributions.xml`文件，插入自定义发行版信息

   - 这个文件的位置在如下类似的位置，该例子来自参考链接（我是直接用 everything 查的位置，听懂掌声）

     ```
     C:\Users\zrs\AppData\Roaming\JetBrains\PyCharm2020.1\options\ wsl.distributions.xml
     ```

   - 只需要增加一项你wsl中ubuntu的位置

     ```xml
     <!-- 配置wsl -->
     <descriptor>
     	<id>ubuntu1804-my</id>
     	<microsoft-id>ubuntu1804-my</microsoft-id>
     	<executable-path>E:\Ubuntu18\ubuntu.exe</executable-path>
     	<presentable-name>ubuntu1804-my</presentable-name>
     </descriptor>
     ```

   - 上述注意要给出自己ubuntu.exe的位置

2. 配置 python，即系统自带的python

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/cb4d68799c7e40f6b550837ed8c37a13.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

   - 注意右键的点点点没用，相信我，反正我是没用，毕竟不是在官方商店里下的系统，如果你非要点，点了之后，左上角会出现报错的信息，所以别点了

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/b31c4bdaf88b4b1d94f99737595dc1da.png)

   - 如果是系统的python，第二行就是（以我的为例）

     `/usr/bin/python3`

   - 弄好之后，就显示这样啦

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/1b9e335b19674814867023902a72d87d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

   - 如果是pyenv安装的python，第二行就是（以我的为例）

     `/home/myname/.pyenv/versions/3.5.4/bin/python`

   - 弄好之后，显示：

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/a9ef182aa3e14d31b96f41edbf260c7e.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

3. 完成手工，点个赞可以吧，我写的时候，网上真查不到啥教程（暗示）


------

- :cloud: 我的CSDN：https://blog.csdn.net/qq_21579045
- :snowflake: 我的博客园：https://www.cnblogs.com/lyjun/
- :sunny: 我的Github：https://github.com/TinyHandsome
- :rainbow: 我的bilibili：https://space.bilibili.com/8182822
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友

