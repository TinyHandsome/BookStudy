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

- 效果看着不错，还是有点唬人的~

  ![image-20260930105301793](%E5%BE%AE%E4%BF%A1%E6%8A%8A%E8%87%AA%E5%AE%B6%E7%9A%84%E4%BC%81%E4%B8%9A%E7%BA%A7%20AI%20%E7%9F%A5%E8%AF%86%E5%BA%93%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%8C%E5%A4%9A%E5%B9%B3%E5%8F%B0%E8%87%AA%E5%8A%A8%E5%90%8C%E6%AD%A5%EF%BC%8C%E8%87%AA%E5%8A%A8%20Wiki%20%E5%8A%9F%E8%83%BD%E6%83%8A%E8%89%B3%EF%BC%81.assets/image-20260930105301793.png)



**问题**

1. 如果设置对象存储，不是本地local，而是minio就会报错

   [rows:0] SELECT * FROM "system_settings" WHERE key = 'model.max_concurrency' ORDER BY "system_settings"."id" LIMIT 1

   ```
   # ========== B3. 文件存储（通用）==========
   # 文件存储类型：local / minio / cos / tos / s3 / obs / oss / dummy。
   STORAGE_TYPE=local
   # 允许用户使用的存储类型白名单（逗号分隔，留空允许全部）。
   # STORAGE_ALLOW_LIST=local,minio,cos,tos,s3,obs,oss
   # 本地存储根目录（STORAGE_TYPE=local 时用）。
   LOCAL_STORAGE_BASE_DIR=/data/files
   # 本地存储路径前缀（legacy 回填用，一般留空）。
   # LOCAL_STORAGE_PATH_PREFIX=
   # 统一文件大小限制（MB，默认 50）。影响知识库/附件单文件上传、docreader gRPC 消息、浏览器知识库校验。属部署期配置：Go/Nginx/docreader/浏览器四层启动时读一次，运行中改不生效，改后须同步重启四层。
   # MAX_FILE_SIZE_MB=50
   # 技能 zip 上传与 GitHub/ClawHub 来源下载上限（MB，默认 256）。与知识库上传分开：ppt-master 一类技能包会超过 50MB。GitHub zipball 按整仓压缩包计，不是 SKILL.md 子树；仓过大仍会在下载阶段被拒。未设置时不低于 MAX_FILE_SIZE_MB，且不超过 512。Nginx 只对 POST /api/v1/skills/catalog 与 POST /api/v1/sandbox-configs/{id}/skills 放宽到这个值，/install、PATCH 等子路径仍是 MAX_FILE_SIZE_MB。改后须重启 app 与 frontend。
   # MAX_SKILL_BUNDLE_SIZE_MB=256
   
   # ========== B4. 对象存储 provider（按 STORAGE_TYPE 选其一）==========
   # ----- MinIO（STORAGE_TYPE=minio）-----
   # MinIO 端点（host:port）。IM 渠道时必须是 IM 平台公网可达的 host（不能用 minio:9000）。
   MINIO_ENDPOINT=minio:2005
   MINIO_ACCESS_KEY_ID=admin
   MINIO_SECRET_ACCESS_KEY=admin
   MINIO_BUCKET_NAME=weknora
   MINIO_PATH_PREFIX=
   MINIO_USE_SSL=false
   # MinIO 端口（compose 映射用）。
   MINIO_PORT=2005
   MINIO_CONSOLE_PORT=2006
   ```

   解决：只能先按 local 使用了，但是如果这里的配置项没有备注上，对应的容器还是启动起来了

2. 本地部署的大模型是 ip:port 的形式，测试链接会报错

   解决：`J1. SSRF 防护` 这一部分的配置项中，把 ip 放到白名单的配置项中

   ```
   SSRF_WHITELIST=xx.xx.xx.xx
   ```

   