---
link:
  - https://mp.weixin.qq.com/s/XbHioPdFbRouKaaptnI_nA
tags:
  - LLM
  - agent
  - wiki
---
Karpathy 写了一篇设计文档，描述了一种完全不同的思路——用 LLM **持续构建并维护**一个结构化的个人 Wiki。

- **传统 RAG 的逻辑**是这样的：用户提问 → 向量检索相关段落 → LLM 基于段落临时生成答案 → 结束。

  每次对话都是从零开始，互相独立。知识没有积累，上下文没有沉淀，不管你用了多久，系统对你领域的"理解"不会比第一天更深。

- **LLM Wiki 的逻辑**是另一套：

  - 导入文档 → LLM 两步分析+生成 → 结构化 Wiki 页面持久存储
  - 用户提问 → 多相位检索（关键词+图谱扩展+可选向量）→ 基于已编译知识库回答

  区别在于：**知识是被"编译"过的**。LLM 读完你的文档后，不是直接存下来备查，而是先消化、分析、生成结构化的 Wiki 页面——带 YAML frontmatter、带 `[[wikilink]]` 交叉引用、有来源追溯，然后这个 Wiki 会持续被维护和更新。用得越久，Wiki 越丰富，知识网络越稠密，回答质量越高。这跟"用了半年感觉一样"的 RAG 是根本不同的产品。

两步思维链摄取：**先分析，再生成**。这是 LLM Wiki 对 Karpathy 原始设计最关键的工程改进之一。

**第一步（分析）**：

- 提取关键实体、概念、论点
- 识别与现有 Wiki 内容的连接点
- 发现矛盾和知识张力
- 给出 Wiki 结构建议

**第二步（生成）**：

- 基于分析结果生成带 frontmatter 的来源摘要页
- 生成实体页、概念页（含交叉引用）
- 更新 `index.md`、`log.md`、`overview.md`
- 标记需要人工判断的 Review 项目

![图片](Karpathy%20%E7%9A%84%E7%9F%A5%E8%AF%86%E5%BA%93%E6%9E%84%E6%83%B3%E8%A2%AB%E4%BA%BA%E5%81%9A%E6%88%90%E6%A1%8C%E9%9D%A2%E5%BA%94%E7%94%A8%E4%BA%86%EF%BC%8C%E8%80%8C%E4%B8%94%E5%81%9A%E5%BE%97%E7%9B%B8%E5%BD%93%E6%89%8E%E5%AE%9E%EF%BC%8C%E5%B7%B2%E5%9C%A8%20Github%20%E4%B8%8A%E6%96%A9%E8%8E%B7%205.8k+%20Star%EF%BC%81.assets/640.webp)

![图片](Karpathy%20%E7%9A%84%E7%9F%A5%E8%AF%86%E5%BA%93%E6%9E%84%E6%83%B3%E8%A2%AB%E4%BA%BA%E5%81%9A%E6%88%90%E6%A1%8C%E9%9D%A2%E5%BA%94%E7%94%A8%E4%BA%86%EF%BC%8C%E8%80%8C%E4%B8%94%E5%81%9A%E5%BE%97%E7%9B%B8%E5%BD%93%E6%89%8E%E5%AE%9E%EF%BC%8C%E5%B7%B2%E5%9C%A8%20Github%20%E4%B8%8A%E6%96%A9%E8%8E%B7%205.8k+%20Star%EF%BC%81.assets/640-17906490247862.png)
