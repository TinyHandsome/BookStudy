---
link:
  - https://mp.weixin.qq.com/s/V8Bl3qkpSWA3qImyeeZTxA
tags:
  - qwen
  - qwen-image
  - 图片生成
---
# 拿下开源生图第一，千问 Qwen-Image-2.1 把生图卷出新高度

- 部署：参考 [Qwen/Qwen-Image-2.1 | vLLM Recipes](https://recipes.vllm.ai/Qwen/Qwen-Image-2.1) 完成[[../3-踩坑笔记/91-docker问题汇总#^5e20bf|部署Qwen-Image-2.1]]
- Github：[QwenLM/Qwen-Image-2.1: Qwen's most powerful open-source image generation model](https://github.com/QwenLM/Qwen-Image-2.1)
- HF：[Qwen/Qwen-Image-2.1 · Hugging Face](https://huggingface.co/Qwen/Qwen-Image-2.1)
- 参数：7b
- 分辨率：原生支持 2k
- 描述：它成为了千问图像系列当前最平衡、性价比最高开源生图模型。公开评测结果显示，Qwen-Image-2.1 取得开源模型第一，得分甚至超过了 Nano Banana 2.0。
- 特点：可直接生成可用透明素材，多图片编辑，文字准确性、画面质感

![](拿下开源生图第一，千问Qwen-Image-2.1把生图卷出新高度.assets/file-20260921133605117.png)

性能不错的同时，Qwen-Image-2.1 还对模型的推理过程进行了优化，核心思路是减少不必要的重复计算。在一次图像编辑中，输入的参考图和编辑指令不会随着每一步生成而改变。因此，新模型使用混合粒度注意力结构，文本部分（系统前缀、编辑指令）遵循传统 Token 级因果掩码，逐词进行严格的序列计算以保证语义逻辑理解的连贯性，图像生成部分则采用 Chunk 级掩码，并通过 KV Cache 的机制在首步计算后缓存这些静态上下文，供后续生成步骤复用。

![](拿下开源生图第一，千问Qwen-Image-2.1把生图卷出新高度.assets/file-20260921133852829.png)
![](拿下开源生图第一，千问Qwen-Image-2.1把生图卷出新高度.assets/file-20260921135331766.png)

![](拿下开源生图第一，千问Qwen-Image-2.1把生图卷出新高度.assets/file-20260921135718639.png)


