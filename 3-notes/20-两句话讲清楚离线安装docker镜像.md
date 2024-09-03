# 两句话讲清楚离线安装docker镜像

[TOC]

## 写在前面

- 背景：银河麒麟、离线环境，装吧，一装一个不吱声。

- 准备：

  - 首先，你要有个docker，安装好了才能搞镜像是不是，参考我的上一篇：[两句话讲清楚离线安装docker](https://blog.csdn.net/qq_21579045/article/details/141718124)
  
  - 其次，你要能访问 `hub.docker.com`，能够知道你要下载的镜像
  
    > 中国有句古话：“github可以git命令行下载git clone/git pull，也可以通过github页面上点击下载压缩包。~~那么docker必然如此。~~” 我尝试了一万次，硬是没找到hub.docker.com上镜像的下载按钮，真的只能 docker pull 了，家人们~

## 解决方案

1. **下载镜像**：以 `hello-world` 为例，在你能访问 `hub.docker.com` 的服务器里：`docker pull hello-world`，这就下下来了，不过是docker管理的。

2. **导出镜像**：所以我们要打包为tar到当前路径了好操作：`docker save -o hello-world.tar hello-world`，前面的是固定的，这里的 `-o` 是 `output`，后面两个是 **输出** 和 **镜像名** ，如果镜像有不同的版本就得在镜像名这加个标签，比如 `hello-world:latest`

3. **传输镜像**：好了，镜像搞到了，你得传输了把，离线安装，什么叫离线安装，就是把你导出的镜像带到任何你没网的服务器里啊，随便你是u盘，还是倒一手服务器，还是scp命令传输呐。

4. **加载镜像**：总之，导出的镜像终于到了目的离线服务器了（这个服务器你已经离线装过docker了嗷），`docker load -i hello-world.tar`，加载呗，这就用上了，`-i` 是 `input`。

5. 完事儿了，开run吧，一run一个不吱声。检查一下也行：`docker images`。

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/45564669971c482ba4dab4e02c8d822f.png)

------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
