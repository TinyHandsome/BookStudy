---
banner: Cover/24.png
sticker: emoji//1f3dd-fe0f
tags:
  - linux
  - 银河麒麟
  - screen
  - ncurses
---
# 两句话讲清楚离线安装screen

[TOC]

## 写在前面

- 摘要

  众所周知，如果linux系统没有安装screen，那么服务器将会很难搞（我编的）。即使关闭了连接服务器的窗口，也想随时重新回到工作区，而不是只能通过本地保存的日志，或者kill进程。

- 环境

  - 离线的银河麒麟
  - 其他的系统应该也差不多，因为我们用的是编译的方式

- 参考链接

  - https://cloud.tencent.com/developer/article/1758732
  - https://developer.aliyun.com/article/1274992


## 解决方案

1. 下载ncurses：https://ftp.gnu.org/gnu/ncurses/

   我选择的是 `ncurses-6.5`，当然了这也是当前最新版了

2. 下载screen：https://ftp.gnu.org/gnu/screen/

   我选择的是 `screen-4.8.0`，注意了，我建议选这个，待会儿说原因

3. 把上述两个 `.tar.gz` 文件上传到服务器

4. 安装 `ncurses`，没错，这个是 `screen` 的依赖

   1. `tar -zxvf ncurses-6.5.tar.gz` ，解压后进入解压文件夹
   2. `mkdir build && cd build` ，创建 build 文件夹并进入
   3. `../configure` 运行配置程序，这就是运行了上一层路径的configure（因为你在build这层嘛，上一层就是ncurses的文件夹中）
   4. `make && make install` ，编译安装

5. 安装 `screen`，其实这个跟上面没区别，不能说毫无关系，只能说一毛一样

   1. `tar -zxvf screen-4.8.0.tar.gz` ，解压后进入解压文件夹
   2. `mkdir build && cd build` ，创建 build 文件夹并进入
   3. `../configure` 运行配置程序
   4. `make && make install` ，编译安装

6. 完事儿了，`screen -V` 看看，已经可以了

## 问题

因为我最开始下载的是最新的 `screen-5.x`，问题来了，在make的时候报错了：

```bash
gcc: error: unrecognized command line option '-std=c17'; did you mean '-std=
```

网上说原因是你的gcc版本太低了，那就不要装5.x的screen了，装4.x即可

## screen使用

稍微介绍一下screen常用命令

1. `screen -R xxx`：创建一个自己命名的会话，检查有没有同名会话已经创建，若有，则进入该回话。**一般新建的时候用这个**
2. `screen -d xxx`：断开xxx的对话，因为有时候服务器断了，其实对话还在，那么需要先断开，**一般重连服务器的时候先执行这个**
3. `screen -r xxx`：恢复对话，R和r是有区别的，反正看个人习惯吧，我创建用R，回到对话用r**每次重新连接服务器，就先2后3**
4. `screen -ls`：查看对话列表
5. `ctrl+a，d`：如果在对话中，想退出到原始宿主机界面，就这样按，切换screen对话可能要用到。注意这里是暂时退出，而不是删除对话，在对话内使用 `exit` 就是退出并删除了
6. ` screen -R xxx -X quit`：删除名字是xxx的screen，简单理解：恢复xxx会话并执行退出


------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
