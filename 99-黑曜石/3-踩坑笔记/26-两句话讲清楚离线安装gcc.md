---
sticker: emoji//1f4bb
tags:
  - gcc
  - 银河麒麟
  - GLIBCXX
  - linux
banner: Cover/26.png
---
# 两句话讲清楚离线安装gcc

[TOC]

## 写在前面

- 摘要

  在部署colabfold的时候，发现gcc版本不能低于9，服务器又没法联网，不得不研究一下gcc的离线安装了。（make的时间超长，真的）

- 环境

  - 离线的银河麒麟
  - 其他的系统应该也差不多，因为我们用的是编译的方式


## 解决方案

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


------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
