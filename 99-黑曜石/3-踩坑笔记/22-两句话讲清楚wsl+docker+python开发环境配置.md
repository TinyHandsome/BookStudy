---
tags:
  - 容器
  - docker
  - wsl
  - conda
  - python
banner: Cover/22.png
sticker: emoji//1f433
---
# 两句话讲清楚wsl+docker+python开发环境配置


[TOC]

## 写在前面

- 背景：win10下wsl+docker整好了之后，还要做什么，windows下载的东西怎么到docker容器里面？win->wsl->容器怎么传好使？
- 准备
  - 先配置：[wsl+docker](https://blog.csdn.net/qq_21579045/article/details/143155408)，教程我独立出来了
  - docker下载ubuntu镜像：`docker pull ubuntu:22.04`
  - 启容器：`docker run --privileged=true -it --name huowang -v /huowang:/data ubuntu:22.04`
    - `--privileged=true`：哎呀，多的不说了，只要后面要挂在 `-v` 就要加这个
    - `-it`：交互式terminal
    - `--name`：取个名字吧，给容器
    - `-v`：目录挂载


## 解决方案

1. 下载miniconda：https://docs.anaconda.com/miniconda/

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/2505fbfeff354d608943991e3a34ba13.png)

2. 拷贝 `Miniconda3-latest-Linux-x86_64.sh` 到wsl的ubuntu里

   - 没错，直接复制粘贴就行
   - **注意：放在home里面**，别问，问就是其他的地方粘贴会**[没权限](https://blog.csdn.net/zero_with_one/article/details/131772057)**

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/7bcc6be8b90246eebd4c8fea0ad42262.png)

3. 从wsl的ubuntu拷贝到容器中并安装

   - 由于你的容器是 `-v` 挂载了的，所以就很方便

   - 直接 `cp Miniconda3-latest-Linux-x86_64.sh /huowang`，就直接把文件搞进去了，爽吧

   - 接下来直接安装就行：`bash Miniconda3-latest-Linux-x86_64.sh`

     应该有执行权限吧，没有就`chmod +x`，这都不是事儿

   - 一顿确认安装就行了

4. 检查一下conda好不好使吧：`conda -v`

5. 多说一句，conda的配置，[避免新建环境各种error的问题](https://blog.csdn.net/leviopku/article/details/140280296)

   `vim ~/.condarc` 写入以下内容就行了

   ```bash
   channels:
     - defaults
   show_channel_urls: true
   default_channels:
     - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
     - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
     - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
   custom_channels:
     conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
     pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
   ```

最后，类似的，其他的sh啊，什么的，都可以这样传进来安装，当然了能直接下载 `apt install` 是最好的。


------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
