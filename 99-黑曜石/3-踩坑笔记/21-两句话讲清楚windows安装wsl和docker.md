---
tags:
  - docker
  - wsl
  - ubuntu
  - 容器
  - 镜像
banner: Cover/21.png
sticker: emoji//1f433
---
# 两句话讲清楚windows安装wsl和docker

> 我不会设置仅粉丝可见，不需要你关注我，仅仅希望我的踩坑经验能帮到你。如果有帮助，麻烦点个 :+1: 吧，这会让我创作动力+1 :grin:

[TOC]

## 写在前面

- 背景：win10/win11，微软商店打不开（打得开还不简单？能打开你直接搜别的攻略得了）
- 准备：
  - 先直接说一个结论：**不要考虑 Docker Desktop**，你都装wsl了，为什么还要用这玩意儿！此外，即使你想用，后续会遇到一个问题（怎么在wsl的linux系统里重启docker服务，没错，`systemctl restart docker` 会显示找不到docker服务，即使你能正常使用docker）
  - **不考虑微软商店安装**，不多比比，很多原因导致你的微软商店打不开，不折腾了，走离线安装，听我的。如果你能打开微软商店，很多事情就变得简单了，你自己看着办吧。


## 解决方案

1. [下载安装wsl2](https://zhuanlan.zhihu.com/p/680372783)：

   1. 先确认你的系统能不能安装wsl2，不能就赶紧放弃（我是22H2）

      > https://docs.docker.com/desktop/install/windows-install/
      >
      > - Windows 11 64-bit: Home or Pro version 21H2 or higher, or Enterprise or Education version 21H2 or higher.
      >
      > - Windows 10 64-bit:
      >   - We recommend Home or Pro 22H2 (build 19045) or higher, or Enterprise or Education 22H2 (build 19045) or higher.
      >   - Minimum required is Home or Pro 21H2 (build 19044) or higher, or Enterprise or Education 21H2 (build 19044) or higher.

   2. 很好，你满足了系统要求，已经成功一半了。继续 **配置环境**

      1. 启动控制面板，打开**hyperV**、**适用于Windows的linux子系统**、**虚拟机功能**，然后**重启**

         ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/41823d0d0cfa44e0a9611a35d4722793.png)

         ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/1c55ff5b5c0349118d8ec5b167950bd3.png)

      2. [下载wsl2安装包](https://learn.microsoft.com/zh-cn/windows/wsl/install-manual#step-2---check-requirements-for-running-wsl-2)：[wsl_update_x64.msi](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)，双击安装

2. 下载系统，比如ubuntu啥的

   1. https://learn.microsoft.com/zh-cn/windows/wsl/install-manual#downloading-distributions

      命令行下载、或者点击直接下载都可以，下载后是 `.appx` 后缀的文件

      ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/d534ce1f44cc442fbd197779d65ddf2c.png)

   2. 把这个 `.appx` 的文件复制到你想要放置系统的位置，比如 `D:\ubuntu22\` 下，**右键解压缩**（解压不了，就把后缀 `.appx` 改为 `.zip` 再解），解压后的文件列表如下：

      ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/4d75f1d64c3f4264886df924aa818399.png)

   3. 双击红色箭头指的文件就可以开始安装系统了，启动！完事儿后会让你输入用户名和密码，用户名就不说了，密码是未来你sudo要用的密码。

      ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/eeac0e8ef3ac4d6f9e5084d2b365787f.png)

   4. 安装完成后，开始菜单里面就能看到ubuntu了，双击打开。或者直接在命令行中输入ubuntu，也能打开。（打开后不要关，下面验证的时候，state才会显示为running）

   2. 检查安装好了没：`wsl --list --verbose`

      ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/b9602d440b3547d488b403e31a9d9244.png)
      
   6. 备注：[如果要卸载](https://www.cnblogs.com/choiiyill/articles/17826113.html)：`wsl --unregister Ubuntu`

3. 环境配置：

   1. wsl默认版本设置为2，ubuntu默认设置为wsl2

      其实这一步可以不做，如果你能正常进入ubuntu的话，不过有的教程做了，保险起见吧，先把这两行在powershell管理员启动里面跑了再说

      ```bash
      wsl --set-default-version 2
      wsl.exe --set-version Ubuntu 2
      ```

   2. systemctl命令启动

      - wsl安装的ubuntu里是没法用systemctl的，因为是init

        > WSL2 本身是由 Windows 负责运行的，因此使用 tree 或 ps 命令时会看到根进程不是 systemd，这将导致无法启动 Linux 系统服务的守护进程(deamon)。当我们执行 systemctl 命令的时候，会显示出我们的 init system (PID 1) 并非 systemd，而是微软提供的 /init。

      - 太坑爹了是吧，别搜，听我的，现在网上一堆解决问题，其实已经outdated，因为**微软已经解决了！**

        > https://devblogs.microsoft.com/commandline/systemd-support-is-now-available-in-wsl/
        >
        > Systemd support is now available in WSL!
        >
        > ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/956c06a9eb4241c4b260f10d11290d64.png)

      - 所以这事儿简单，听微软的

        1. sudo创建文件：`/etc/wsl.conf`

        2. 写入以下内容并保存：

           ```bash
           [boot]
           systemd=true
           ```

        3. 关掉ubuntu，关掉wsl的窗口，启个命令行关掉wsl

           ```bash
           wsl --shutdown
           ```

        4. 重新打开就发现 `systemctl` 能用了，这一步是干啥呢，后面 `systemctl restart docker` 改docker镜像要用啊
      
   3. root启动：su

      - 你直接 `su`，然后输入密码是报错的：`su: Authentication failure`
      - [怎么解决呢](https://blog.csdn.net/weixin_47872288/article/details/120631212)：`sudo passwd root`，重新输入密码就行了，后面直接su进入root用户开搞，不然什么都要sudo，麻烦的嘞

4. 配置ubuntu的源（22.04）

   1. 备份原来的：`cp /etc/apt/sources.list /etc/apt/sources.list.bak`

   2. [修改并更新](https://blog.csdn.net/FL1623863129/article/details/134229831)：`vim /etc/apt/sources.list`

      ```
      # 选一家的就行了
      # aliyun
      deb http://mirrors.aliyun.com/ubuntu/ jammy main restricted universe multiverse
      deb-src http://mirrors.aliyun.com/ubuntu/ jammy main restricted universe multiverse
      deb http://mirrors.aliyun.com/ubuntu/ jammy-security main restricted universe multiverse
      deb-src http://mirrors.aliyun.com/ubuntu/ jammy-security main restricted universe multiverse
      deb http://mirrors.aliyun.com/ubuntu/ jammy-updates main restricted universe multiverse
      deb-src http://mirrors.aliyun.com/ubuntu/ jammy-updates main restricted universe multiverse
      deb http://mirrors.aliyun.com/ubuntu/ jammy-proposed main restricted universe multiverse
      deb-src http://mirrors.aliyun.com/ubuntu/ jammy-proposed main restricted universe multiverse
      deb http://mirrors.aliyun.com/ubuntu/ jammy-backports main restricted universe multiverse
      deb-src http://mirrors.aliyun.com/ubuntu/ jammy-backports main restricted universe multiverse
      
      # tsinghua
      deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
      deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
      deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
      deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
      deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
      deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
      deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
      deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
      deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse
      deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse
      # 中科大
      deb https://mirrors.ustc.edu.cn/ubuntu/ jammy main restricted universe multiverse
      deb-src https://mirrors.ustc.edu.cn/ubuntu/ jammy main restricted universe multiverse
      deb https://mirrors.ustc.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
      deb-src https://mirrors.ustc.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
      deb https://mirrors.ustc.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
      deb-src https://mirrors.ustc.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
      deb https://mirrors.ustc.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
      deb-src https://mirrors.ustc.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
      deb https://mirrors.ustc.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse
      deb-src https://mirrors.ustc.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse
      # 163
      deb http://mirrors.163.com/ubuntu/ jammy main restricted universe multiverse
      deb http://mirrors.163.com/ubuntu/ jammy-security main restricted universe multiverse
      deb http://mirrors.163.com/ubuntu/ jammy-updates main restricted universe multiverse
      deb http://mirrors.163.com/ubuntu/ jammy-proposed main restricted universe multiverse
      deb http://mirrors.163.com/ubuntu/ jammy-backports main restricted universe multiverse
      deb-src http://mirrors.163.com/ubuntu/ jammy main restricted universe multiverse
      deb-src http://mirrors.163.com/ubuntu/ jammy-security main restricted universe multiverse
      deb-src http://mirrors.163.com/ubuntu/ jammy-updates main restricted universe multiverse
      deb-src http://mirrors.163.com/ubuntu/ jammy-proposed main restricted universe multiverse
      deb-src http://mirrors.163.com/ubuntu/ jammy-backports main restricted universe multiverse
      ```

   3. 刷新：`apt-get update && apt-get upgrade`

5. 下载安装docker并配置国内代理：[在wsl2中安装Docker，非Docker Desktop方案](https://www.ctyun.cn/developer/article/595016087945285)

   1. 安装必要的证书并允许 apt 包管理器使用以下命令通过 HTTPS 使用存储库

      ```bash
      apt install apt-transport-https ca-certificates curl software-properties-common gnupg lsb-release
      ```

   2. 运行下列命令添加 Docker 的官方 GPG 密钥：

      ```bash
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
      ```

   3. 添加 Docker ~~*官方*~~ **清华** 库

      ```bash
      add-apt-repository \
         "deb [arch=amd64] https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/ubuntu \
         $(lsb_release -cs) \
         stable"
      ```

   4. 安装docker

      ```bash
      apt install docker-ce docker-ce-cli containerd.io docker-compose
      ```

   5. 配置docker国内源：docker就没辙了，默认源肯定不行，所以

      - 创建文件 `/etc/docker/daemon.json`

      - 写入下面内容并保存

        ```json
        {
            "registry-mirrors" : [
              "https://docker.registry.cyou",
              "https://docker-cf.registry.cyou",
              "https://dockercf.jsdelivr.fyi",
              "https://docker.jsdelivr.fyi",
              "https://dockertest.jsdelivr.fyi",
              "https://mirror.aliyuncs.com",
              "https://dockerproxy.com",
              "https://mirror.baidubce.com",
              "https://docker.m.daocloud.io",
              "https://docker.nju.edu.cn",
              "https://docker.mirrors.sjtug.sjtu.edu.cn",
              "https://docker.mirrors.ustc.edu.cn",
              "https://mirror.iscas.ac.cn",
              "https://docker.rainbond.cc"
          ]
        }
        ```

      - 重载和重启：好家伙，这时候 `systemctl` 就能用上了， 这个地方卡了我好久，气死了家人们

        ```bash
        systemctl daemon-reload
        systemctl restart docker
        
        # 开机自启docker
        systemctl enable docker
        ```

      - 检查一下docker换源成功没：`docker info`，往下翻，Registry Mirrors里面就是你的源

   6. 验证一下docker好不好使吧：`docker pull hello-world`

   最后：其实我不是很明白5中一顿操作安装`docker-ce`，还不如直接 `apt install docker.io`

   > [!question] docker-ce 和 docker.io
   >
   > https://blog.csdn.net/harryhare/article/details/106015022
   >
   > - docker-ce 是 docker 官方维护的
   > - docker.io 是 Debian 团队维护的
   > - docker.io 采用 apt 的方式管理依赖
   > - docker-ce 用 go 的方式管理依赖，会自己管理所有的依赖。

6. 显卡驱动安装，搞AI怎么能不考虑显卡呢

   1. 其实我是先安装的cuda驱动：`apt install nvidia-cuda-toolkit`，装完了可以用 `nvcc -V` 查看版本

      ```bash
      (base) root@L2010403019000:/home/litian# nvcc -V
      nvcc: NVIDIA (R) Cuda compiler driver
      Copyright (c) 2005-2021 NVIDIA Corporation
      Built on Thu_Nov_18_09:45:30_PST_2021
      Cuda compilation tools, release 11.5, V11.5.119
      Build cuda_11.5.r11.5/compiler.30672275_0
      ```

   2. 其次我才装nvidia驱动：`apt install nvidia-utils-545`，后面545是我自己选的。因为用 `nvidia-smi` 指令会看到艺堆可选的，我直接选择了最新的，安装完成后同样可以看到 `nvidia-smi` 的情况

      ```bash
      (base) root@L2010403019000:/home/litian# nvidia-smi
      Thu Jan  9 11:02:51 2025
      +---------------------------------------------------------------------------------------+
      | NVIDIA-SMI 545.29.06              Driver Version: 538.78       CUDA Version: 12.2     |
      |-----------------------------------------+----------------------+----------------------+
      | GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
      | Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
      |                                         |                      |               MIG M. |
      |=========================================+======================+======================|
      |   0  NVIDIA RTX 3500 Ada Gene...    On  | 00000000:01:00.0  On |                  Off |
      | N/A   42C    P8               7W / 123W |    532MiB / 12282MiB |      0%      Default |
      |                                         |                      |                  N/A |
      +-----------------------------------------+----------------------+----------------------+
      
      +---------------------------------------------------------------------------------------+
      | Processes:                                                                            |
      |  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
      |        ID   ID                                                             Usage      |
      |=======================================================================================|
      |  No running processes found                                                           |
      +---------------------------------------------------------------------------------------+
      ```

      > [!question] wsl中的docker和docker desktop的冲突
      >
      > 奇了怪了，因为我两个都装了，我发现了一个问题：
      >
      > 1. 如果没启动docker desktop，那么在wsl中看docker是wsl的ubuntu自带的
      > 2. 如果启动了docker desktop，那么在wsl中看docker是win10的docker desktop
      > 3. 在2的基础上关闭docker desktop，那么wsl的ubuntu中docker会出问题，看不到`docker ps`，报错：`Cannot connect to the Docker daemon at unix: ///var/run/docker.sock.`


------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
