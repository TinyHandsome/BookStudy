---
link:
  - https://mp.weixin.qq.com/s/vZcHacSH32qxM88BGtCSBw
tags:
  - agent
  - LLM
---
WeKnora 是一个「**多源知识同步 → RAG 检索 → Agent 推理 → 自动 Wiki → Skill 执行 → 企业级权限与集成**」系统。一套能够持续运转的：**企业级 AI 知识系统。**

- Github：[Tencent/WeKnora: Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.](https://github.com/Tencent/WeKnora)

- 官网：https://weknora.weixin.qq.com/

- 实践步骤：
  1. **把分散资料接进来**：除了常规数据源，还支持飞书、gitlab、ima、notion、钉钉等
  2. **从 RAG 问答，到 Agent 推理**
     - 支持 BM25、向量检索、Rerank、父子分块、GraphRAG 等检索方式，并可以在回答中保留引用来源
     - 在这个基础上，WeKnora 又加入了 **ReAct** **Agent**，和传统的「提问 → 检索 → 回答」不同，Agent 可以根据任务，组合知识库检索、Web Search、MCP、Skill 等工具，完成多步骤的信息获取和分析。
  3. **自动 Wiki**：WeKnora 比较 **有辨识度** 的一项能力
     - 普通的 AI 知识库更多是的解决「怎么从已有资料里找到知识」
     - WeKnora 的 Wiki 模式，会进一步让 Agent 读取原始资料，自动生成结构化、彼此关联的 Markdown Wiki 页面，并形成可视化知识图谱。:bulb: [[5-技术文档/Karpathy 的知识库构想被人做成桌面应用了，而且做得相当扎实，已在 Github 上斩获 5.8k+ Star！.md|跟 Karpathy 的 LLM Wiki 一样]]
  4. **长期记忆和 Skill**：其中包括 Skill Catalog、沙箱运行环境和跨会话长期记忆。
  5. **企业场景**：多工作空间、Owner / Admin / Contributor / Viewer 四级 RBAC 权限、资源归属、审计日志、细粒度 API Key，以及本地、Docker、Kubernetes 和私有化部署等。

- 部署方式：

  ```bash
  git clone https://github.com/Tencent/WeKnora.git
  cd WeKnora
  cp .env.example .env    # 按需编辑 .env，详见文件内注释
  docker-compose --profile full pull     # 拉取最新镜像
  docker-compose --profile full up -d    # 启动核心服务
  
  docker-compose down     # 停止服务
  ```

- 先启动 langfuse ，获取 langfuse 的公钥私钥，填入配置文件中

  ```bash
  docker compose --profile langfuse up -d
  ```

  