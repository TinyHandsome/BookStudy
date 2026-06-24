---
banner: 5-技术文档/一文搞懂MCP和A2A.assets/640-17452847176304.webp
sticker: emoji//1f916
reference:
  - https://mp.weixin.qq.com/s/7w4Rc3k_xC6dt_9W8LGHig
tags:
  - agent
  - mcp
  - a2a
  - LLM
---
# 一文搞懂MCP和A2A

**MCP**（Model-Context Protocol，模型上下文协议）和**A2A**（Agent-to-Agent，智能体到智能体）是大模型应用中两个重要的协议，分别侧重于智能体与外部工具的交互以及智能体之间的协作。

![How MCP+A2A Could Revulazanize Software Industry](一文搞懂MCP和A2A.assets/640-17452847176304.webp)

## MCP

💡 **MCP 是什么？**

- MCP是一种标准化协议，旨在为人工智能模型（如大语言模型）与外部工具、数据源之间的交互提供统一接口。
- MCP是AI智能体与外部工具的"USB接口"，定义了AI模型与外部工具（如API、数据库、文档编辑器等）的交互标准，开发者无需为每个工具单独开发适配代码。
- MCP协议旨在实现大型语言模型（LLM）与外部数据源和工具之间的无缝集成，通过提供标准化的接口，使AI应用程序能够安全、可控地与本地或远程资源进行交互。

![What is Model Context Protocol (MCP)? How it simplifies AI integrations  compared to APIs | AI Agents That Work](一文搞懂MCP和A2A.assets/640.webp)

:bulb: **MCP Server 和 MCP Client 是什么？**

- MCP Server 和 MCP Client 是模型上下文协议（MCP）中的两个核心组件。

- 以支付宝MCP为案例，MCP Server 和 MCP Client 的定义与功能如下：

  ![img](一文搞懂MCP和A2A.assets/640-17452845641742.webp)

  - MCP Server：`@alipay/mcp-server-alipay` 是支付宝开放平台提供的 MCP Server，让你可以轻松将支付宝开放平台提供的交易创建、查询、退款等能力集成到 LLM 应用中，并进一步创建具备支付能力的智能工具。
  - MCP Client：开发者构建的“支付能力调用端”，通常是 AI 应用或智能体，负责向 MCP Server 发起支付请求并处理响应。例如，一个 AI 助手通过自然语言交互，引导用户完成支付流程。

  ```json
  {
    "mcpServers": {
      "mcp-server-alipay": {
        "command": "npx",
        "args": ["-y", "@alipay/mcp-server-alipay"],
        "env": {
          "AP_APP_ID": "2014...222",
          "AP_APP_KEY": "MIIE...DZdM=",
          "AP_PUB_KEY": "MIIB...DAQAB",
          "AP_RETURN_URL": "https://success-page",
          "AP_NOTIFY_URL": "https://your-own-server"
        }
      }
    }
  }
  ```


## A2A

:bulb: **A2A（Agent-to-Agent，智能体到智能体）是什么？**

- A2A是一种开放协议，旨在实现不同智能体之间的直接互通与协作。
- A2A是智能体间的"外交协议"，专注于不同AI智能体间的跨平台协作。通过HTTP/SSE等技术，支持智能体发现彼此能力、任务协调及多模态交互。例如，物流Agent与仓储Agent可实时同步货物状态。

![图片](一文搞懂MCP和A2A.assets/640-17452849255266.gif)

:bulb: **SSE（Server-Sent Events，服务器发送事件）是什么？**

- SSE是一种基于 HTTP 协议的技术，允许服务器向客户端单向、实时地推送数据。
- SSE是实时数据推送的"广播电台"，开发者可以在客户端通过创建一个 EventSource 对象与服务器建立持久连接，服务器则通过该连接持续发送数据流，而无需客户端反复发送请求。在AI协作场景中，A2A协议利用SSE实现智能体间的实时状态同步。

![A simple guide to Server Sent Events (SSE) and EventSource | by Omer  Keskinkilic | Pon.Tech.Talk | Medium](一文搞懂MCP和A2A.assets/640-17452849734498.webp)

以高德地图开放平台为例，通过通用级 SSE（Server-Sent Events）协议实现A2A（Agent-to-Agent）交互，可以构建一个基于地理信息服务的智能体协作框架。

- AI Agent → Map Service Agent：通过 REST API 或 WebSocket 发送请求（如“查询从 A 到 B 的最优路径”）。
- Map Service Agent → AI Agent：通过 SSE 推送实时地理数据（如“当前路段拥堵，建议绕行”）。

![图片](一文搞懂MCP和A2A.assets/640-174528502830610.webp)

![图片](一文搞懂MCP和A2A.assets/640-174528506614712.webp)