# 浅谈视觉大模型Sora

### 背景

自2022年11月ChatGPT发布以来，AI技术的出现标志着一个重大转变，重塑了交互方式，并深入融入了日常生活和行业的各个方面。在这一势头的推动下，OpenAI于2024年2月发布了Sora，这是一种文本到视频的生成式AI模型，可以根据文本提示生成逼真或想象中的场景视频。与以前的视频生成模型相比，**Sora以其能够高质量地生成长达1分钟的视频而与用户的文本指令保持一致而与众不同**。Sora的进步体现了长期以来AI研究任务的使命，即赋予AI系统理解和互动的物理世界的能力。这涉及开发能够不仅解释复杂用户指令，而且应用这种理解来通过动态和丰富的上下文模拟解决现实世界问题的AI模型。[^1][^2]



![image-20240301103732496](%E6%B5%85%E8%B0%88%E8%A7%86%E8%A7%89%E5%A4%A7%E6%A8%A1%E5%9E%8BSora.assets/image-20240301103732496.png)



















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

  **训练过程 = 1 视频视觉特征的提取压缩 + 2 扩散模型的训练**

---

有没有人解释下Sora原理? - Likelihood的回答 - 知乎
https://www.zhihu.com/question/644790078/answer/3401041037

Diffusion是一个**迭代过程**：

- 先向一个 图片中增加噪声，那么对每个图片，清晰图片`X + Noise_x = X'`（含有噪声的图片）
- 如果训练一个模型（通常用UNet模型），能够预测`X'`中噪声`Noise_x`， 那么用`X' - Noise_x`就能恢复到X

![](https://pic1.zhimg.com/v2-adddb6d45b91fd180363e7469bcd70ee_b.jpg)

当对一个完全是噪音的图片，逐渐去掉噪声的时候，就能得到一个清晰的图片（循环迭代预测噪声过程，从而得到清晰图）：

![](https://pic2.zhimg.com/v2-aeec28a93faebc4c30abbee810efc5b9_b.jpg)

一般会引入一个Condition，比如文字的condition，这样基于这个condition，就能得到一个该Condition下清晰的图片，这就是Text2Image的大致原理

![](https://pica.zhimg.com/v2-7ac9542102d4a3f6f2cdf076cd06e0a4_b.jpg)







[^1]: https://mp.weixin.qq.com/s/1DZWMNIp0O33LKhxL38c1Q "Sora：大视觉模型的背景、技术、局限性和机遇综述"
[^2]: https://arxiv.org/pdf/2402.17177.pdf