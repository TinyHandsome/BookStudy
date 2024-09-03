# 尚硅谷Docker实战教程学习笔记

[TOC]

## 写在前面

- 封面 | 摘要 | 关键词

  尚硅谷Docker实战教程

  ```
  docker
  李英俊
  尚硅谷
  ```

- 学习链接：[尚硅谷Docker实战教程（docker教程天花板）](https://www.bilibili.com/video/BV1gr4y1U7CY)

- 感想 | 摘抄 | 问题

  - [麒麟系统离线安装docker](https://blog.csdn.net/qq_21579045/article/details/141718124)
  - 操作
    - `docker images`：查看已有镜像


## 1. Docker简介

1. **是什么**

   - 为什么会有docker出现

     **系统平滑移植，容器虚拟化技术**

     Docker的出现使得Docker得以打破过去「程序即应用」的观念。透过镜像(images)将作业系统核心除外，运作应用程式所需要的系统环境，由下而上打包，达到应用程式跨平台间的无缝接轨运作。

     ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/df69ab7f7e9246699fa47a9feb477e6d.png)

   - docker的理念

     ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/0e0cc8c01b0d4e1485d29b60a4671632.png)

   - Docker是基于Go语言实现的云开源项目

   - Docker的主要目标是：**Build, Ship and Run Any App, Anywhere**。也就是通过对应用组件的封装、分发、部署、运行等生命周期的管理，使用户的APP及其运行环境能够做到 **一次镜像，处处运行**

   - **Docker解决了运行环境和配置问题的软件容器，方便做持续集成并有助于整体发布的容器虚拟化技术**

2. **容器与虚拟机比较**

   1. 虚拟机（virtual machine）就是带环境安装的一种解决方案。

      - 缺点：资源占用多，冗余步骤多，启动慢

   2. 由于前面虚拟机存在缺点，Linux发展出了另一种虚拟化技术：**Linux容器（Linux Containers，LXC）**。

      - Linux容器是与系统其他部分隔离开的一系列进程，从另一个镜像运行，并由该镜像提供支持进程所需的全部文件。容器提供的镜像包含了应用的所有依赖项，因而在从开发到测试再到生产的整个过程中，它都具有**可移植性**和**一致性**。

      - Docker容器是在**操作系统层面**上实现虚拟化，直接复用本地主机的操作系统，而传统虚拟机则是在**硬件层面**实现虚拟化。与传统的虚拟机相比，Docker优势体现为启动速度快，占用体积小。

      ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/ae15d2f6d4aa4d79bff940cf373f14e9.png)

   3. 总结

      - 传统虚拟机技术是虚拟出一套硬件后，在其上运行一个完整的操作系统，在该系统上再运行所需应用进程；
      - 容器内的应用进程直接运行于宿主的内核，容器内没有自己的内核且也没有进行硬件虚拟。因此容器要比传统虚拟机更为轻便；
      - 每个容器之间互相隔离，每个容器有自己的文件系统，容器之间进程不会相互影响，能区分计算资源。

3. **能干嘛**

   1. 技术职级的变化：coder->programmer->software engineer->DevOps engineer

   2. 开发/运维（DevOps）新一代开发工程师

      - 一次构建、随处运行

        - 更快的应用交付和部署
        - 更便捷的升级和扩缩容
        - 更简单的系统运维
        - 更高效的计算资源利用

      - Docker的应用场景

        ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/66c615f46df949d18f034c41e6b3e19e.png)

4. **去哪儿下**

   - docker官网：http://www.docker.com/
   - Docker Hub仓库：http://www.hub.docker.com/，安装docker镜像的仓库

## 2. Docker安装

1. **前提说明**
   1. Docker 并非是一个通用的容器工具，它依于已存在并运行的 Linux 内核环境。
   2. Docker 实质上是在已经运行的 Linux 下制造了个隔离的文件环境，因此它执行的效率几乎等同于所部署的 Linux 主机。
   3. 因此
      Docker 必须部署在 Linux 内核的系统上，如果其他系统想部署 Docker 就必须安装一个虚拟 Linux 环境。
   4. 获取系统版本内核：`uname -r`
   
2. docker的基本组成
   1. 镜像，image ==类==
      - `Redis r1 = docker run 镜像`类似鲸鱼背上的集装箱，就是一个容器实例
      
   2. 容器，container ==实例==
      - 上述的 r1、r2、r3...多个实例
      - 容器是用镜像创建的运行实例
      - 可以看作是一个简易版的Linux环境（包括root用户权限、进程空间、用户空间和网络空间等）和运行在其中的应用程序。
      
   3. 仓库，repository ==存放镜像的地方==
      - Maven仓库：放各种jar包
      - Github仓库：放各种git项目
      - Docker Hub：放各种镜像模板
      
   4. 小总结：image文件可以看作是容器的模板，Docker根据image文件生成容器的实例。同一个image文件，可以生成多个同时运行的容器实例。
   
      ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/c4ded02074a042efabcbb91dcc926ed2.png)
   
      ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/6c66af26dd4044d4990590b53bcdffa2.png)
   
      - docker daemon：真正干活的，通过Socket连接从客户端访问，守护进程从客户端接收命令并管理运行在主机上的容器。
   
3. docker平台架构

   - docker是一个C/S模式的架构，后端是一个松耦合架构，众多模块各司其职

     ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/8e1cb78b23ff46dba02edb4d9c9a280a.png)

   - Docker运行的基本流程：

     - 用户使用Docker Client与Docker Daemon建立通信，并发送请求给后者
     - Docker Daemon作为Docker架构中的主体部分，首先提供Docker Server的功能，使其可以接收Docker Client的请求
     - Docker Engine执行Docker内部的一系列工作，每一项工作都是以一个Job的形式存在
     - Job的运行过程中，当需要容器镜像时，则从Docker Registry中下载镜像，并通过镜像管理驱动Graph driver将下载镜像以Graph的形式存储
     - 当需要为Docker创建网络环境时，通过网络管理驱动Network driver创建并配置Docker容器网络环境
     - 当需要限制docker容器运行资源或者执行用户指令等操作时，则通过Exec driver来完成
     - Libcontainer是一项独立的容器管理包，Network driver以及Exec driver都是通过Libcontainer来实现具体对容器进行的操作

4. 安装步骤

   1. 确定版本
   2. 卸载旧版本
   3. yum安装gcc相关
      1. 能上外网（CentOS7）
      2. `yum -y install gcc`
      3. `yum -y install gcc-c++`
   4. 安装需要的软件包
      1. `yum install -y yum-utils`
      2. 配置docker库：`yum-config-manager --add-repo https://xxx`
      3. 推荐使用阿里云的加速：`yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo`
      4. 更新yum软件包索引：`yum makecache fast`
   5. 安装docker：`yum install docker-ce docker-ce-cli containerd.io`
   6. 启动docker：`systemctl start docker`
   7. HelloWorld：`docker run hello-world`、`docker version`
      - 本地没有hello-world，则会从远程库拉下来运行
   8. 卸载：
      - `systemctl stop docker`
      - `yum remove docker-ce docker-ce-cli containerd.io`
      - `rm -rf /var/lib/docker`
      - `rm -rf /var/lib/containerd`
   
5. **阿里云镜像加速**

   1. 是什么：https://promotion.aliyun.com/ntms/act/kubernetes.html

   2. 注册账户，工具台，容器镜像服务，镜像工具，镜像加速器，**获取加速器地址链接**：https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors

      ```bash
      # 创建目录，将镜像配置反写回文件
      sudo mkdir -p /etc/docker
      sudo tee /etc/docker/daemon.json <<-'EOF'
      {
        "registry-mirrors": ["https://[你自己的].mirror.aliyuncs.com"]
      }
      EOF
      
      # 重启docker
      sudo systemctl daemon-reload
      sudo systemctl restart docker
      ```

   3. 
























------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045/`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome/`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822/`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj/`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_/`
- :potato: 我的豆瓣：`https://www.douban.com/people/lyjun_/`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
