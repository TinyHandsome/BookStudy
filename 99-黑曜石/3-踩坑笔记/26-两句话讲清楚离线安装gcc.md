---
sticker: emoji//1f4bb
tags:
  - gcc
  - GLIBCXX
  - openmm
  - colabfold
  - conda
banner: Cover/26.png
---
# LocalColabFold安装全流程：离线安装解决gcc和GLIBCXX+openmm报错解决

[TOC]

## 写在前面

- 摘要

  在部署colabfold的时候，发现gcc版本不能低于9，服务器又没法联网，不得不研究一下gcc的离线安装了。（make的时间超长，真的）即使升级了gcc还会报错：`ImportError: /usr/lib64/libstdc++.so.6: 'version GLIBCXX_3.4.26' not found`。修复后又报错：`ValueError: Minimization failed after 100 attempts`

- 环境

  - 离线的银河麒麟
  - 其他的系统应该也差不多，因为我们用的是编译的方式

## 0. 简单介绍一些LocalColabFold的安装流程

作者的流程写的很清楚了，照着干就完了，是吧。1是检查一些常规命令，2是检查gpu相关（这里我没用gpu，想用cpu推理，所以跳过），3是检查gcc，这里我的版本就只有7，所以一开始没检查，后面报错了 `ImportError: /usr/lib64/libstdc++.so.6: 'version GLIBCXX_3.4.26' not found`，所以才回头来升级（**见Chapter 1**），4就是全自动安装了，其实后续没啥了，因为我比较皮，一看这玩意儿就是conda嘛，醉醉的，我就装了一个conda pack，把整个环境打包了，然后把params放到了指定位置。

**注意**：自己改了之后要改params的路径，因为在加载模型的时候要用本地的权重（见图2）。比如我的params的路径是 `/disk/projects/colabfold/params`，那么①中的内容就写：`/disk/projects/colabfold`，这是因为②里面写死了 `params`（这个开发者写的代码真的很烂，一顿conda乱搞，代码也是各种写死，服辣！）

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/2058b023eb044225a06be48a6c806545.png)

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/278d66c33d014670a47a5eb7c5c884d2.png)


## 1. gcc离线安装升级

首先，我们要知道gcc安装是有依赖的，如果你直接make gcc，会报错，告诉你需要gmp、mpfr和mpc三个依赖，且这三个依赖还有安装顺序：

1. 下载这四个库，传到服务器：

   - https://ftp.gnu.org/gnu/gmp/gmp-6.3.0.tar.gz
   - https://ftp.gnu.org/gnu/mpfr/mpfr-4.2.1.tar.gz
   - https://ftp.gnu.org/gnu/mpc/mpc-1.3.1.tar.gz
   - https://ftp.gnu.org/gnu/gcc/gcc-14.2.0/gcc-14.2.0.tar.xz

   这里，我选择的是我下载的版本，毕竟都选最新的感觉版本导致的问题最小。

2. 按上述顺序分别执行下面的流程：

   1. `tar -zxvf xxx.tar.gz`：解压文件
   2. `mkdir build && cd build`：创建build文件夹并进入
   3. `../configure`：运行配置程序
   4. `make && make install`：编译安装

   如果有类似经验的你，肯定知道这一套是标准流程，把上述四个 xxx.tar.gz 按这个流程走四遍就完了。注意：gcc 在第三步的时候要 `../configure -–disable-multilib`，如果你不加也会提醒你，没错，如果禁用了的话你就用不了32位的程序了，但是能怎么办呢，如果enbale，就会遇到缺少某个库的问题。

3. 没错，结束了，三个依赖的编译和安装都很快，gcc的make可慢可慢了，我用了半天，你要有心理准备，耐心耐心耐心！

4. 最后完事后用 `gcc -v` 查看版本哦，如果在screen里面，要退出来重新进。

## 2. Link GLIBCXX_3.4.26

作者就写了个什么东西啊，升级gcc就解决吗？解决不了阿喂！依然报错：`ImportError: /usr/lib64/libstdc++.so.6: 'version GLIBCXX_3.4.26' not found`。为什么？[参考链接](https://www.cnblogs.com/studywithallofyou/p/17611199.html)，因为就嘎嘎升级，但是没建立链接啊，用的时候还是没这玩意儿，醉醉的。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/aad2a180a1f54ab196171d912f7b4ef0.png)

1. 查看你当前的 `libstdc++.so.6` 中链接了哪些 `GLIBCXX` ：`strings /usr/lib64/libstdc++.so.6|grep GLIBCXX`，其中 `strings` 是一个用于提取文件中可打印文本字符串的Unix/Linux命令。发现没有 `GLIBCXX_3.4.26` 了吧

   > 可以看到是`3.4.24`，最后的编号`24`与lib库`libstdc++.so.6.0.24`最后的编号是一致的。

2. 那么怎么办呢：找 `libstdc++.so.6.0.26` 这个然后重建链接就完了，所以**重装gcc真的有必要吗**，我持怀疑态度，直接去找一个重建链接是不是能解决。

   - 找到libstdc++.so.6.0库有哪些：`find / -name "libstdc++.so.6.0.*"`
   - 复制一个大于等于26的库到 `/user/lib64/`，比如我选33：`cp /usr/local/lib64/libstdc++.so.6.0.33 /usr/lib64/`
   - 备份已有链接：`mv /usr/lib64/libstdc++.so.6 /usr/lib64/libstdc++.so.6.bak`
   - 建立新的链接：`ln -s /usr/lib64/libstdc++.so.6.0.33 /usr/lib64/libstdc++.so.6`

3. 再看 `strings /usr/lib64/libstdc++.so.6|grep GLIBCXX`，是不是就有了。这下好使了。

## 3. ValueError: Minimization failed after 100 attempts

好不容易前面搞好了，运行又报错。这个问题不光是我一个人嗷，https://github.com/YoshitakaMo/localcolabfold/issues/108 。一顿讨论，有说不用gpu的：`remove --use-gpu-relax`，可我本来就没用啊，有说重装openmm的：`mamba install openmm==7.7.0 -y`，重复安装警告了。作者还问有没有：`remove or rename the colabfold_batch directory from somewhere`，没错，就是在下！（自豪，:sweat_smile:）

> https://blog.csdn.net/qq_41856194/article/details/135391884
>
> ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/a5ed383181a04d1e97addfc813386783.png)

这就暗示了这个问题到底是啥原因了，别搜！搜了很难搜到，但我还是搜到了：启发！还是启发！这个作者一顿操作吧，没错我也操作不了，因为 `from simtk.openmm import *` 这一步就直接报错了，我复现个蛇皮复现。但是他让我知道了，这个憨批库，有一个很重要的配置文件：`openmm_library_path`。那么这个库的正常配置是多少，我是可以知道的，新建个conda环境，装一下就知道了。我的路径这啥玩意啊这是，给我改！！！！！没错：写到你的**conda环境的lib目录**。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/3431b7d751c84840bbf9c08c9f8424c6.png)

## :tada: 尾声

结束了家人们，累了。运行终于不报错了。Done is all you need！:tada:

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/ebb990b1198c47468db0a07861ca5249.png)


------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
