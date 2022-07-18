# VSCode集成Cmder控制台输入中文乱码

[TOC]

## 写在前面

- 环境

  - VSCode
  - Cmder
  - Win10

- 问题

  - 根据方法1配置VSCode后，在终端输入中文会出现下图的乱码，查看 `locale charmap` 显示的编码不是 `UTF-8`

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/8e57b32ada62483f87371db182773864.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

- 参考链接

  - [方法1](https://zhuanlan.zhihu.com/p/304522286)

    ```json
    "git.enabled": true,
    "git.path": "D:\\cmder\\vendor\\git-for-windows\\cmd\\git.exe",
    "terminal.integrated.shell.windows": "D:\\cmder\\vendor\\git-for-windows\\bin\\bash.exe",
    ```

  - [方法2](https://blog.csdn.net/leonhe27/article/details/81210000)

    ```json
    "terminal.integrated.shell.windows": "cmd.exe",
    "terminal.integrated.env.windows": {"CMDER_ROOT": "D:\\cmder"},
    "terminal.integrated.shellArgs.windows": ["/k", "D:\\cmder\\vendor\\init.bat"],
    ```

## 解决方案

1. 我们看一下两者的配置，就能看出不同了

   - 方法1用的是cmder内置的git和bash，讲道理我查了很久到没有看到怎么设置cmder 的bash.exe中的编码，各种设置都没法实现编码设为 `UTF-8`，即使用如下配置：

     ```
     set LANG=zh_CN.utf8
     set LC_ALL=zh_CN.utf8
     ```

   - 方法2用的是系统自带的cmd作为shell，然后调用cmder的环境，并初始化cmder，我的理解就是：在cmd中直接输入 `cmder` 

   - 方法1和方法2的界面还是有区别的

2. 结论：**用方法2就好**

3. 我真的是查遍全网没找到解决方案，所以自己研究了半天，才直到两者的差异的，**给个赞不过分吧**


------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
