# docker问题汇总

[TOC]

==docker问题汇总贴，不断学习不断更新。当前更新时间：**20240903**==

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/df9b936058c94cd8a81a9f262a5d9163.png)

## 银河麒麟不删podman无法运行docker

- 报错内容：

  ```
  docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: container_linux.go:318: starting container process caused "permission denied": unknown.
  ```

- 最终解决方案：删掉podman就ok了，`yum remove podman`

- 原因分析：

  - **检查镜像架构是否正确**：查看镜像架构：`docker inspect hello-world`，兄弟，amd64架构你才能跑啊，别搞成arm了

    ![image-20240903092531460](https://i-blog.csdnimg.cn/direct/477137f779924770a297982c6cdcc297.png)

  - [网上有说是版本问题的](https://blog.csdn.net/2401_84926028/article/details/138768767)

    > 这里要安装 docker-ce 19.03 版本，因为我在使用最新版 20.10 启动容器时出现了未知的权限问题，而麒麟服务器操作系统资料相对较少，我未能找到相应的解决方案，只好退而求其次，换到上一个稳定版本。

  - 最后发现删除podman可以解决：[参考1](https://blog.csdn.net/yzlz888/article/details/140043920)、[参考2](https://blog.csdn.net/qq_45547688/article/details/138150469)

    > 找了N多了地方 最后发现是这个podman惹的祸
    >
    > yum remove podman
    >
    > 删掉后docker start *
    >
    > 世界清净了







------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
