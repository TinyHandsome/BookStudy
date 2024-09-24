# 两句话讲清楚离线安装docker

[TOC]

## 写在前面

- 背景：银河麒麟、离线环境，装吧，一装一个不吱声。

- 参考链接：https://blog.csdn.net/zhaogangyyxf/article/details/141328640

- 准备：

  - **docker安装包**：文件类型是一个压缩包。一般是要去docker官网下的，懂我意思吧，不过之前国内镜像不好使，又突然好使了，比如 [阿里的镜像](http://mirrors.aliyun.com/docker-ce/linux/static/stable/)，进去下载就行。

    > `CE`版本是什么意思，就是 `Community Edition` ，社区版，更新会频繁一些，不是很稳定，所以一般下普通的就行。

    ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/77ab01a062e84f59aebb51e109322e8d.png)

  - **docker-compose**：文件类型是一个二进制文件。虽然你找的是docker，但后面肯定也要用到docker-compose，教程也一并给出。比起docker不好弄，docker-compose稍微方便一点，从github上直接下。

    ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/18a81a57f22047d9a339a8e805158f07.png)

    > Docker 主要是用来管理单个容器，而 Docker Compose 则是用来组织和编排多个容器，形成一个完整的、多服务的应用环境


## 解决方案

1. 编写`docker.service`脚本，后面要用，不懂？抄就完了。写了放哪儿？跟docker、docker-compose同一级先放着吧。

   ```bash
   docker.service
    
   [Unit]
   Description=Docker Application Container Engine
   Documentation=https://docs.docker.com
   After=network-online.target firewalld.service
   Wants=network-online.target
    
   [Service]
   Type=notify
   # the default is not to use systemd for cgroups because the delegate issues still
   # exists and systemd currently does not support the cgroup feature set required
   # for containers run by docker
   ExecStart=/usr/bin/dockerd
   ExecReload=/bin/kill -s HUP $MAINPID
   # Having non-zero Limit*s causes performance problems due to accounting overhead
   # in the kernel. We recommend using cgroups to do container-local accounting.
   LimitNOFILE=infinity
   LimitNPROC=infinity
   LimitCORE=infinity
   # Uncomment TasksMax if your systemd version supports it.
   # Only systemd 226 and above support this version.
   #TasksMax=infinity
   TimeoutStartSec=0
   # set delegate yes so that systemd does not reset the cgroups of docker containers
   Delegate=yes
   # kill only the docker process, not all processes in the cgroup
   KillMode=process
   # restart the docker process if it exits prematurely
   Restart=on-failure
   StartLimitBurst=3
   StartLimitInterval=60s
    
   [Install]
   WantedBy=multi-user.target
   ```

2. 解压docker，移动到 `/usr/bin/`目录。本地解压的删不删随你，反正没用了：`rm -rf docker/`

   这里的 `-*` 是让你写自己的版本，别照抄啊

   ```bash
   tar -xvf docker-*.tgz
   cp -p docker/* /usr/bin/
   ```

3. 移动docker-compose到 `/usr/local/bin/` 目录，且改名为 `docker-compose`，增加执行权限，依然删不删随你

   这里的 `-*` 是让你写自己的版本，别照抄啊

   ```bash
   cp docker-compose-* /usr/local/bin/docker-compose
   chmod +x /usr/local/bin/docker-compose
   ```

4. 移动docker.service，刚让你抄的那个，到 `/etc/systemd/system/` 目录，增加执行权限，依然删不删随你

   ```bash
   cp docker.service /etc/systemd/system/
   chmod +x /etc/systemd/system/docker.service
   ```

5. 重新加载配置文件，启动docker，设置开机自启

   ```bash
   systemctl daemon-reload
   systemctl start docker
   systemctl enable docker.service
   ```

6. 完成了已经，检查一下吧

   ```bash
   docker -v
   docker-compose -v
   ```


------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
