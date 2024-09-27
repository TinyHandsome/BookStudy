# LINK学起来家人们

[TOC]

## 大模型

### :star:全面解析大模型

1. 全面解析LoRA、QLoRA、RLHF，PPO，DPO，Flash Attention、增量学习等大模型算法：https://mp.weixin.qq.com/s/2ML5xyTQgZog_dbN2RZNXg
2. 当有人问我“什么是大模型”，我顿住了！ - 掘金安东尼的文章 - 知乎
   https://zhuanlan.zhihu.com/p/688385792

### HuggingFace

- Huggingface 超详细介绍 - 基本粒子的文章 - 知乎
  https://zhuanlan.zhihu.com/p/535100411
- 使用Transformers实现Chat：https://qwen.readthedocs.io/zh-cn/latest/inference/chat.html#streaming-mode

### AI变现

1. 30个AI变现案例，太全了，赶紧实操起来 - 萝卜大杂烩的文章 - 知乎
   https://zhuanlan.zhihu.com/p/683477341

### RAG

- 创业：大模型RAG系统三个月的开发心得和思考 - 八一菜刀的文章 - 知乎
  https://zhuanlan.zhihu.com/p/690298565
  
  ![img](LINK%E5%AD%A6%E8%B5%B7%E6%9D%A5%E5%AE%B6%E4%BA%BA%E4%BB%AC.assets/v2-55cbdfc1c7c16d566518ce1f323cdc0f_1440w.jpg)
  
- **LangChain-ChatChat详解**：https://blog.csdn.net/qq_41185868/article/details/132529666
  
- 一文入门最热的 LLM 应用开发框架 LangChain - 腾讯技术工程的文章 - 知乎
  https://zhuanlan.zhihu.com/p/647274130

- RAG大模型增强生成能力案例有哪些？ - 产品二姐的回答 - 知乎https://www.zhihu.com/question/638503601/answer/3384081209

- 图解高级RAG技术 - iyacontrol的文章 - 知乎 https://zhuanlan.zhihu.com/p/674755232

- LLM（廿一）：从 RAG 到 Self-RAG —— LLM 的知识增强 - 紫气东来的文章 - 知乎https://zhuanlan.zhihu.com/p/661465330

- 揭秘Self-RAG技术内幕 - AI pursuer的文章 - 知乎
  https://zhuanlan.zhihu.com/p/669030475
  
- 动手实现一个最小RAG——TinyRAG - 不要葱姜蒜的文章 - 知乎
  https://zhuanlan.zhihu.com/p/685989556

  ![image-20240313083514292](LINK%E5%AD%A6%E8%B5%B7%E6%9D%A5%E5%AE%B6%E4%BA%BA%E4%BB%AC.assets/image-20240313083514292.png)

### Agent

- AI Agents in One Minute - Yuxi Li的视频 - 知乎
  https://www.zhihu.com/zvideo/1731598973545259008

### 大模型干架

![Image](LINK%E5%AD%A6%E8%B5%B7%E6%9D%A5%E5%AE%B6%E4%BA%BA%E4%BB%AC.assets/Image.png)

#### 星火大模型

![Image](LINK%E5%AD%A6%E8%B5%B7%E6%9D%A5%E5%AE%B6%E4%BA%BA%E4%BB%AC.assets/Image-17092725948083.png)

![Image](LINK%E5%AD%A6%E8%B5%B7%E6%9D%A5%E5%AE%B6%E4%BA%BA%E4%BB%AC.assets/Image-17092725983814.png)

### AI绘画

- **ComfyUI介绍(官方直译)详细部署教程和使用** - 瞿同学(Darren)的文章 - 知乎
  https://zhuanlan.zhihu.com/p/662041596

- ai绘画主流模型有哪些？ - M-ing的回答 - 知乎https://www.zhihu.com/question/565575317/answer/3149736971

- dalle，prompt推荐和使用案例：https://zhuanlan.zhihu.com/p/660775448

  ![Image](LINK%E5%AD%A6%E8%B5%B7%E6%9D%A5%E5%AE%B6%E4%BA%BA%E4%BB%AC.assets/Image-17092723546122.png)



### Stable Diffusion

1. 【翻译】How Stable Diffusion Work - 给小白看的StableDiffusion原理介绍 - Sparrowfc的文章 - 知乎 https://zhuanlan.zhihu.com/p/616195288
2. Diffusion Model：从基础到前沿 - JunMa的文章 - 知乎 https://zhuanlan.zhihu.com/p/622800350
3. stable diffusion 本地部署：https://zhuanlan.zhihu.com/p/626006585



### SORA

Sora大模型从读万卷书到行万里路：https://mp.weixin.qq.com/s/j12LX7xlqfFeNFLHVHK33A

  - Sora的惊艳之处
    - Sora目前的缺陷
    - Sora技术报告主要内容
    - OpenAI的技术理想

Sora是Transformer架构和Diffusion model的合体，OpenAI继续Scale up（甚至此前有Sam Altman希望用7万亿美元重构芯片市场的传闻），LLM（大模型）从此前的读万卷书到现在开始行万里路——从视频和真实世界学习。

---

Sora的训练过程-超级人话版 - 李明骏的文章 - 知乎
https://zhuanlan.zhihu.com/p/682450509

- Sora的训练数据: 大量带有文本描述的视频画面和视频内容总结

  **训练数据= 1 视频图像 + 2帧级的画面文本描述 + 3 视频内容总结（视频的生成指令描述 ）**

- Sora的训练方法：将带有相应文本描述的视频，通过视觉编码器先变为“visual-patches”（视觉特征标记，对标文本的token），然后再通过Transformer网络进行多次压缩，变成低维的向量，对比和指令prompt的向量的相似性，不断去拟合。

  **训练过程= 1视频视觉特征的提取压缩+ 2扩散模型的训练**

---



## 加密算法

- 对称加密和非对称加密，图文：https://zhuanlan.zhihu.com/p/436455172



## 机器学习

### 正则化

- 正则化是什么：https://www.zhihu.com/question/20924039/answer/3362200530



## 深度学习

### 卷积神经网络

- 从此明白了卷积神经网络（CNN）：https://mp.weixin.qq.com/s/-X2jd1RDM-Y1ujR7ndfcMA

### GAN和VAE

- VAE、GAN 这种生成模型和 transformer 有什么区别？ - YouZhi的回答 - 知乎
  https://www.zhihu.com/question/558574918/answer/3356124092

### YOLO

- 《YOLO全面回顾：从YOLOV1到现在及未来》 - 松林的文章 - 知乎
  https://zhuanlan.zhihu.com/p/641297736

### Transformer

- 啥是Transformer：https://blog.csdn.net/weixin_48978134/article/details/125567184



## 学英语

### 托业

1. 经验
   - 题型经验：https://zhuanlan.zhihu.com/p/371913297
   - 题型介绍：https://zhuanlan.zhihu.com/p/377220442
2. 听力
   - 托业听力b站获取：https://space.bilibili.com/289993698/



## 前端设计

### 颜色设计

- 有哪些设计较好的开源 PyQt/Qt/Qml 应用？ - AtomDream的回答 - 知乎https://www.zhihu.com/question/39607624/answer/3242995186

  ![Image](LINK%E5%AD%A6%E8%B5%B7%E6%9D%A5%E5%AE%B6%E4%BA%BA%E4%BB%AC.assets/Image-17092722608691.png)



## 后端开发

### 消息推送

1. 我有七种实现web实时消息推送的方案！：https://mp.weixin.qq.com/s/FkD6zUZQDSikRpR43o9MRg

   ![Image](LINK%E5%AD%A6%E8%B5%B7%E6%9D%A5%E5%AE%B6%E4%BA%BA%E4%BB%AC.assets/Image-17098616826911.png)





## Vue

1. markdown实现解析：https://blog.csdn.net/it_xushixiong/article/details/131183140

## python开发

### 白名单网页

推荐：`https://mirrors.aliyun.com/pypi/simple/`

```
https://hub.docker.com/
https://huggingface.co/
https://www.google.com/
https://github.com/
https://openai.com/
https://pypi.org/
https://repo.anaconda.com/
https://www.anaconda.com/
https://pubchem.ncbi.nlm.nih.gov/
https://download.pytorch.org/
https://data.dgl.ai/
https://www.kaggle.com/
https://stackoverflow.com/
https://3x.antdv.com/
https://fastapi.tiangolo.com/
https://docs.djangoproject.com/
https://scikit-learn.org/
https://www.tensorflow.org/
https://botorch.org/
https://docs.vllm.ai/
https://python.langchain.com/
https://dashboard.cohere.com/
https://pypi.tuna.tsinghua.edu.cn/simple/
https://mirrors.aliyun.com/pypi/simple/
https://mirrors.ustc.edu.cn/
https://mirrors.tuna.tsinghua.edu.cn/
https://pubchem.ncbi.nlm.nih.gov/
https://www.modelscope.cn/
https://www.paddlepaddle.org.cn/
https://hf-mirror.com/
https://dashscope.alyuncs.com/
```

