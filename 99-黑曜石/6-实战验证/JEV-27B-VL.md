---
tags:
  - jev
  - LLM
link:
  - https://modelscope.csdn.net/6ac99b41536f457592aecfbf.html
---
AutoTrust AI Lab 开源 JEV-27B-VL，一款基于 Qwen3.8-27B 的多模态决策模型。它可以视为能“看见”的 JEV-27B：沿用原有的 System 1 决策与 System 2 推理能力，并将其扩展至图像输入。

System 1 可在单次前向传播中完成 yes/no 判断、2–256 个选项选择和 0–5 评分，并输出校准概率；System 2 则保留 Qwen3.8-27B 的通用多模态理解与推理能力。JEV-27B-VL 的决策头仅通过纯文本训练，即可零样本迁移至图像。

截至 2026 年 10 月 7 日，JEV-27B-VL 在 **Jev Decision Index 0.3 视觉榜单的 20 个视觉决策模型中排名第一**，并在 13,695 条评测数据上取得 77.8% 的准确率。模型支持最长 256K tokens 上下文，采用 Apache 2.0 协议开源。

![img](JEV-27B-VL.assets/v2-9eed746f1621b2ade0a48356156cae35_1440w.jpg)

部署：[[../3-踩坑笔记/91-docker问题汇总.md#^0800be]]