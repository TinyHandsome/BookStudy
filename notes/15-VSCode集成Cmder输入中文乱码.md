# VSCode集成Cmder输入中文乱码

[TOC]

## 写在前面

- 环境

  - VSCode
  - Cmder
  - Win10

- 问题

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












------

- :cloud: 我的CSDN：https://blog.csdn.net/qq_21579045
- :snowflake: 我的博客园：https://www.cnblogs.com/lyjun/
- :sunny: 我的Github：https://github.com/TinyHandsome
- :rainbow: 我的bilibili：https://space.bilibili.com/8182822
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友

