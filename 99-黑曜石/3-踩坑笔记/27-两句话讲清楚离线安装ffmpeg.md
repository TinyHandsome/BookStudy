---
sticker: emoji//1f3b9
tags:
  - ffmpeg
  - whisper
  - pipeline
  - 离线
banner: 3-踩坑笔记/27-两句话讲清楚离线安装ffmpeg.assets/4ea1bf7cc5fd498b90451b29e4eaf25c.png
---
# 两句话讲清楚离线安装ffmpeg

[TOC]

## 写在前面

- 摘要

  在我对开源语音转文字大模型whisper胡搞瞎搞的时候，发现报错了，服务启没有ffmpeg，好家伙，我服务器离线啊，我conda搬运的环境啊，我的天啊，开整。

- 环境

  - 平平无奇Ubuntu，不过其他系统也无所谓，毕竟我们是源码编译
  - 跟我其他的教程很像啊，其实是一样的，但是我再研究之前不知道啊，好记性不如烂笔头吧

- 参考链接

  - http://ffmpeg.org/download.html

  - 直接下就完了：我下的 `ffmpeg_7.1.orig.tar.xz`，看到这个，诶？有点眼熟，但好像不太熟

    ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/4ea1bf7cc5fd498b90451b29e4eaf25c.png)

    ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/d3db21fe11384dde862101540c4e2b20.png)


## 解决方案

1. 眼熟的是 `.gz` ，那么 `.xz` 是啥

   > `.xz`和`.gz`是两种不同的文件压缩格式，主要区别在于压缩算法、压缩效率和用途：==来自GPT-4o==
   >
   > 1. **压缩算法**：
   >    - `.xz` 使用的是 LZMA（Lempel-Ziv-Markov chain algorithm）算法。这个算法以高压缩率而著称。
   >    - `.gz` 使用的是 DEFLATE 算法，是一种结合了LZ77和哈夫曼编码的算法。它是GNU项目的 gzip 工具的一部分。
   >
   > 2. **压缩效率和速度**：
   >    - `.xz` 通常提供更高的压缩率，这意味着在相同的文件大小下，`.xz` 压缩后的文件通常比 `.gz` 更小。但是，`.xz` 的压缩速度通常较慢，解压速度也可能较慢。
   >    - `.gz` 的压缩速度和解压速度通常比 `.xz` 快，因此在需要快速压缩和解压的情境下可能更适合。
   >
   > 3. **用途和兼容性**：
   >    - `.xz` 常用于需要高压缩比的场合，适合于存储和传输较大的文件。
   >    - `.gz` 是一种更传统的格式，广泛用于 UNIX 和 Linux 系统中，常用于 tar 打包的二进制文件（如 `.tar.gz`）。
   >
   > 选择哪种格式通常取决于你对压缩比和压缩速度的需求。在传输带宽或存储空间非常宝贵的情况下，`.xz` 可能是更好的选择。而在需要快速处理的场合，`.gz` 可能更合适

2. 所以我们要用 `tar -xvf ffmpeg_7.1.orig.tar.xz`，所以这里没有 `-z`，因为用的不是 `gzip`

   > 当你使用 `tar` 命令来处理 `.tar.gz` 或类似格式的文件时，`-zxvf` 是一个常用的选项组合。每个选项的含义如下：
   >
   > 1. **`-z`**：代表 "gzip"，表示 `tar` 工具需要通过 `gzip` 来处理压缩。这个选项用于处理 `.gz` 格式的压缩文件。
   >
   > 2. **`-x`**：代表 "extract"（提取），用于从归档文件中提取文件。这是用来解压缩和解档文件的核心选项。
   >
   > 3. **`-v`**：代表 "verbose"（详细），用于在命令执行过程中输出详细信息。输出提取的每个文件的名称，方便用户查看处理进度和内容。
   >
   > 4. **`-f`**：代表 "file"，表示后面的参数紧跟的是要处理的目标文件名称。告诉 `tar` 哪个文件是要被处理的压缩归档文件。
   >
   > 因此，`tar -zxvf filename.tar.gz` 的完整命令执行过程是：
   >
   > - 使用 `gzip` （`-z`）解压缩文件。
   > - 从压缩归档文件中提取内容（`-x`）。
   > - 在提取过程中输出每个文件的名称（`-v`）。
   > - 从指定的归档文件中提取数据，目标文件由 `-f` 设定，它要求你指定文件名（如 `filename.tar.gz`）。
   >
   > 这个命令最终的作用是解压并解档 `filename.tar.gz`，同时在终端显示解压过程中每个文件提取的信息

3. 后面的就一样了
   1. `mkdir build && cd build` ，创建 build 文件夹并进入
   2. `../configure` 运行配置程序，注意，这里会报错，让你加上了 `--disable-x86asm`，行吧加就加呗
   3. `make && make install` ，编译安装，时间稍微有点久
   
4. 完事儿，`ffmpeg -version` 看看吧。ok完事儿了，我的大模型也能正常启动啦~

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/6334b2f86e764eac86ce3c02624a6d6b.png)


------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
