---
tags:
  - docker
  - 尚硅谷
---
# 尚硅谷Docker实战教程学习笔记

[toc]

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

  - 什么是云原生：（我的理解）一切在云端，基于容器开发的都会打包push到registry中，然后pull下来进行使用

  - [麒麟系统离线安装docker](https://blog.csdn.net/qq_21579045/article/details/141718124)

  - 开发流程：
  
    ```mermaid
    graph LR
    编码开发微服务-->上线部署容器化-->时时刻刻要监控-->devops
    ```

  - **面试题快速跳转：**
  
    - [谈谈docker虚悬镜像是什么？](#1)
    - [谈谈docker exec和docker attach两个命令的区别？工作中用哪一个？](#2)
    - [为什么Docker镜像要采用分层结构？](#3)
    - [容器创建成功但是启不起来](#4)


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

1. 前提说明
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

5. 阿里云镜像加速

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

6. 测试运行hello-world

   - `docker run hello-world`

   - run到底干了什么

     ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/df04829d096b496d87d148781f0bc6c9.png)

7. 底层原理：为什么Docker会比VM虚拟机要快

   - docker有着比虚拟机更少的抽象层

     由于docker不需要Hypervisor（虚拟机）实现硬件层面的虚拟化，运行在docker容器上的程序直接使用的都是实际物理机的硬件资源。因此在CPU、内存利用率上，docker将会在效率上有明显优势。

   - docker利用的是宿主机的内核，而不需要加载操作系统os内核

     当新建一个容器时，docker不需要和和虚拟机一样重新加载一个操作系统内核。进而避免引寻、加载操作系统内核返回等比较费时费资源的过程，当新建一个虚拟机时，虚拟机软件需要加载OS，返回新建过程是分钟级别的。而docker由于直接利用宿主机的操作系统，则省略了返回过程，因此新建一个docker容器只需要几秒钟。

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/af41bbd8acae4e38b0d847873b89be08.png)

   |            | docker容器              | 虚拟机VM                       |
   | :--------- | ----------------------- | ------------------------------ |
   | 操作系统   | 与宿主机共享OS          | 宿主机OS上运行虚拟机OS         |
   | 存储大小   | 镜像小，便于存储与运输  | 镜像庞大（vmdk、vdi等）        |
   | 运行性能   | 几乎无额外性能损失      | 操作系统额外的ＣＰＵ、内存消耗 |
   | 移植性     | 轻便、灵活，适用于Linux | 笨重，与虚拟化技术耦合度高     |
   | 硬件亲和性 | 面向软件开发者          | 面向硬件运维者                 |
   | 部署速度   | 快速，秒级              | 较慢，10s以上                  |

## 3. Docker常用命令

1. 帮助启动类命令

   - `systemctl start docker`：启动docker
   - `systemctl stop docker`：停止docker
   - `systemctl restart docker`：重启docker
   - `systemctl status docker`：查看docker状态
   - `systemctl enable docker`：开机启动docker
   - `docker info`：查看docker概要信息
   - `docker --help`：查看docker总体帮助文档
   - `docker 具体命令 --help`：查看docker命令帮助文档

2. 镜像命令

   - `docker images`：列出本地主机上的镜像

     同一个仓库源可以有多个tag版本，代表这个仓库源的不同的版本，我们使用 `REPOSITORY:TAG `来定义不同的镜像。如果你不指定一个镜像的版本标签，例如你只使用 ubuntu，docker将默认使用 ubuntu:latest 镜像。

     ```
     REPOSITORY：表示镜像的仓库源
     TAG：镜像的标签
     IMAGE ID：镜像ID
     CREATED：镜像创建时间
     SIZE：镜像大小
     ```

     OPTIONS说明：

     - `-a`：列出本地所有的镜像（含历史镜像层）
     - `-q`：；只显示镜像ID

   - `docker search 镜像名`：默认是从 `hub.docker.com` 上检索镜像列表，一般选第一个官方认证过的，比较靠谱

     OPTIONS说明：

     - `--limit`：只列出N个镜像，默认25个，例如`docker search --limit 5 redis`

   - `docker pull 镜像名`：下载镜像，`docker pull 镜像名字[:TAG]`，没有tag就下载最新版

   - `docker system df`：查看镜像/容器/数据卷所占的空间

   - `docker rmi [-f] 镜像名/镜像ID`：[强制]删除镜像

     - 删除多个镜像：`docker rmi -f id1 name2:tag2`
     - 删除全部镜像：`docker rmi -f $(docker images -qa)`

   > :question: <span id="1">谈谈docker虚悬镜像是什么？</span>
   >
   > - 是什么：仓库名、标签都是<none>的镜像，俗称虚悬镜像 dangling image
   >
   > :book: [参考延申](https://blog.csdn.net/Wod_7/article/details/132983731)
   >
   > 虚悬镜像可能会在以下几种情况下**产生**：
   >
   > 1. 构建过程中出现错误，导致镜像没有被正确标记。
   > 2. 用户忘记为新创建的镜像添加标签。
   > 3. 用户试图删除一个正在被使用的镜像，但该镜像仍有其他容器在使用。
   >
   > 虚悬镜像可能会带来一些**问题**：
   >
   > - 无法找到正确的镜像版本：当用户试图运行一个虚悬镜像时，他们可能无法确定应该使用哪个版本的镜像。这可能导致应用程序运行在不同的环境中，或者在不同版本的代码上运行，从而导致兼容性问题。
   > - 无法进行有效的更新：虚悬镜像意味着用户无法对其进行更新。即使镜像内部的版本进行了升级，用户也无法通过简单地添加一个新标签来获取这个新版本的镜像。
   > - 占用存储空间：虽然虚悬镜像不会立即影响应用程序的运行，但是它们会一直占用存储空间，直到有人为它们添加标签。
   >
   > 如何**解决**虚悬镜像问题，我们可以采取以下几种方案：
   >
   > - 检查并重新标记镜像：如果发现虚悬镜像，可以尝试查找出现问题的构建过程，并修复其中的错误。然后为镜像添加一个新的标签，以确保用户能够找到正确的版本。
   > - 使用Dockerfile：Dockerfile可以帮助我们自动化镜像的构建过程，并确保每次构建的镜像都是正确且可重复的。通过编写详细的Dockerfile，我们可以确保每次构建的镜像都带有正确的标签。
   > - 定期清理虚悬镜像：Docker提供了一些命令来帮助用户管理虚悬镜像，例如`docker rmi --force`可以强制删除虚悬镜像。然而，最好的方法还是定期检查并清理这些无用的虚悬镜像，以节省存储空间。

3. 容器命令

   有镜像才能创建容器，这是根本前提

   - `docker run 镜像名`：新建+启动容器，启动交互式容器（前台命令行）

     - `--name=名字`：容器新名字，为容器指定一个名称
     - `-d`：后台运行容器并返回容器ID，启动守护式容器（后台运行）
     - `-i`：以交互模式运行容器，通常与 `-t` 同时使用
     - `-t`：为容器重新分配一个伪输入中断，通常与 `-i` 同时使用，也称交互式容器（前台有伪终端，等待交互）常用：`docker run -it ubuntu /bin/bash`（以交互模式启动一个容器，在容器内执行 /bin/bash 命令，退出：exit）
     - `-P`：随机端口映射，大P
     - `-p`：指定端口映射，小p。例：`-p 6379:6379`是指外面访问docker的6379服务（宿主机）被映射到容器内的6379服务（docker ）

   - `docker ps`：列出当前所有正在运行的容器

     - `-a`：列出当前所有正在运行的容器+历史上运行过的
     - `-l`：显示最近创建的容器
     - `-n`：显示最近n个创建的容器
     - `-q`：静默模式，只显示容器编号

   - 容器的退出

     1. `exit`：run进去的容器，exit退出，容器停止（docker ps就没啦）
     2. `ctrl+p+q`：run进去的容器，ctrl+p+q，容器不停止

   - `docker start 容器id/容器名`：启动已经停止运行的容器

   - `docker restart 容器id/容器名`：重启容器

   - `docker stop 容器id/容器名`：停止容器

   - `docker kill 容器id/容器名`：强制停止容器

   - `docker rm [-f] 容器id/容器名`：[强制]删除容器

     一次性删除多个实例：

     - `docker rm -f $(docker ps -a -q)`
     - `docker ps -a -q | xargs docker rm`

4. 其他

   - 启动守护式容器（后台服务器）

     - 在大部分得场景下，我们希望docker的服务是在后台运行的，，我们可以通过 `-d` 指定容器的后台运行模式

     - `docker run -d 容器名`

       > 问题：直接用 `docker run 容器名` 启动后用`docker ps -a`进行查看发现容器已经退出了，需要注意很重要的一点是，**Docker容器后台运行，就必须有一个前台进程**。容器运行的命令如果不是那些一直挂起的命令（比如运行top，tail），就是会自动退出的。
       >
       > 这是docker的机制问题，最佳的解决方案是：**将你要运行的程序以前台进程的形式运行，常见就是命令行模式 `-it` **，表示我还有交互操作，别中断。

     - 以redis为例，用前台交互式的启动肯定不行：`docker run -it redis`；所以要用后台守护式启动：`docker run -d redis`

   - `docker log 容器id`：查看容器日志

   - `docker top 容器id`：查看容器内运行的进程

   - `docker inspect 镜像名/容器id`：查看镜像配置/查看容器内部细节

   - **进入正在运行的容器，并以命令行交互**

     - `docker exec -it 容器id bashShell`
     - 重新进入还有一个命令：`docker attach 容器id`

     > :question: <span id="2">上述两个命令的区别？工作中用哪一个？</span>
     >
     > - attach直接进入容器启动命令的终端，不会启动新的进程，用exit退出，会导致容器的停止
     > - exec是在容器中打开新的终端，并且可以启动新的进程，用exit退出，不会导致容器的停止
     >
     > 推荐在工作中使用 `docker exec` 命令，因为退出容器终端也不会导致容器的停止
     >
     > 一般用 `-d` 后台启动的程序，再用 `docker exec`进入对应容器实例

   - `docker cp 容器id:容器内路径 目的主机路径`：从容器内拷贝文件到主机上

   - 导入导出容器：

     - export 导出容器的内容留作为一个tar归档文件[对应import命令]
     - import 从tar包中的内容创建一个新的文件系统再导入为镜像[对应export]
     - 案例
       - `docker export 容器id > 文件名.tar`
       - `cat 文件名.tar | docker import - 镜像用户/镜像名:镜像版本号`，例如：`cat abcd.tar | docker import - atguigu/ubuntu:3.7`

     > :sunny: docker save和docker export的区别
     >
     > :book: [docker知识点大全](https://www.cnblogs.com/happy-king/p/10028476.html)
     >
     > 1. `docker save`保存的是镜像（image），`docker export`保存的是容器（container）；
     > 2. `docker load`用来载入镜像包，`docker import`用来载入容器包，但两者都会恢复为镜像；
     > 3. `docker load`不能对载入的镜像重命名，而`docker import`可以为镜像指定新名称。

5. 小结

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/77f0c79ab6994c40acfb72cd1684a1cb.png)

## 4. Docker镜像

1. 是什么：镜像是一种轻量级、可执行的独立软件包，它包含运行某个软件所需的所有内容，我们把应用程序和配置依赖打包好形成一个可交付的运行环境(包括代码、运行时需要的库、环境变量和配置文件等)，这个打包好的运行环境就是image镜像文件。

2. 分层的镜像：UnionFS（联合文件系统），Union文件系统（UnionFS）是一种分层、轻量级并且高性能的文件系统，它支持**对文件系统的修改作为一次提交来一层层的叠加**，同时可以将不同目录挂载到同一个虚拟文件系统下（unite several directories into a single virtual filesystem）。Union 文件系统是 Docker镜像的基础。**镜像可以通过分层来进行继承**，基于基研镜像（没有父镜像），可以制作各和具体的应用镜像。

   特性：一次同时加载多个文件系统，但从外面看起来，只能看到一个文件系统，联合加载会把各层文件系统叠加起来，这样最终的文件系统会包含所有底层的文件和目录

3. Docker镜像加载原理：docker的镜像实际上由一层一层的文件系统组成，这种层级的文件系统UnionFS。

   bootfs(boot file system)主要包含bootloader和kernel, bootloader主要是引导加载kernel，Linux刚启动时会加载bootfs文件系统，**在Docker镜像的最底层是引导文件系统bootfs**。这一层与我们典型的Linux/unix系统是一样的，包含boot加载器和内核。当boot加载完成之后整个内核就都在内存中了，此时内存的使用权已由bootfs转交给内核，此时系统也会卸载bootfs。

   rootfs (root file system)，在bootfs之上，包含的就是典型 Linux 系统中的`/dev`，`/proc`，`/bin`，`/etc`等标准目录和文件。rootfs就是各种不同的操作系统发行版，比如Ubuntu，Centos。

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/e73d9f92af0b492a85a1bcd4a3827a8c.png)

   > 对于一个精简的OS，rootfs可以很小，只需要包括最基本的命令、工具和程序库就可以了，因为底层直接用Host和Kernel，自己只需要提供rootfs就行了。由此可见对于不同的linux发行版，bootfs基本是一致的，rootfs会有差别，因此不同的发行版可以公用bootfs。

   > :question: <span id="3">为什么Docker镜像要采用分层结构？</span>
   >
   > 镜像分层最大的一个好处就是**共享资源**，方便复制迁移，就是为了**复用**。
   >
   > 比如说有多个镜像都从相同的 base 镜像构建而来，那么 Docker Host 只需在磁盘上保存一份 base 镜像；同时内存中也只需加载一份 base 镜像，就可以为所有容器服务了。而且镜像的每一层都可以被共享。

4. **重点理解**

   - Docker镜像层都是**只读**的，容器层是**可写**的
   - 当容器启动时，一个新的可写层被加载到镜像的顶部。这一层通常被称作“容器层"，**“容器层"之下的都叫“镜像层”**。

5. Docker镜像commit操作案例

   1. `docker commit` 提交容器副本，使之成为一个新的镜像

   2. `docker commit -m="提交的描述信息" -a="作者" 容器ID 要创建的目标镜像名称[:标签名]`

      ```bash
      docker commit -m="vim cmd add ok" -a="huowang" de60078e6a9a huowang/myubuntu:1.0
      docker images
      ```

6. 小结

   Docker中的镜像分层，**支持通过扩展现有镜像，创建新的镜像**。类似Java继承于一个Base基础类，自己再按需扩展。新镜像是从 base 镜像一层一层叠加生成的。每安装一个软件，就在现有镜像的基础上增加一层。

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/8cdf97e38e3245ec9316ef19dc6e85c8.png)

## 5. 本地镜像发布到阿里云

1. 本地镜像发布到阿里云流程

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/b4ba6662839649e3b2e6829fc88c0598.png)

2. 镜像的生成方法

   1. 方法1：基于当前容器创建一个新的镜像，新功能增强：`docker commit [OPTIONS] 容器ID [REPOSITORY[:TAG]]`
   2. 方法2：DockerFile

3. 将本地镜像推送到阿里云

   1. 选择控制台，进入容器镜像服务

   2. 选择个人实例

   3. 命名空间-创建命名空间

   4. 仓库名称-创建镜像仓库-选择命名空间-创建仓库名称-创建本地仓库-创建镜像仓库

   5. 进入管理界面获得脚本

   6. 将镜像推送到阿里云registry

      ```bash
      # 登录
      docker login --username=你的用户名 registry.cn.qingdao.aliyuncs.com
      # 输入密码，Login Succeeded就是登录成功
      docker tag [ImageId，即镜像id] registry.cn.qingdao.aliyuncs.com/命名空间/仓库名:[镜像版本号]
      docker push registry.cn.qingdao.aliyuncs.com/命名空间/仓库名:[镜像版本号]
      ```

4. 将阿里云上的镜像下载到本地

   ```bash
   docker login --username=你的用户名 registry.cn.qingdao.aliyuncs.com
   docker pull registry.cn.qingdao.aliyuncs.com/命名空间/仓库名:[镜像版本号]
   ```

## 6. 本地镜像发布到私有库

1. 是什么：官方是 `hub.docker.com`，国内一般选择阿里云，类似github，建立企业自己的github。**Docker Registry** 是官方提供的工具，用于构建私有镜像仓库。

2. 将本地镜像推送到私有库

   1. 下载镜像 Docker Registry：`docker pull registry`

   2. 运行私有库 Registry，相当于本地有个私有的Docker Hub：`docker run -d -p 5000:5000 -v /主机路径:/容器路径 --privileged=true registry`

      ==我的实践==：`docker run -d -p 5005:5000 -v /mydocker:/tmp/registry --privileged=true registry`，这里端口号试了下用5005做映射，看看好不好使

      > -p 主机端口映射到容器端口
      >
      > -v 将主机路径"/host/path"挂载到容器路径"/container/path"，这样容器中的应用就可以访问"/container/path"目录，并且任何对这个路径的更改都会反映在主机的"/host/path"上
      >
      > 默认情况下，仓库被创建在容器的 `/var/lib/registry` 目录下，建议自行用容器卷映射，方便宿主机联调

   3. 演示：创建一个新镜像，ubuntu安装ifconfig命令

      `apt install net-tools`

      1. 从Hub上下载ubuntu镜像到本地并成功运行
      2. 原始的Ubuntu镜像是不带着ifconfg命令的
      3. 外网连通的情况下，安装ifconfg命令并测试通过
      4. 安装完成后，commit我们自己的新镜像
      5. 启动我们的新镜像并和原来的对比

   4. curl验证私服库上有什么镜像

      - 根据上面的操作，pull并run了一个registry的容器；又打包了一个镜像，然后run，测试成功
      - `curl -XGET http://...:5000/v2/_catalog`
      - ==我的实践==：`curl -XGET http://...:5005/v2/_catalog`

   5. 将新镜像修改符合私服规范的Tag

      `docker tag 镜像名称[:TAG] http://...:5000/镜像名称[:TAG]`

      相当于把本机的镜像克隆了一份，按规范命名

      ==我的实践==：

      - 先把容器commit成镜像：`docker commit -m="my ubuntu" -a="huowang" huowang huowang/myubuntu:1.0`
      - 再修改tag：`docker tag huowang/myubuntu:1.0 ...:5005/huowangos:1.0`

   6. 修改配置文件使之支持http

      1. `vim /etc/docker/daemon.json`，我们曾经在这里配置过阿里云的镜像

         ```bash
         "registry-mirrors": ["https://xxx.mirrors.aliyuncs.com"]
         ```

      2. 后面再加一个：

         ```bash
         "insecure-registries": ["你的registry ip地址:5000"]
         ```

      3. docker默认不允许http方式推送镜像，通过配置选项来取消这个限制。修改完如果不生效，建议重启docker

      ==我的实践==：

      - 如果直接push，会报错：`GET ...: http: server gave HTTP response to HTTPS client`
      - 所以需要在 `daemon.json` 中增加对应的ip从而支持 HTTP
      - 然后重启docker `systemctl restart docker`，注意，这步操作会把你所有的镜像给关了，很要命的，小心点。
      - 最终push：`docker push ...:5005/huowangos:1.0`

   7. push推送到私服库：`docker push 镜像名称[:TAG]`，其实这里的镜像名称就是：`http://...:5005/镜像名称[:TAG]`

      1. curl验证私服库上有什么镜像：`curl -XGET http://...:5005/v2/_catalog`，应该就有啦

   8. pull到本地运行：`docker pull http://...:5005/镜像名称[:TAG]`

## 7. Docker容器数据卷

1. :no_entry_sign: 坑：容器卷记得加入 `--privileged=true`

   否则，Docker挂载主机目录访问会出现 `cannot open directory: Permission denied`

2. 参数v：默认情况下，仓库被创建在容器的 `/var/lib/registry` 目录下，建议自行用容器卷映射，方便宿主机联调

3. 是什么

   1. 有点类似我们redis里面的rdb和aof文件
   2. 将docker容器内的数据保存进宿主机的磁盘中
   3. 运行一个带有容器卷存储功能的容器实例

   > 卷是目录或文件，存在于一个或多个容器中，由docker挂载到容器，但不属于联合文件系统，因此能够绕过 Union File System 提供一些用于持续存储或共享数据的特性。卷的设计目的就是`数据的持久化`，完全独立于容器的生存周期，因此Docker不会在容器删除时删除其挂载的数据卷
   >
   > `docker run -it -privileged=true -v /宿主机绝对路径目录:/容器内目录 镜像名`

4. 能干嘛：将运用与运行的环境打包镜像，run后形成容器实例运行，但是我们对数据的要求希望是持久化的。Docker容器产生的数据，如果不备份，那么当容器实例删除后，容器内的数据自然也就没有了。为了能保存数据在docker中我们使用卷。

   特点：

   1. 数据卷可在容器之间共享或重用数据
   2. 卷中的更改可以直接实时生效
   3. 数据卷中的更改不会包含在镜像的更新中
   4. 数据卷的生命周期一直持续到没有容器使用它为止

5. 案例：

   1. 宿主vs容器之间映射添加容器卷，直接命令添加

      - `docker run -it -privileged=true -v /宿主机绝对路径目录:/容器内目录 镜像名`

      - 查看数据卷是否挂载成功：可以在主机上看到 `/mydocker`，然后启动容器 `docker exec -it 容器id /bin/sh`（因为没有bash），在容器的路径中看到 `/tmp/registry`

      - 也可以用 `docker inspect 容器id`，查看mount字段中的内容

        ```bash
        "Mounts": [
            {
                "Type": "bind",
                "Source": "/mydocker",
                "Destination": "/tmp/registry",
                "Mode": "",
                "RW": true,
                "Propagation": "rprivate"
            },
            ...
        ]
        ```

      - **注意：**如果把容器 `docker stop` 之后，在宿主机路径下增加文件，重启容器之后，容器内部依然能看到对应的文件增加

   2. 读写规则映射添加说明

      - 读写（默认）
        - `docker run -it --privileged=true -v /宿主机绝对路径目录:/容器内目录:rw 镜像名`
        - rw为默认值
      - 只读
        - 容器实例内部被限制，只能读取不能写
        - `docker run -it --privileged=true -v /宿主机绝对路径目录:/容器内目录:ro 镜像名`
        - 宿主机写如内容可以同步给容器，容器可以读取到

   3. 卷的继承和共享

      - 容器1完成和宿主机的映射
      - 容器2继承容器1的卷规则：`docker run -it --privileged=true --volumnes-from 父类容器 --name u2 ubuntu`，其实这里的 `--volumnes` 就是 `-v`
      - 实现：父容器、子容器、宿主机文件共享
      - 简单来说，无论谁死都不影响文件传递，一主二从


## 8. Docker常规安装简介

1. 总体步骤
   1. 搜索镜像
   2. 拉取镜像
   3. 查看镜像
   4. 启动镜像，服务端口映射
   5. 停止容器
   6. 移除容器
   
2. 安装tomcat
   1. docker hub上查找tomcat镜像：`docker search tomcat`
   2. 从docker hub上拉去tomcat镜像到本地：`docker pull tomcat`
   3. docker images查看是否有拉取到的tomcat
   4. 使用tomcat镜像创建容器实例（也叫运行镜像）：`docker run -it -p 8080:8080 --name t1 tomcat`
   5. 访问 :cat: 首页
      - 问题：最后发现访问报错404异常
      - 解决：
        - 可能没有映射端口或者没有关闭防火墙 
        - 把webapps.dist目录换成webapps
          - 先成功启动tomcat
          - 查看webapps文件夹查看为空
   
3. 安装mysql

   1. `docker search mysql`

   2. `docker pull mysql:8.0.29`

   3. 运行：

      - `docker run -p 33061:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql:8.0.29`

      - `docker exec -it 3ce95ebd240c bash`

        ```bash
        bash-4.4# mysql -uroot -p
        Enter password:
        Welcome to the MySQL monitor.  Commands end with ; or \g.
        Your MySQL connection id is 9
        Server version: 8.0.29 MySQL Community Server - GPL
        
        Copyright (c) 2000, 2022, Oracle and/or its affiliates.
        
        Oracle is a registered trademark of Oracle Corporation and/or its
        affiliates. Other names may be trademarks of their respective
        owners.
        
        Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
        
        mysql> show databases;
        +--------------------+
        | Database           |
        +--------------------+
        | information_schema |
        | mysql              |
        | performance_schema |
        | sys                |
        +--------------------+
        4 rows in set (0.00 sec)
        
        mysql> create database db01;
        Query OK, 1 row affected (0.00 sec)
        
        mysql> use db01;
        Database changed
        mysql> create table t1(id int, name varchar(32));
        Query OK, 0 rows affected (0.01 sec)
        
        mysql> insert into t1 values(1, 'zhangsan')
            -> ;
        Query OK, 1 row affected (0.01 sec)
        
        mysql> select * from t1;
        +------+----------+
        | id   | name     |
        +------+----------+
        |    1 | zhangsan |
        +------+----------+
        1 row in set (0.00 sec)
        
        mysql>
        ```

      - 用工具连接也没问题
      - 问题：
        - 插入中文数据报错：docker上默认字符集编码隐患
        - 删除容器之后，里面的mysql数据怎么办

   4. mysql实战：

      1. 新建mysql容器实例：`docker run -d -p 33061:3306 --privileged=true -v /data/litian_test/mysql/log:/var/log/mysql -v /data/litian_test/mysql/data:/var/liv/mysql -v /data/litian_test/mysql/conf:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=root --name ltmysql mysql:8.0.29`
   
      2. 在宿主机 `/data/litian_test/mysql/conf` 新建 `my.cnf`：通过容器卷同步给mysql容器实例
   
         ```bash
         [client]
         default_character_set = utf8
         [mysqld]
         collation_server = utf8_general_ci
         character_set_server = utf8
         ```
   
      3. 重新启动mysql容器实例再重新进入并查看字符编码：`docker restart ltmysql`
   
         ```bash
         mysql> show variables like 'character%';
         +--------------------------+--------------------------------+
         | Variable_name            | Value                          |
         +--------------------------+--------------------------------+
         | character_set_client     | utf8mb3                        |
         | character_set_connection | utf8mb3                        |
         | character_set_database   | utf8mb3                        |
         | character_set_filesystem | binary                         |
         | character_set_results    | utf8mb3                        |
         | character_set_server     | utf8mb3                        |
         | character_set_system     | utf8mb3                        |
         | character_sets_dir       | /usr/share/mysql-8.0/charsets/ |
         +--------------------------+--------------------------------+
         8 rows in set (0.01 sec)
         ```
   
      4. **结论：docker安装完MySQL并run出容器后，建议请先修改完字符集编码后再新建mysql库-表-插数据**
   
   5. 删除容器后，里面的mysql数据怎么办：数据不丢失

4. 安装redis

   1. 拉取redis镜像到本地

   2. 容器卷记得加 `--privileged=true`

   3. 宿主机新建目录 `/app/redis`：`mkdir -p /app/redis`

   4. 将一个 `redis.conf` 文件模板拷贝进 `/app/redis` 目录下

   5. `/app/redis` 目录下修改 `redis.conf` 文件（默认出厂的原始是redis.conf）
      - 开启redis密码验证（可选）：`requirepass 123`
      - 允许redis外地连接（必须）：`bind 127.0.0.1 ::1`和 `bind 127.0.0.1` 这两行的注释取消
      - 注释 `daemonize yes`，或者设置 `daemonize no` ，因为该配置和docker run中 -d 参数冲突，会导致容器一直启动失败
      - 开启redis数据持久化（可选）：`appendonly yes`
      - 开启外部访问链接（可选）：`protected-mode no`，关闭保护模式

   6. 创建容器，运行镜像：`docker run -p 63791:6379 --name ltredis --privileged=true -v /app/redis/redis.conf:/etc/redis/redis.conf -v /app/redis/data:/data -d redis:6.0.8 redis-server /etc/redis/redis.conf`

      注意：这里不是 `bash` 了，而是 `redis-server xxx`

      测试效果：

      ```bash
      KAZ0VLGPT01:/app/redis # docker exec -it ltredis /bin/bash
      root@1843deb637b4:/data# redis-cli
      127.0.0.1:6379> set k1 v1
      OK
      127.0.0.1:6379> get k1
      "v1"
      127.0.0.1:6379> ping
      PONG
      127.0.0.1:6379> select 15
      OK
      127.0.0.1:6379[15]>
      ```

   7. 验证redis是按照指定的conf启动的：

      - `select 15` 的结果是ok的

      - 退出后修改conf中 `databases 16` 为 `databases 10`

      - 重启redis服务：`docker restart ltredis`

      - 进入容器内测试是否超出index，则为修改成功

        ```bash
        KAZ0VLGPT01:/app/redis # docker exec -it ltredis bash
        root@1843deb637b4:/data# redis-cli
        127.0.0.1:6379> get k1
        "v1"
        127.0.0.1:6379> select 3
        OK
        127.0.0.1:6379[3]> select 15
        (error) ERR DB index is out of range
        ```

5. 安装nginx：见后续Portainer

## 9. Docker复杂安装说明

1. 安装mysql主从复制

   - 主从复制原理（跳过不讲）

   - 做下一步之前的建议

     1. :imp: 直接用mysql:5.7的镜像，会报错容器起不起来，这个问题在下面步骤中解释了，不再细说，但是我发现如果指定容器版本 `mysql:5.7.29`，就没有出现如下问题，更无需修复，所以建议在执行以下代码时，将所有5.9改为5.9.29

     2. :imp: 在重启mysql容器之后，再进去，输入用户名和密码的时候发现：

        ```
        ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)
        ```

        这个问题很玄学，先不要去百度，退出容器之后再进一次发现又好了，就很奇怪。。。==最后是内存不够==

     3. :imp: 注意 `my.cnf` 千万别写成 `my.conf`，切记切记，血的教训

   - 主从搭建步骤

     1. 新建服务器容器实例3307：

        ```bash
        docker run -p 3307:3306 --name mysql-master --privileged=true -v /mydata/mysql-master/log:/var/log/mysql -v /mydata/mysql-master/data:/var/lib/mysql -v /mydata/mysql-master/conf:/etc/mysql -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7
        ```

        > :warning: <span id="4">注意</span>：在这一步可能会报错，容器创建成功但是启不起来，查看容器报错内容：`docker logs mysql-master`发现：
        >
        > ```bash
        > [ERROR] [Entrypoint]: mysqld failed while attempting to check config
        >         command was: mysqld --verbose --help --log-bin-index=/tmp/tmp.WHijR591XA
        >         mysqld: Can't read dir of '/etc/mysql/conf.d/' (Errcode: 2 - No such file or directory)
        > mysqld: [ERROR] Fatal error in defaults handling. Program aborted!
        > ```
        >
        > :book: [原因分析](https://blog.csdn.net/javaboyweng/article/details/130928503)：官方的配置文件已经不放在/etc/mysql底下了
        >
        > :sailboat: 解决方案：
        >
        > 1. 先创建一个简单的mysql容器实例：
        >
        >    ```bash
        >    docker run -p 3307:3306 --name mysql-master -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7
        >    ```
        >
        > 2. 复制里面的`/etc/mysql`文件夹：`docker cp mysql-master:/etc/mysql/. /mydata/mysql-master/conf`
        >
        > 3. 删除这个临时容器：`docker rm -f mysql-master`
        >
        > 4. 重新启动原始命令
     
     2. 进入 `/mydata/mysql-master/conf` 目录下新建 `my.conf`，插入以下内容
     
        ```bash
        [mysqld]
        ## 设置server_id，同一局域网中需要唯一
        server_id=101
        ## 指定不需要同步的数据库名称
        binlog-ignore-db=mysql
        ## 开启二进制日志功能
        log-bin=mall-mysql-bin
        ## 设置二进制日志使用内存大小（事务）
        binlog_cache_size=1M
        ## 设置使用的二进制日志格式（mixed,statement,row）
        binlog_format=mixed  
        ## 二进制日志过期清理时间。默认值为0，表示不自动清理。
        expire_logs_days=7
        ## 跳过主从复制中遇到的所有错误或指定类型的错误，避免slave端复制中断。
        ## 如：1062错误是指一些主键重复，1032错误是因为主从数据库数据不一致
        slave_skip_errors=1062
        ```
     
     3. 修改完配置后重启master实例：`docker restart mysql-master`
     
     4. 进入mysql-master容器
     
        ```bash
        KAZ0VLGPT01:/mydata/mysql-master/conf # docker exec -it mysql-master bash
        bash-4.2# mysql -uroot -p
        Enter password:
        Welcome to the MySQL monitor.  Commands end with ; or \g.
        Your MySQL connection id is 2
        Server version: 5.7.44 MySQL Community Server (GPL)
        
        Copyright (c) 2000, 2023, Oracle and/or its affiliates.
        
        Oracle is a registered trademark of Oracle Corporation and/or its
        affiliates. Other names may be trademarks of their respective
        owners.
        
        Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
        
        mysql>
        ```
     
     5. master容器实例内创建数据同步用户
     
        ```sql
        # 新建用户
        create user 'slave'@'%' identified by '123456';
        # 授权
        grant replication slave, replication client on *.* to 'slave'@'%';
        ```
     
     6. 新建从服务器容器实例3308
     
        ```bash
        docker run -p 3308:3306 --name mysql-slave --privileged=true -v /mydata/mysql-slave/log:/var/log/mysql -v /mydata/mysql-slave/data:/var/lib/mysql -v /mydata/mysql-slave/conf:/etc/mysql -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7
        ```
     
     7. 进入 `/mydata/mysql-slave/conf` 目录下新建 `my.conf`，插入以下内容
     
        ```bash
        [mysqld]
        ## 设置server_id，同一局域网中需要唯一
        server_id=102
        ## 指定不需要同步的数据库名称
        binlog-ignore-db=mysql  
        ## 开启二进制日志功能，以备Slave作为其它数据库实例的Master时使用
        log-bin=mall-mysql-slave1-bin  
        ## 设置二进制日志使用内存大小（事务）
        binlog_cache_size=1M  
        ## 设置使用的二进制日志格式（mixed,statement,row）
        binlog_format=mixed  
        ## 二进制日志过期清理时间。默认值为0，表示不自动清理。
        expire_logs_days=7  
        ## 跳过主从复制中遇到的所有错误或指定类型的错误，避免slave端复制中断。
        ## 如：1062错误是指一些主键重复，1032错误是因为主从数据库数据不一致
        slave_skip_errors=1062  
        ## relay_log配置中继日志
        relay_log=mall-mysql-relay-bin  
        ## log_slave_updates表示slave将复制事件写进自己的二进制日志
        log_slave_updates=1  
        ## slave设置为只读（具有super权限的用户除外）
        read_only=1
        ```
     
     8. 修改完配置后重启slave实例：`docker restart mysql-slave`
     
     9. 在主数据库中查看主从同步状态：`show master status;`（:imp: 真的能看到，如果是empty set，看看是不是配置文件的名称或者内容有问题），并且也可以通过 `show variables like '%log_bin%';` 看 `log_in` 是否开启
     
        ```
        mysql> show master status;
        +------------------------------+----------+--------------+------------------+-------------------+
        | File                         | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
        +------------------------------+----------+--------------+------------------+-------------------+
        | mall-mysql-slave1-bin.000001 |      154 |              | mysql            |                   |
        +------------------------------+----------+--------------+------------------+-------------------+
        1 row in set (0.01 sec)
        ```
     
     10. 进入mysql-slave容器中：`docker exec -it mysql-slave bash`
     
     11. 在**从**数据库中配置主从复制
     
         ```bash
         change master to master_host='10.10.102.111', master_user='slave', master_password='123456', master_port=3307, master_log_file='mall-mysql-bin.000001', master_log_pos=154, master_connect_retry=30;
         ```
     
         - master_host：主数据库的IP地址；
         - master_port：主数据库的运行端口；
         - master_user：在主数据库创建的用于同步数据的用户账号； 
         - master_password：在主数据库创建的用于同步数据的用户密码；
         - master_log_file：指定从数据库要复制数据的日志文件，通过查看主数据的状态，获取File参数；==重要，从master status中拿到的数据==
         - master_log_pos：指定从数据库从哪个位置开始复制数据，通过查看主数据的状态，获取Position参数；==重要，从master status中拿到的数据==
         - master_connect_retry：连接失败重试的时间间隔，单位为秒
     
     12. 在从数据库中查看主从同步状态：`show slave status \G;`
     
         ```
         mysql> show slave status \G;
         *************************** 1. row ***************************
                        Slave_IO_State:
                           Master_Host: 10.10.102.111
                           Master_User: slave
                           Master_Port: 3307
                         Connect_Retry: 30
                       Master_Log_File: mall-mysql-bin .000001
                   Read_Master_Log_Pos: 154
                        Relay_Log_File: mall-mysql-relay-bin.000001
                         Relay_Log_Pos: 4
                 Relay_Master_Log_File: mall-mysql-bin .000001
                      Slave_IO_Running: No
                     Slave_SQL_Running: No
                       Replicate_Do_DB:
                   Replicate_Ignore_DB:
                    Replicate_Do_Table:
                Replicate_Ignore_Table:
               Replicate_Wild_Do_Table:
           Replicate_Wild_Ignore_Table:
                            Last_Errno: 0
                            Last_Error:
                          Skip_Counter: 0
                   Exec_Master_Log_Pos: 154
                       Relay_Log_Space: 154
                       Until_Condition: None
                        Until_Log_File:
                         Until_Log_Pos: 0
                    Master_SSL_Allowed: No
                    Master_SSL_CA_File:
                    Master_SSL_CA_Path:
                       Master_SSL_Cert:
                     Master_SSL_Cipher:
                        Master_SSL_Key:
                 Seconds_Behind_Master: NULL
         Master_SSL_Verify_Server_Cert: No
                         Last_IO_Errno: 0
                         Last_IO_Error:
                        Last_SQL_Errno: 0
                        Last_SQL_Error:
           Replicate_Ignore_Server_Ids:
                      Master_Server_Id: 0
                           Master_UUID:
                      Master_Info_File: /var/lib/mysql/master.info
                             SQL_Delay: 0
                   SQL_Remaining_Delay: NULL
               Slave_SQL_Running_State:
                    Master_Retry_Count: 86400
                           Master_Bind:
               Last_IO_Error_Timestamp:
              Last_SQL_Error_Timestamp:
                        Master_SSL_Crl:
                    Master_SSL_Crlpath:
                    Retrieved_Gtid_Set:
                     Executed_Gtid_Set:
                         Auto_Position: 0
                  Replicate_Rewrite_DB:
                          Channel_Name:
                    Master_TLS_Version:
         1 row in set (0.01 sec)
         ```
     
         `Slave_IO_Running: No`、`Slave_SQL_Running: No`表示还没开始
     
     13. 在从数据库中开启主从同步：`start slave;`
     
     14. 查看从数据库状态发现已经同步：`show slave status \G;`
     
         `Slave_IO_Running: Yes`、`Slave_SQL_Running: Yes`表示成功
     
         > :imp: 如果是发现Slave_IO为No，Slave_SQL为Yes
         >
         > :aerial_tramway: 可能是 `master_log_file` 文件名没写对，比如多了一个空格啥的
     
     15. 主从测试复制
     
         1. 主机新建库、使用库、新建表、插入数据
         2. 从机使用库、查看记录
     
         结果表明：主机创建的表和数据，从机可以看到。

2. 安装redis集群：**cluster（集群）模式-docker版，哈希槽分区进行亿级数据存储**

   > :fox_face: 面试题：1-2亿数据需要缓存，请问如何设计这个存储案例
   >
   > :bow_and_arrow: 回答：单机单台100%不可能，肯定是分布式存储，用redis如何落地？（上述问题阿里P6-P7工程案例和场景设计类必考题目，一般业界有3种解决方案）

   
























------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045/`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome/`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822/`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_/`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
