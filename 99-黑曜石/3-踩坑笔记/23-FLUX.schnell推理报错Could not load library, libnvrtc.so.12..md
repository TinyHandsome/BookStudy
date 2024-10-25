---
banner: Cover/23.png
sticker: emoji//1f434
tags:
  - flux
  - AI绘图
  - nvidia
  - torch
  - diffusers
---
# FLUX.schnell推理报错Could not load library, libnvrtc.so.12. 

[TOC]

## 写在前面

- 背景：flux弄个好了，模型也能跑起来，但是推理的时候就卡卡报错：

  - 一个是上面的错：Could not load library, libnvrtc.so.12.
  - 一个是下面的错：RuntimeError: cuDNN Frontend error: [cudnn_frontend] Error: No execution plans support the graph.

  ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/7c1ba29057a040d9b0d6943b68e12988.png)

- 参考链接：

  - [(SDPA-CUDNN) Make CuDNN Attention Opt in by drisspg · Pull Request #138522 · pytorch/pytorch](https://github.com/pytorch/pytorch/pull/138522)
  - [RuntimeError: cuDNN Frontend error: (cudnn_frontend) Error: No execution plans support the graph. · Issue #9704 · huggingface/diffusers](https://github.com/huggingface/diffusers/issues/9704)


## 解决方案

- 我的环境是：torch=2.5.0+cu124，没错问题就在torch这，先说结论，**torch改为2.4.1即可**

- [具体怎么搞](https://pytorch.org/get-started/previous-versions/)：

  ```bash
  # conda
  conda install pytorch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 -c pytorch
  # pip
  pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1
  ```

- 简单来说就是pytorch2.5的bug导致的，我特么服啦

  ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/b07cee8a1d93485490a8a401f96820e8.png)

- :grin: 兄弟，全网，我搜遍了全网没找到答案，还是靠自己咔咔外网找啊，点个赞不过分吧


------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
